from flask import Flask, render_template, request
import database


app = Flask(__name__, static_folder='static')

# database.user_database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_users")
def add_users():
    add_name = request.args["add_name"]
    add = database.add_user(add_name)
    return f'Successfully Added: {add_name}'

@app.route("/add_jobs")
def add_jobs():
    nameJ = request.args["nameJ"]
    job_name = request.args["job_name"]
    if not database.check_user(nameJ):
        add_name = database.add_user(nameJ)
        user_id = database.user_id(nameJ)
        add_job = database.add_job(user_id, job_name)
        return f'Successfully Added: {nameJ}'
    user_id = database.user_id(nameJ)
    add_job = database.add_job(user_id, job_name)
    return f'Successfully Added: {job_name} & {nameJ}'

@app.route("/update_job")
def update_job():
    if request.args["job_id"] and request.args["status"]:
        job_id = request.args["job_id"]
        status = request.args["status"]
        database.update_jobID(job_id, status)
        return ""
    else:
        nameU = request.args["nameU"]
        job = request.args["job"]
        status = request.args["status"]
        user_id = database.user_id(nameU)
        print(user_id)
        update_job = database.update_job(user_id, job, status)
        return f'Successfully Updated {job} to {status}'

@app.route("/view_job")
def view_job():
    nameV = request.args["nameV"]
    user_id = database.user_id(nameV)
    view_job = database.view_job(user_id)
    return view_job

# @app.route("/view_users")
# def view_users():


@app.route("/remove_job")
def remove_job():
    
    if request.args["job_id"]:
        database.remove_jobID(request.args["job_id"])
        return f'{request.args["job_id"]} Has Been Removed'
    else:
        nameR = request.args["nameJ"]
        job_nameR = request.args["job_name"]
        user_id = database.user_id(nameR)
        database.remove_job(user_id, job_nameR)
        return f'{job_nameR} Has Been Removed'

@app.route("/get_user_names")
def get_user_names():
    names = database.get_user()
    return names
    
app.run(port=3000, host="0.0.0.0", debug=True)