import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "pregnancy_tracker.db")


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, dose TEXT, time TEXT, taken INTEGER DEFAULT 0
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS tests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, date TEXT, result TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, doctor TEXT, notes TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, weight TEXT, kicks TEXT, symptoms TEXT
    )""")
    conn.commit()
    conn.close()


# Medicines
def add_medicine(name, dose, time_str):
    conn = get_conn(); c = conn.cursor()
    c.execute("INSERT INTO medicines (name, dose, time, taken) VALUES (?, ?, ?, 0)", (name, dose, time_str))
    conn.commit(); conn.close()


def get_medicines():
    conn = get_conn(); c = conn.cursor()
    c.execute("SELECT * FROM medicines ORDER BY time")
    rows = c.fetchall(); conn.close()
    return rows


def mark_medicine_taken(mid):
    conn = get_conn(); c = conn.cursor()
    c.execute("UPDATE medicines SET taken=1 WHERE id=?", (mid,))
    conn.commit(); conn.close()


def delete_medicine(mid):
    conn = get_conn(); c = conn.cursor()
    c.execute("DELETE FROM medicines WHERE id=?", (mid,))
    conn.commit(); conn.close()


# Tests
def add_test(name, date, result):
    conn = get_conn(); c = conn.cursor()
    c.execute("INSERT INTO tests (name, date, result) VALUES (?, ?, ?)", (name, date, result))
    conn.commit(); conn.close()


def get_tests():
    conn = get_conn(); c = conn.cursor()
    c.execute("SELECT * FROM tests ORDER BY date")
    rows = c.fetchall(); conn.close()
    return rows


def delete_test(tid):
    conn = get_conn(); c = conn.cursor()
    c.execute("DELETE FROM tests WHERE id=?", (tid,))
    conn.commit(); conn.close()


# Appointments
def add_appointment(date, doctor, notes):
    conn = get_conn(); c = conn.cursor()
    c.execute("INSERT INTO appointments (date, doctor, notes) VALUES (?, ?, ?)", (date, doctor, notes))
    conn.commit(); conn.close()


def get_appointments():
    conn = get_conn(); c = conn.cursor()
    c.execute("SELECT * FROM appointments ORDER BY date")
    rows = c.fetchall(); conn.close()
    return rows


def delete_appointment(aid):
    conn = get_conn(); c = conn.cursor()
    c.execute("DELETE FROM appointments WHERE id=?", (aid,))
    conn.commit(); conn.close()


# Logs (weight / kicks / symptoms)
def add_log(date, weight, kicks, symptoms):
    conn = get_conn(); c = conn.cursor()
    c.execute("INSERT INTO logs (date, weight, kicks, symptoms) VALUES (?, ?, ?, ?)", (date, weight, kicks, symptoms))
    conn.commit(); conn.close()


def get_logs():
    conn = get_conn(); c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY date")
    rows = c.fetchall(); conn.close()
    return rows


def delete_log(lid):
    conn = get_conn(); c = conn.cursor()
    c.execute("DELETE FROM logs WHERE id=?", (lid,))
    conn.commit(); conn.close()
