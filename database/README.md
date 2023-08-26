# Database plan

This document will outline the relational database that will store the stats

Players (
    <u>PlayerID</u>, 
    Name
)

Teams (
    <u>TeamID</u>, 
    Name
)

Games (
    <u>GameID</u>,
    <span style="text-decoration:overline">HomeTeamID</span>,
    <span style="text-decoration:overline">AwayTeamID</span>,
    HomeScore,
    AwayScore
)

PlayerSelections (
    <u><span style="text-decoration:overline">PlayerID</span></u>,
    <u><span style="text-decoration:overline">TeamID</span></u>,
    <u><span style="text-decoration:overline">GameID</span></u>,
    Position
)

Event(
    <u>EventID</u>,
    <span style="text-decoration:overline">GameID</span>,
    <span style="text-decoration:overline">PlayerID</span>,
    Type,
    Outcome,
    Time
)