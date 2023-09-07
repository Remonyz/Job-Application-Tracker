from flask import Flask, render_template, request
import database

app = Flask(__name__, static_folder='static')

# database.user_database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_users", methods=["POST"])
def add_users():
    add_name = request.args.get("add_name")
    if add_name:
        add = database.add_user(add_name)
        return f'Successfully Added: {add_name}'
    else:
        return "Missing 'add_name' query parameter"

@app.route("/add_jobs", methods=["POST"])
def add_jobs():
    nameJ = request.args.get("nameJ")
    job_name = request.args.get("job_name")
    if nameJ and job_name:
        user_id = database.user_id(nameJ)
        add_job = database.add_job(user_id, job_name)
        return f'Successfully Added: {job_name}'
    else:
        return "Missing 'nameJ' or 'job_name' query parameter"

@app.route("/update_job", methods=["POST"])
def update_job():
    nameU = request.args.get("nameU")
    job = request.args.get("job")
    status = request.args.get("status")
    if nameU and job and status:
        user_id = database.user_id(nameU)
        print(user_id)
        update_job = database.update_job(user_id, job, status)
        return f'Successfully Updated {job} to {status}'
    else:
        return "Missing 'nameU', 'job', or 'status' query parameter"

@app.route("/view_job", methods=["POST"])
def view_job():
    nameV = request.args.get("nameV")
    if nameV:
        user_id = database.user_id(nameV)
        view_job = database.view_job(user_id)
        return view_job
    else:
        return "Missing 'nameV' query parameter"

@app.route("/remove_job", methods=["POST"])
def remove_job():
    nameR = request.args.get("nameJ")
    job_nameR = request.args.get("job_name")
    if nameR and job_nameR:
        user_id = database.user_id(nameR)
        database.remove_job(user_id, job_nameR)
        return f'{job_nameR} Has Been Removed'
    else:
        return "Missing 'nameJ' or 'job_name' query parameter"

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0", debug=True)
