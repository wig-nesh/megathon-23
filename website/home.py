from flask import Flask, redirect, url_for, request, render_template
from pymongo.mongo_client import MongoClient
import pandas as pd
import numpy as np

uri = "mongodb+srv://vighneshvembaar:3HvgpBVcYXsu3VUM@jobberjobbee.jg4fczh.mongodb.net/?retryWrites=true&w=majority"
temp = "hi"
app = Flask(__name__)
client = MongoClient(uri)  # connect to your MongoDB server
db = client['jobberjobbee']  # replace 'your_database' with your database name
collection = db['responses']  # replace 'your_collection' with your collection name
collection1 = db['jobbers']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("@@" + str(e) + "@@")


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    accountType = request.form.get('accountType')
    if accountType == '0':
        accountType = 'Jobber'
    elif accountType == '1':
        accountType = 'Jobbee'
    return redirect(url_for('login_get', userName=username, accountType=accountType))


@app.route('/login/<userName>/<accountType>')
def login_get(accountType, userName):
    if accountType == 'Jobber':
        return redirect(url_for('jobber_home', userName=userName))
    elif accountType == 'Jobbee':
        return redirect(url_for('jobbee_quiz', userName=userName))


@app.route('/<userName>/Jobber')
def jobber_home(userName):
    global temp
    temp = userName
    existing_user = collection1.find_one({'username': userName})
    if existing_user is None:
        new_user_data = {'username': userName, 'jobs': []}
        collection1.insert_one(new_user_data)

    return render_template("jobber_home.html")


@app.route('/create_job', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        # Handle form submission here
        username = temp  # Get the username from the form
        # username = userName
        job_title = request.form.get('job_title')
        job_description = request.form.get('job_description')
        # Extract more job information from the form



        # Create a dictionary with the job information
        job_data = {
            'job_title': job_title,
            'job_description': job_description,
            'communication': 0,
            'leadership': 0,
            'team_work': 0,
            'adaptability': 0,
            'problem_solving': 0,
            'interpersonal_skill': 0,
            'loyalty': 0
        }
        print(username)
        # Update the user's dictionary in collection1 with the job information
        # Make sure the user already exists in collection1
        existing_user = collection1.find_one({'username': username})

        if existing_user:
            existing_user['jobs'].append(job_data)  # Assuming 'jobs' is a list field in the user's document
            collection1.update_one({'username': username}, {'$set': {'jobs': existing_user['jobs']}})
            return 'Job has been added!'
        else:
            return 'User does not exist.'  # You can handle this case accordingly

    return render_template("create_job.html")


@app.route('/review_applications')
def review_applications():
    # fetch data from MongoDB and pass to template
    x = collection1.find()
    for i in x:
        if i['username'] == temp:
            print(i)
    return render_template("review_applications.html", applications=i)


@app.route('/<userName>/Jobbee')
def jobbee_quiz(userName):
    return render_template("jobbee_quiz.html")


@app.route('/submit', methods=['POST'])
def submit():
    link = request.form.get('link')
    dropdown = request.form.get('dropdown')
    # add more variables here for the rest of your questions

    # create a document with the form data
    document = {
        'link': link,
        'dropdown': dropdown,
        'communication': 0,
        'leadership': 0,
        'team_work': 0,
        'adaptability': 0,
        'problem_solving': 0,
        'interpersonal_skill': 0,
        'loyalty': 0
    }

    df = pd.read_csv(r"C:\Users\vigne\Downloads\dataset_doc - Sheet1 - Copy.csv")

    for i in range(12):
        for j in range(3):
            qxoy = request.form.get(f'q{i + 1}o{j + 1}')
            if qxoy == '1':
                document['communication'] += df['communication'][(i*3)+j] * 3
                document['leadership'] += df['leadership'][(i*3)+j] * 3
                document['team_work'] += df['team_work'][(i*3)+j] * 3
                document['adaptability'] += df['adaptability'][(i*3)+j] * 3
                document['problem_solving'] += df['problem_solving'][(i*3)+j] * 3
                document['interpersonal_skill'] += df['interpersonal_skill'][(i*3)+j] * 3
                document['loyalty'] += df['loyalty'][(i*3)+j] * 3
            elif qxoy == '2':
                document['communication'] += df['communication'][(i*3)+j] * 2
                document['leadership'] += df['leadership'][(i*3)+j] * 2
                document['team_work'] += df['team_work'][(i*3)+j] * 2
                document['adaptability'] += df['adaptability'][(i*3)+j] * 2
                document['problem_solving'] += df['problem_solving'][(i*3)+j] * 2
                document['interpersonal_skill'] += df['interpersonal_skill'][(i*3)+j] * 2
                document['loyalty'] += df['loyalty'][(i*3)+j] * 2
            elif qxoy == '3':
                document['communication'] += df['communication'][(i*3)+j]
                document['leadership'] += df['leadership'][(i*3)+j]
                document['team_work'] += df['team_work'][(i*3)+j]
                document['adaptability'] += df['adaptability'][(i*3)+j]
                document['problem_solving'] += df['problem_solving'][(i*3)+j]
                document['interpersonal_skill'] += df['interpersonal_skill'][(i*3)+j]
                document['loyalty'] += df['loyalty'][(i*3)+j]


    # insert the document into the MongoDB collection
    for key, value in document.items():
        if isinstance(value, np.int64):
            document[key] = int(value)/72
    collection.insert_one(document)

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run()
