import random

# open the crime file
# create a list of all crime points
coordinates = []
coordinates_2018 = []
coordinates_2019 = []
coordinates_2020 = []
coordinates_2021 = []
coordinates_2022 = []

common_assault = []
larceny = []
agg_assault = []
robbery = []
auto_theft = []
robbery_carjacking = []
burglary = []
larceny_from_auto = []
rape = []
shooting = []
homicide = []
robbery_commercial = []
arson = []

filenames = ["coordinates", "coordinates_2018", "coordinates_2019", "coordinates_2020", "coordinates_2021", "coordinates_2022",
             "common_assault", "larceny", "agg_assault", "robbery", "auto_theft", "robbery_carjacking", "burglary",
             "larceny_from_auto", "rape", "shooting", "homicide", "robbery_commercial", "arson"]

with open("venv/Part_1_Crime_Data_.csv", "r") as f:
    i = 0
    for line in f:
        if i != 0:
            coords = line.split(",")
            x1 = coords[0]
            y1 = coords[1]
            point = [x1, y1]
            if x1 and y1:
                coordinates.append(point)
                if "2018" in coords[3]:
                    coordinates_2018.append(point)
                if "2019" in coords[3]:
                    coordinates_2019.append(point)
                if "2020" in coords[3]:
                    coordinates_2020.append(point)
                if "2021" in coords[3]:
                    coordinates_2021.append(point)
                if "2022" in coords[3]:
                    coordinates_2022.append(point)

                if "COMMON ASSAULT" in coords[6]:
                    common_assault.append(point)
                if "LARCENY" in coords[6]:
                    larceny.append(point)
                if "AGG. ASSAULT" in coords[6]:
                    agg_assault.append(point)
                if "ROBBERY" in coords[6]:
                    robbery.append(point)
                if "AUTO THEFT" in coords[6]:
                    auto_theft.append(point)
                if "ROBBERY - CARJACKING" in coords[6]:
                    robbery_carjacking.append(point)
                if "BURGLARY" in coords[6]:
                    burglary.append(point)
                if "LARCENY FROM AUTO" in coords[6]:
                    larceny_from_auto.append(point)
                if "RAPE" in coords[6]:
                    rape.append(point)
                if "SHOOTING" in coords[6]:
                    shooting.append(point)
                if "HOMICIDE" in coords[6]:
                    homicide.append(point)
                if "ROBBERY - COMMERCIAL" in coords[6]:
                    robbery_commercial.append(point)
                if "ARSON" in coords[6]:
                    arson.append(point)
        i = i + 1

for filename in filenames:
    # open a JavaScript file to store coordinates in lat,long
    # change the path to suit your setup
    f2 = open("venv/{}.js".format(filename), "w")
    # create a variable
    f2.write('var {} = ['.format(filename))

    count = 1

    # write data to js file
    for coord in globals()[filename]:
        print(coord)
        if count == 1:
            f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

            count = count + 1

        else:
            f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

            count = count + 1

    # closing bracket
    f2.write(']')
    # close file
    f2.close()

"""
# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/crime_points.js", "w")
# create a variable
f2.write('var crime_points = [')

count = 1

# write data to js file
for coord in coordinates:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/crime_points_2018.js", "w")
# create a variable
f2.write('var crime_points_2018 = [')

count = 1

# write data to js file
for coord in coordinates_2018:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/crime_points_2019.js", "w")
# create a variable
f2.write('var crime_points_2019 = [')

count = 1

# write data to js file
for coord in coordinates_2019:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/crime_points_2020.js", "w")
# create a variable
f2.write('var crime_points_2020 = [')

count = 1

# write data to js file
for coord in coordinates_2020:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/crime_points_2021.js", "w")
# create a variable
f2.write('var crime_points_2021 = [')

count = 1

# write data to js file
for coord in coordinates_2021:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/crime_points_2022.js", "w")
# create a variable
f2.write('var crime_points_2022 = [')

count = 1

# write data to js file
for coord in coordinates_2022:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/common_assault.js", "w")
# create a variable
f2.write('var common_assault = [')

count = 1

# write data to js file
for coord in common_assault:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/larceny.js", "w")
# create a variable
f2.write('var larceny = [')

count = 1

# write data to js file
for coord in larceny:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/agg_assault.js", "w")
# create a variable
f2.write('var agg_assault = [')

count = 1

# write data to js file
for coord in agg_assault:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/arson.js", "w")
# create a variable
f2.write('var arson = [')

count = 1

# write data to js file
for coord in arson:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/auto_theft.js", "w")
# create a variable
f2.write('var auto_theft = [')

count = 1

# write data to js file
for coord in auto_theft:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/burglary.js", "w")
# create a variable
f2.write('var burglary = [')

count = 1

# write data to js file
for coord in burglary:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/homicide.js", "w")
# create a variable
f2.write('var homicide = [')

count = 1

# write data to js file
for coord in homicide:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()

# open a JavaScript file to store coordinates in lat,long
# change the path to suit your setup
f2 = open("venv/larceny_from_auto.js", "w")
# create a variable
f2.write('var larceny_from_auto = [')

count = 1

# write data to js file
for coord in larceny_from_auto:
    if count == 1:
        f2.write('[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

    else:
        f2.write(',[' + str(coord[1]) + ',' + str(coord[0]) + ']')

        count = count + 1

# closing bracket
f2.write(']')
# close file
f2.close()
"""