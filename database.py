from __future__ import annotations

import csv
import os
import random
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AIRPORTS_CSV_PATH = os.path.join(BASE_DIR, "airports.csv")

_AIRPORT_CACHE: Optional[List[Dict]] = None


def _load_airports_from_csv() -> List[Dict]:
    global _AIRPORT_CACHE
    if _AIRPORT_CACHE is not None:
        return _AIRPORT_CACHE

    if not os.path.exists(AIRPORTS_CSV_PATH):
        raise FileNotFoundError(
            f"Could not find airports.csv at: {AIRPORTS_CSV_PATH}\n"
            "Make sure airports.csv is in the same folder as database.py."
        )

    airports: List[Dict] = []
    with open(AIRPORTS_CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            airports.append(
                {
                    "ident": row.get("ident", "").strip(),
                    "name": row.get("name", "").strip(),
                    "iso_country": row.get("iso_country", "").strip(),
                    "type": row.get("type", "").strip(),
                }
            )
    _AIRPORT_CACHE = [a for a in airports if a["ident"] and a["name"]]
    return _AIRPORT_CACHE


def fetch_airports(limit: int = 5, airport_type: str = "all") -> List[Dict]:
    airports = _load_airports_from_csv()

    if airport_type != "all":
        airports = [a for a in airports if a["type"] == airport_type]

    if not airports:
        return []

    # random.sample needs limit <= len(list)
    limit = max(0, min(limit, len(airports)))
    return random.sample(airports, limit)

phantom_airports = [
    {"id": "X-LOOP", "name": "Cyclone Airfield", "effect": "loop", "zone": "Twilight"},
    {"id": "X-DEC", "name": "Drowned Terminal", "effect": "stranded", "zone": "Twilight"},
    {"id": "X-HAUNT", "name": "Collapsed Runway", "effect": "crash", "zone": "Twilight"},
]

aurora_airport = {
    "id": "X-AURORA",
    "name": "Aurora Beacon",
    "effect": "win",
    "zone": "Aurora Frontier",
}

HOF_DB_PATH = os.path.join(BASE_DIR, "hall_of_fame.db")

def _get_conn() -> sqlite3.Connection:
    return sqlite3.connect(HOF_DB_PATH)


def _init_hof_table() -> None:
    conn = _get_conn()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS hall_of_fame (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                ending TEXT NOT NULL,
                survivors INTEGER NOT NULL,
                fuel INTEGER NOT NULL,
                played_at TEXT NOT NULL
            );
            """
        )
        conn.commit()
    finally:
        conn.close()


def save_run(player_name: str, ending: str, survivors: int, fuel: int) -> None:
    _init_hof_table()
    conn = _get_conn()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO hall_of_fame (player_name, ending, survivors, fuel, played_at)
            VALUES (?, ?, ?, ?, ?);
            """,
            (player_name, ending, int(survivors), int(fuel), datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()
    finally:
        conn.close()


def fetch_runs(limit: int = 5) -> List[Dict]:
    _init_hof_table()
    conn = _get_conn()
    conn.row_factory = sqlite3.Row
    try:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT player_name, ending, survivors, fuel, played_at
            FROM hall_of_fame
            ORDER BY played_at DESC
            LIMIT ?;
            """,
            (int(limit),),
        )
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()
