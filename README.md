# Rugby Data Web Scraper

An application that combines a webscraper to source rugby match data from
[StatBunker](https://rugby.statbunker.com/competitions/) and a relational
database to store the data.

Due to the database using typing from the scraper the whole directory acts as
a module that needs to be run. For this reason the entry point is in 
`__main__.py`. All the dependencies for this module are in `requirements.txt`

## Scraper information

In `__main__.py` the `run_wc(comp_id)` will collect all the data from a world
cup with a given competition ID and return it in a `Game` object. The class
definition can be found in `scraper/rugbyclasses.py`. This `Game` object is what
the database uses to add the data to the database. The following table shows 
the IDs for given World Cup years.

| World Cup Year | Competition ID |
| -------------- | -------------- |
| 2023           | 727            |
| 2019           | 606            |
| 2015           | 449            |
| 2011           | 356            |
| 2007           | 239            |
| 2003           | 84             |

## Database Schema

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
    Date,
    HomeScore,
    AwayScore
)

PlayerSelections (
    <u><span style="text-decoration:overline">PlayerID</span></u>,
    <u><span style="text-decoration:overline">TeamID</span></u>,
    <u><span style="text-decoration:overline">GameID</span></u>,
    Position
)

Events(
    <u>EventID</u>,
    <span style="text-decoration:overline">GameID</span>,
    <span style="text-decoration:overline">PlayerID</span>,
    Type,
    Outcome,
    Time
)

The SQL for setting up the database can be found in `database/create.sql` and
code exists to set up a database file `database/data.db` in 
`database/database_setup.py`
