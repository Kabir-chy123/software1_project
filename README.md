

🗄️ Database System

Flight AURORA uses two forms of data storage.

Airport Dataset

Airport information is stored in:

airports.csv

This dataset contains airport information used to generate random destinations.

Example fields:

Field	Description
ident	Airport identifier
name	Airport name
iso_country	Country code
type	Airport category

The game loads airport data automatically when the program starts.

Hall of Fame Database

Completed game runs are stored in a local SQLite database:

hall_of_fame.db

This database is automatically created when the game runs for the first time.

Table structure
CREATE TABLE hall_of_fame (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    ending TEXT NOT NULL,
    survivors INTEGER NOT NULL,
    fuel INTEGER NOT NULL,
    played_at TEXT NOT NULL
);

Each entry records:

Player name

Ending achieved

Survivors rescued

Remaining fuel

Timestamp of the run

Players can view previous runs through the Hall of Fame menu in the game.

⚙️ Requirements

Python 3.8 or newer

No external libraries required

SQLite (included with Python)

▶️ Running the Game

Clone the repository:

git clone https://github.com/yourusername/flight-aurora.git
cd flight-aurora

Run the game:

python game.py
📁 Project Structure
flight-aurora/
│
├── game.py
├── world.py
├── database.py
├── dialogue.py
├── endings.py
├── hud.py
├── weather.py
├── clue_bank.py
│
├── airports.csv
├── hall_of_fame.db
│
└── README.md
🧠 Design Goals

Flight AURORA aims to:

Combine interactive storytelling with gameplay

Create tension through resource management

Encourage replayability

Deliver a cinematic experience within a terminal environment

🚀 Future Improvements

Possible future additions:

Save and resume game feature
Sound effects
ASCII storm animations
Expanded story branches
Additional airports
Online leaderboard

🌠 Final Transmission

“Through storm and silence, you proved humanity can still fly.”

Good luck, Pilot.
