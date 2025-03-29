CREATE TABLE folk (
    folk_id VARCHAR(16) NOT NULL,
    dob DATE NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    nickname VARCHAR(40) NOT NULL,
    PRIMARY KEY(folk_id),
    UNIQUE(folk_id)
);

CREATE TABLE folk_emailAddrs(
    email VARCHAR(40) NOT NULL,
    folk_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(email),
    FOREIGN KEY(folk_id) REFERENCES folk(folk_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE(email)
);

CREATE TABLE folk_phoneNums(
    work VARCHAR(10),
    mobile VARCHAR(10) NOT NULL,
    home VARCHAR(10),
    folk_id VARCHAR(16) NOT NULL,
    FOREIGN KEY(folk_id) REFERENCES folk(folk_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE(work, mobile, home, folk_id)
);

CREATE TABLE elections_staff(
    employee_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(employee_id),
    FOREIGN KEY(employee_id) REFERENCES folk(folk_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    UNIQUE(employee_id)
);

CREATE TABLE staff_schedule(
    staff_id VARCHAR(16) NOT NULL,
    date_start DATETIME NOT NULL,
    date_end DATETIME NOT NULL,
    PRIMARY KEY(staff_id),
    FOREIGN KEY(staff_id) REFERENCES elections_staff(employee_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    UNIQUE(staff_id)
);

CREATE TABLE staff_administrator(
    admin_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(admin_id),
    FOREIGN KEY(admin_id) REFERENCES elections_staff(employee_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    UNIQUE(admin_id)
);

CREATE TABLE staff_clerk(
    clerk_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(clerk_id),
    FOREIGN KEY(clerk_id) REFERENCES elections_staff(employee_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    UNIQUE(clerk_id)
);

CREATE TABLE staff_judge(
    judge_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(judge_id),
    FOREIGN KEY(judge_id) REFERENCES elections_staff(employee_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    UNIQUE(judge_id)
);

CREATE TABLE staff_monitor(
    monitor_id VARCHAR(16) NOT NULL,
    PRIMARY KEY(monitor_id),
    FOREIGN KEY(monitor_id) REFERENCES elections_staff(employee_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    UNIQUE(monitor_id)
);



CREATE TABLE place(
    addr_state VARCHAR(20) NOT NULL,
    addr_city VARCHAR(30) NOT NULL,
    addr_street_number VARCHAR(30) NOT NULL,
    addr_street_name VARCHAR(30) NOT NULL,
    coord_id VARCHAR(3) NOT NULL,
    PRIMARY KEY(addr_state, addr_city, addr_street_number, addr_street_name),
    UNIQUE(coord_id)
);

CREATE TABLE place_coords(
    coord_id VARCHAR(3) NOT NULL,
    X VARCHAR(3) NOT NULL,
    Y VARCHAR(3) NOT NULL,
    PRIMARY KEY(coord_id),
    FOREIGN KEY(coord_id) REFERENCES place(coord_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE(coord_id)
);

CREATE TABLE residence(
    addr_state VARCHAR(20) NOT NULL,
    addr_city VARCHAR(30) NOT NULL,
    addr_street_number VARCHAR(30) NOT NULL,
    addr_street_name VARCHAR(30) NOT NULL,
    PRIMARY KEY(addr_state, addr_city, addr_street_number, addr_street_name),
    FOREIGN KEY(addr_state, addr_city, addr_street_number, addr_street_name) 
        REFERENCES place(addr_state, addr_city, addr_street_number, addr_street_name)
        ON DELETE CASCADE  
        ON UPDATE CASCADE
);

CREATE TABLE voting_center(
    addr_state VARCHAR(20) NOT NULL,
    addr_city VARCHAR(30) NOT NULL,
    addr_street_number VARCHAR(30) NOT NULL,
    addr_street_name VARCHAR(30) NOT NULL,
    center_acronym VARCHAR(4) NOT NULL,
    PRIMARY KEY(addr_state, addr_city, addr_street_number, addr_street_name),
    FOREIGN KEY(addr_state, addr_city, addr_street_number, addr_street_name) 
        REFERENCES place(addr_state, addr_city, addr_street_number, addr_street_name)
        ON DELETE CASCADE  
        ON UPDATE CASCADE,
    UNIQUE(center_acronym)
);

CREATE TABLE works_at(
    staff_id VARCHAR(16) NOT NULL,
    center_acronym VARCHAR(4) NOT NULL,
    FOREIGN KEY(staff_id) REFERENCES elections_staff(employee_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(center_acronym) REFERENCES voting_center(center_acronym) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE operating_period(
    date_start DATETIME NOT NULL,
    date_end DATETIME NOT NULL,
    cntr_acronym VARCHAR(4) NOT NULL,
    FOREIGN KEY(cntr_acronym) REFERENCES voting_center(center_acronym)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE ballots(
    ballot_name VARCHAR(4) NOT NULL,
    date_start DATETIME NOT NULL,
    date_end DATETIME NOT NULL,
    PRIMARY KEY(ballot_name),
    UNIQUE(ballot_name)
);

CREATE TABLE ballot_questions(
    question_num VARCHAR(2) NOT NULL,
    ballot_name VARCHAR(4) NOT NULL,
    question_text VARCHAR(200) NOT NULL,
    PRIMARY KEY(ballot_name, question_num),
    FOREIGN KEY(ballot_name) REFERENCES ballots(ballot_name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE stores(
    ballot_name VARCHAR(4) NOT NULL,
    center_acronym VARCHAR(4) NOT NULL,
    FOREIGN KEY(center_acronym) REFERENCES voting_center(center_acronym)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(ballot_name) REFERENCES ballots(ballot_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE(ballot_name, center_acronym)
);

CREATE TABLE registry(
    ballot_name VARCHAR(4) NOT NULL,
    center_acronym VARCHAR(4) NOT NULL,
    folk_id VARCHAR(16) NOT NULL,
    voting_date DATE NOT NULL,
    PRIMARY KEY(ballot_name, center_acronym, folk_id),
    FOREIGN KEY(folk_id) REFERENCES folk(folk_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    FOREIGN KEY(center_acronym) REFERENCES voting_center(center_acronym)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(ballot_name) REFERENCES ballots(ballot_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE casted_vote(
    ballot_name VARCHAR(4) NOT NULL,
    center_acronym VARCHAR(4) NOT NULL,
    folk_id VARCHAR(16) NOT NULL,
    monitor_id VARCHAR(16) NOT NULL,
    cast_date DATE NOT NULL,
    FOREIGN KEY(folk_id) REFERENCES folk(folk_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    FOREIGN KEY(monitor_id) REFERENCES staff_monitor(monitor_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    FOREIGN KEY(center_acronym) REFERENCES voting_center(center_acronym)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(ballot_name) REFERENCES ballots(ballot_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE ballot_answers(
    folk_id VARCHAR(16) NOT NULL,
    ballot_name VARCHAR(4) NOT NULL,
    question_num VARCHAR(2) NOT NULL,
    response VARCHAR(7),
    FOREIGN KEY(folk_id) REFERENCES folk(folk_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    FOREIGN KEY(ballot_name) REFERENCES ballots(ballot_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE resides_at(
    folk_id VARCHAR(16),
    addr_state VARCHAR(20) NOT NULL,
    addr_city VARCHAR(30) NOT NULL,
    addr_street_number VARCHAR(30) NOT NULL,
    addr_street_name VARCHAR(30) NOT NULL,
    FOREIGN KEY (folk_id) REFERENCES folk(folk_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(addr_state, addr_city, addr_street_number, addr_street_name) 
        REFERENCES place(addr_state, addr_city, addr_street_number, addr_street_name)
        ON DELETE CASCADE  
        ON UPDATE CASCADE
);

