import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "mess2meal.db"


@contextmanager
def get_connection():
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 10000")
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    """Create tables and apply small, backwards-compatible SQLite migrations."""
    with get_connection() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity_kg REAL NOT NULL,
            prepared_at TEXT NOT NULL,
            best_before TEXT NOT NULL,
            storage_condition TEXT NOT NULL,
            pickup_location TEXT NOT NULL,
            notes TEXT DEFAULT '',
            status TEXT NOT NULL DEFAULT 'available',
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS recipients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            recipient_type TEXT NOT NULL,
            contact_person TEXT NOT NULL,
            contact_phone TEXT NOT NULL,
            location TEXT NOT NULL,
            preferred_categories TEXT NOT NULL,
            capacity_kg REAL NOT NULL,
            urgency INTEGER NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1
        );
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_id INTEGER NOT NULL,
            recipient_id INTEGER NOT NULL,
            score REAL NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(food_id) REFERENCES food(id),
            FOREIGN KEY(recipient_id) REFERENCES recipients(id)
        );
        CREATE TABLE IF NOT EXISTS status_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_id INTEGER NOT NULL,
            old_status TEXT,
            new_status TEXT NOT NULL,
            changed_at TEXT NOT NULL,
            note TEXT DEFAULT '',
            FOREIGN KEY(food_id) REFERENCES food(id) ON DELETE CASCADE
        );
        """)
        columns = {row["name"] for row in conn.execute("PRAGMA table_info(recipients)")}
        if "distance_km" not in columns:
            conn.execute("ALTER TABLE recipients ADD COLUMN distance_km REAL NOT NULL DEFAULT 0")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_food_status ON food(status)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_recipient_active ON recipients(is_active)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_status_history_food ON status_history(food_id, id)")
