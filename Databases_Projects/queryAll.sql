SELECT first_name, last_name, email, addr_city 
FROM folk INNER JOIN folk_emailaddrs INNER JOIN resides_at 
WHERE folk.folk_id = folk_emailaddrs.folk_id AND folk.folk_id = resides_at.folk_id;

SELECT addr_city, addr_state, COUNT(*)
FROM resides_at
GROUP BY addr_city
ORDER BY COUNT(*) DESC;

SELECT place.addr_state, COUNT(*)
FROM place INNER JOIN residence
WHERE place.addr_state = residence.addr_state AND place.addr_city = residence.addr_city AND 
place.addr_street_number = residence.addr_street_number AND place.addr_street_name = residence.addr_street_name
GROUP BY place.addr_state
ORDER BY place.addr_state;

SELECT folk.folk_id, registry.voting_date
FROM folk INNER JOIN registry
WHERE folk.folk_id = registry.folk_id;

SELECT voting_center.center_acronym, COUNT(*)
FROM voting_center INNER JOIN place INNER JOIN place_coords INNER JOIN registry
WHERE place.addr_state = voting_center.addr_state AND place.addr_city = voting_center.addr_city AND 
place.addr_street_number = voting_center.addr_street_number AND place.addr_street_name = voting_center.addr_street_name
AND place.coord_id = place_coords.coord_id
AND (SQRT( POW(place_coords.Y, 2) + POW(place_coords.X, 2) ) <= 5)
AND registry.center_acronym = voting_center.center_acronym 
AND MONTH(registry.voting_date) = 11
GROUP BY voting_center.center_acronym
ORDER BY COUNT(*);


SELECT voting_center.center_acronym, place.addr_city, COUNT(*) as c
FROM voting_center INNER JOIN place INNER JOIN registry
WHERE voting_center.center_acronym = registry.center_acronym
AND MONTH(registry.voting_date) = 11 AND (1 <= DAY(registry.voting_date) <= 30)
AND place.addr_state = voting_center.addr_state AND place.addr_city = voting_center.addr_city AND 
place.addr_street_number = voting_center.addr_street_number AND place.addr_street_name = voting_center.addr_street_name
GROUP BY place.addr_city
ORDER BY c DESC;

SELECT folk.folk_id, voting_center.addr_state
FROM folk INNER JOIN registry ON folk.folk_id = registry.folk_id INNER JOIN voting_center ON voting_center.center_acronym = registry.center_acronym
WHERE registry.center_acronym = voting_center.center_acronym AND folk.folk_id = registry.folk_id AND voting_center.addr_state = 'Maryland'
GROUP BY folk.folk_id, registry.center_acronym
HAVING COUNT(*) = COUNT(DISTINCT voting_center.center_acronym);

WITH reg_tab AS (SELECT place_coords.X, place_coords.Y, voting_center.center_acronym, folk.folk_id
FROM voting_center INNER JOIN place_coords INNER JOIN place INNER JOIN registry INNER JOIN folk
WHERE place.coord_id = place_coords.coord_id
AND place.addr_state = voting_center.addr_state AND place.addr_city = voting_center.addr_city 
AND place.addr_state = voting_center.addr_state AND place.addr_street_number = voting_center.addr_street_number
AND registry.center_acronym = voting_center.center_acronym
AND registry.folk_id = folk.folk_id
ORDER BY voting_center.center_acronym),
res_tab AS (SELECT place_coords.X, place_coords.Y, folk.folk_id
FROM resides_at INNER JOIN place_coords INNER JOIN place INNER JOIN folk
WHERE place.coord_id = place_coords.coord_id
AND place.addr_state = resides_at.addr_state AND place.addr_city = resides_at.addr_city 
AND place.addr_state = resides_at.addr_state AND place.addr_street_number = resides_at.addr_street_number
AND resides_at.folk_id = folk.folk_id
GROUP BY folk.folk_id)
SELECT folk.folk_id, res_tab.X, res_tab.Y, reg_tab.X, reg_tab.Y
FROM folk, res_tab, reg_tab
WHERE res_tab.folk_id = reg_tab.folk_id
AND res_tab.folk_id = folk.folk_id
AND (SQRT( POW(reg_tab.Y-res_tab.Y, 2) + POW(reg_tab.X-res_tab.X, 2) ) > 0)
GROUP BY folk.folk_id;

WITH vc_tab AS (SELECT place_coords.X, place_coords.Y, voting_center.center_acronym
FROM voting_center INNER JOIN place_coords INNER JOIN place INNER JOIN folk
WHERE place.coord_id = place_coords.coord_id
AND place.addr_state = voting_center.addr_state AND place.addr_city = voting_center.addr_city 
AND place.addr_state = voting_center.addr_state AND place.addr_street_number = voting_center.addr_street_number
ORDER BY voting_center.center_acronym),
res_tab AS (SELECT place_coords.X, place_coords.Y, folk.folk_id
FROM resides_at INNER JOIN place_coords INNER JOIN place INNER JOIN folk
WHERE place.coord_id = place_coords.coord_id
AND place.addr_state = resides_at.addr_state AND place.addr_city = resides_at.addr_city 
AND place.addr_state = resides_at.addr_state AND place.addr_street_number = resides_at.addr_street_number
AND resides_at.folk_id = folk.folk_id
GROUP BY folk.folk_id)
SELECT vc_tab.center_acronym, folk.folk_id, (SQRT( POW(vc_tab.Y-res_tab.Y, 2) + POW(vc_tab.X-res_tab.X, 2) )) AS distance
FROM folk INNER JOIN vc_tab INNER JOIN res_tab INNER JOIN operating_period INNER JOIN voting_center
WHERE DATE(operating_period.date_start) <= '2022-11-01 08:00:00' <= DATE(operating_period.date_end)
AND folk.folk_id = res_tab.folk_id
AND voting_center.center_acronym = vc_tab.center_acronym
GROUP BY voting_center.center_acronym
ORDER BY distance ASC;

