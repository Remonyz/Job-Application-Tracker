import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
table_exists = c.fetchone()
if not table_exists:
    c.execute("""CREATE TABLE user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        UNIQUE(username)
    )""")

    c.execute("""CREATE TABLE jobs(
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_name TEXT,
        job_status TEXT,
        user_jobs INTEGER NOT NULL, 
        FOREIGN KEY (user_jobs) REFERENCES user (user_id)
    )""")

conn.commit()
conn.close()


def user_database():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # c.execute("DROP TABLE user")
    # c.execute("DROP TABLE jobs")

    c.execute("""CREATE TABLE user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        UNIQUE(username)
    )""")

    c.execute("""CREATE TABLE jobs(
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_name TEXT,
        job_status TEXT,
        user_jobs INTEGER NOT NULL, 
        FOREIGN KEY (user_jobs) REFERENCES user (user_id)
    )""")


def check_user(user):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(f"SELECT COUNT(*) FROM user WHERE username = '{user}'")
    count = c.fetchone()[0]
    return count > 0 #return count if count if bigger than 0

def add_user(user):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO user(username) VALUES ('{user}')")
    conn.commit()

    # c.execute("SELECT username FROM user") #update the user dropdown after a user is added
    # names = c.fetchall()
    # conn.close()
    # return names

# add_job helper function to retrieve user_id
def user_id(user):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(f"SELECT user_id FROM user WHERE username = '{user}'")
    result = c.fetchall()
    return (str(result[0]))

def add_job(user_id, job):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # just insert normally the user id and job name
    c.execute(f"INSERT INTO jobs(job_name, user_jobs, job_status) VALUES ('{job}', '{user_id}', 'Pending')")    
    conn.commit()

def update_job(user_id, job, status):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # c.execute(f"REPLACE INTO jobs(job_status) VALUES ('{status}') WHERE job_name = '{job}' AND user_job = '{user_id}'")
    # print(f"UPDATE jobs SET job_status = '{status}' WHERE job_name = '{job}' AND user_jobs = '{user_id}'")
    c.execute(f"UPDATE jobs SET job_status = '{status}' WHERE job_name = '{job}' AND user_jobs = '{user_id}'")
    conn.commit()

def update_jobID(job_id, status):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(f"UPDATE jobs SET job_status = '{status}' WHERE job_id = '{job_id}'")
    conn.commit()

def view_job(user):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # c.execute(f"SELECT * FROM jobs WHERE user_jobs = '{user}'")
    
    c.execute(f"SELECT job_id, job_name, ifnull(job_status, 'Pending') AS job_status FROM jobs WHERE user_jobs = '{user}'")
    jobs = c.fetchall()
    
    return jobs

def remove_job(user, job):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # print(f"DELETE FROM jobs WHERE user_jobs = '{user}' AND job_name = '{job}'")
    c.execute(f"DELETE FROM jobs WHERE user_jobs = '{user}' AND job_name = '{job}'")
    conn.commit()

def remove_jobID(job_id):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(f"DELETE FROM jobs WHERE job_id = '{job_id}'")
    conn.commit()

def get_user():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user") #dropdown containing the usernames in db
    names = c.fetchall()

    return names