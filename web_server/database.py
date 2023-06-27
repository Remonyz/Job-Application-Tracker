import sqlite3

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




def add_user(user):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO user(username) VALUES ('{user}')")
    conn.commit()

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

def view_job(user):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # c.execute(f"SELECT * FROM jobs WHERE user_jobs = '{user}'")
    
    c.execute(f"SELECT job_name, ifnull(job_status, 'Pending') AS job_status FROM jobs WHERE user_jobs = '{user}'")
    jobs = c.fetchall()
    # for user in jobs:
    #     print(str(user[1]) + " " + str(user[2]))
    return jobs

def remove_job(user, job):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # print(f"DELETE FROM jobs WHERE user_jobs = '{user}' AND job_name = '{job}'")
    c.execute(f"DELETE FROM jobs WHERE user_jobs = '{user}' AND job_name = '{job}'")
    conn.commit()
