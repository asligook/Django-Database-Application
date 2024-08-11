CREATE TABLE DatabaseManagers (
	username VARCHAR(125),
    password VARCHAR(250),
	PRIMARY KEY (username)
);

CREATE TABLE Users ( 
	username VARCHAR(125),
	password VARCHAR(125),
	name VARCHAR(125),
	surname VARCHAR(125),
	PRIMARY KEY (username)
);

CREATE TABLE Players (
	username VARCHAR(125),
	date_of_birth VARCHAR(125),
	height INTEGER,
	weight INTEGER,
	PRIMARY KEY (username),
	FOREIGN KEY (username) REFERENCES Users(username)
	ON DELETE CASCADE
);
CREATE TABLE Positions (
	position_id INTEGER,
	position_name VARCHAR(120) ,
	PRIMARY KEY (position_id)
);

CREATE TABLE Have_Positions(
	player_position_id INTEGER,
	username VARCHAR(125),
	position_id INTEGER NOT NULL ,
	PRIMARY KEY (player_position_id),
	FOREIGN KEY (username) REFERENCES Players(username),
	FOREIGN KEY (position_id) REFERENCES Positions(position_id)
);

CREATE TABLE Coaches (
	username VARCHAR(125),
	nationality VARCHAR(125) NOT NULL ,
	PRIMARY KEY (username),
	FOREIGN KEY (username) REFERENCES Users(username) 
	ON DELETE CASCADE
);

CREATE TABLE Channels (
	channel_id INTEGER,
	channel_name  VARCHAR(150) UNIQUE,
	PRIMARY KEY (channel_id)
);

CREATE TABLE Teams (
	team_id INTEGER,
	team_name VARCHAR(150) ,
	channel_id INTEGER NOT NULL,
	PRIMARY KEY (team_id),
	FOREIGN KEY (channel_id) REFERENCES Channels(channel_id)
);
CREATE TABLE Player_Registered_Team (
	player_teams_id INTEGER,
	username VARCHAR(125),
	team_id INTEGER NOT NULL,
	PRIMARY KEY (player_teams_id),
	FOREIGN KEY (username) REFERENCES Players(username),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id)
);

CREATE TABLE Leads (
	lead_id INTEGER,
	coach_username VARCHAR(150),
	contract_start_time VARCHAR(125),
	contract_end_time VARCHAR(125),
	team_id INTEGER NOT NULL,
	PRIMARY KEY (lead_id),
	FOREIGN KEY (coach_username) REFERENCES Coaches(username),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id),
	CHECK (STR_TO_DATE(contract_end_time, '%d-%m-%Y') > STR_TO_DATE(contract_start_time, '%d-%m-%Y'))
);


CREATE TABLE Juries (
	username VARCHAR(125),
	nationality VARCHAR(125) NOT NULL ,
	PRIMARY KEY (username),
	FOREIGN KEY (username) REFERENCES Users(username) 
	ON DELETE CASCADE
);
CREATE TABLE Stadiums (
	stadium_id INTEGER,
	stadium_name VARCHAR(150),
	stadium_country VARCHAR(150),
	PRIMARY KEY (stadium_id)
);

CREATE TABLE Match_Event(
	session_id INTEGER,
	team_id INTEGER NOT NULL,
	assigned_jury_username VARCHAR(125) NOT NULL, 
	date VARCHAR(125),
	rating FLOAT,
	time_slot INTEGER,
	stadium_id INTEGER NOT NULL,
	PRIMARY KEY (session_id),
	FOREIGN KEY (assigned_jury_username) REFERENCES Juries(username),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id),
	FOREIGN KEY (stadium_id) REFERENCES Stadiums(stadium_id),
	CHECK (time_slot >= 1 AND time_slot  <= 3)
);


CREATE TABLE Match_PlayedBy_Team (
	session_id INTEGER,
	team_id INTEGER,
	PRIMARY KEY (session_id),
	FOREIGN KEY (session_id) REFERENCES Match_Event(session_id),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id)
);

CREATE TABLE Players_PlayIn_Matches ( 
	squad_id INTEGER,
	username VARCHAR(125),
	session_id INTEGER,
	position_id INTEGER,
	PRIMARY KEY (squad_id),
	FOREIGN KEY (username) REFERENCES Players(username),
	FOREIGN KEY (session_id) REFERENCES Match_Event(session_id),
	FOREIGN KEY (position_id) REFERENCES Positions(position_id)
);


