Game Story – Flight AURORA

You are the last pilot in the sky.

When the world began to fade, it didn’t end with explosions or fire. Airports vanished from radar. Cities blinked out like dying stars. Pilots reported strange lights before their signals dissolved into static. One by one, every aircraft disappeared—every aircraft except yours. Now, you fly alone.

Your only companion is NOVA, an advanced AI navigator built for long-haul survival missions. Calm, precise, almost human, NOVA monitors your fuel levels, calculates unstable routes, and warns you of storms forming beyond the horizon. Somewhere in the chaos, one signal still burns bright: the Aurora Beacon. It may be the last hope for humanity or the source of everything that went wrong.

You begin at the last confirmed safe airport. As your engines idle on the cracked runway, your cockpit display flickers to life: Fuel: X units. Chances: X. Survivors: 0. Mission: Reach the Aurora Beacon. There is no money anymore, no control towers guiding your only fuel, limited chances, and the endless sky. Every decision matters.

Before takeoff, you choose who you are. An Engineer who conserves precious fuel. A Navigator who reduces crash risk in violent storms. Or a Leader who rescues more survivors along the way. Your role shapes your survival, but the sky remains unpredictable.

As you cross into new zones, reality begins to distort. The first skies feel unstable but manageable. Then come interference fields where airports flicker on your map. In the Twilight regions, phantom runways may trap or destroy you. In the Crisis zone, brutal storms and desperate distress calls test your resolve. And beyond it all lies the Aurora zone, where lightning surrounds your aircraft and the atmosphere itself seems alive.

Each flight consumes fuel. Weather increases crash risk. Random events may save you—or push you closer to disaster. A tailwind might grant relief. Turbulence could drain your reserves. A distress signal might reward you with supplies—or cost you one of your last chances. Some airports are safe. Some are illusions. Some are endings.

Through every storm, NOVA guides you. “Fuel levels critical.” “Severe turbulence ahead.” “The Aurora signal is increasing in strength.” As fuel runs low and chances disappear, the survivors you carry look to you for hope. The final storm gathers at the edge of the world, and beyond it, the Beacon shines.

You can push forward into the unknown… or turn away and carve your own path into the fading sky.

Flight AURORA is not about wealth or glory. It is about survival, trust, and the courage to keep flying when the sky itself is breaking. And beyond the final storm, the Aurora waits.

🗄️ Database System

Flight AURORA uses two forms of data storage.

Airport Dataset

Airport information is stored in:

airports.csv

This dataset contains airport information used to generate random destinations.

Example fields:

Field		|	Description
ident		|   Airport identifier
name		|	Airport name
iso_country	|	Country code
type		|	Airport category

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
