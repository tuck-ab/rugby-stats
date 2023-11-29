CREATE TABLE Players (
    PlayerID INT NOT NULL,
    Name TEXT NOT NULL,
    PRIMARY KEY (PlayerID)
);

INSERT INTO Players VALUES (0, 'Null Player');

CREATE TABLE Teams (
    TeamID INT NOT NULL,
    Name TEXT NOT NULL,
    PRIMARY KEY (TeamID)
);

INSERT INTO Teams VALUES (0, 'Null Team');

CREATE TABLE Games (
    GameID INT NOT NULL,
    HomeTeamID INT NOT NULL,
    AwayTeamID INT NOT NULL,
    Date TEXT NOT NULL,
    HomeScore INT NOT NULL,
    AwayScore INT NOT NULL,
    PRIMARY KEY (GameID),
    FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID)
);

INSERT INTO Games VALUES (0, 0, 0, "20-Nov-2000", 0, 0);

CREATE TABLE PlayerSelections (
    PlayerID INT NOT NULL,
    TeamID INT NOT NULL,
    GameID INT NOT NULL,
    Position INT NOT NULL,
    PRIMARY KEY (PlayerID, TeamID, GameID),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID)
);

INSERT INTO PlayerSelections VALUES (0, 0, 0, 15);

CREATE TABLE Events (
    EventID INT NOT NULL,
    GameID INT NOT NULL,
    PlayerID INT NOT NULL,
    Type TEXT NOT NULL,
    Outcome TEXT,
    Time INT,
    PRIMARY KEY (EventID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);

INSERT INTO Events VALUES (0, 0, 0, 'Null Event', NULL, 0);