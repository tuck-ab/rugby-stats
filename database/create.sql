create TABLE Players (
    PlayerID INT NOT NULL,
    Name TEXT NOT NULL,
    PRIMARY KEY (PlayerID)
);

create TABLE Teams (
    TeamID INT NOT NULL,
    Name TEXT NOT NULL,
    PRIMARY KEY (TeamID)
);

create TABLE Games (
    GameID INT NOT NULL,
    HomeTeamID INT NOT NULL,
    AwayTeamID INT NOT NULL,
    HomeScore INT NOT NULL,
    AwayScore INT NOT NULL,
    PRIMARY KEY (GameID),
    FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID)
);

create TABLE PlayerSelections (
    PlayerID INT NOT NULL,
    TeamID INT NOT NULL,
    GameID INT NOT NULL,
    Position INT NOT NULL,
    PRIMARY KEY (PlayerID, TeamID, GameID),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID)
);

create TABLE Event (
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