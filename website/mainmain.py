from flask import Flask, redirect, url_for, request, render_template
from pymongo.mongo_client import MongoClient
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from operator import itemgetter

uri = "mongodb+srv://vighneshvembaar:3HvgpBVcYXsu3VUM@jobberjobbee.jg4fczh.mongodb.net/?retryWrites=true&w=majority"

def home():
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    global temp
    temp = username
    accountType = request.form.get('accountType')
    if accountType == '0':
        accountType = 'Jobber'
def create_job():
        username = request.form.get('userName')  # Get the username from the form
        job_title = request.form.get('job_title')
        job_description = request.form.get('job_description')
        job_type = request.form.get('job_type')
        # Extract more job information from the form
        train = pd.read_csv(r'/doc_test.csv')

        train = pd.read_csv('\doc_test.csv')

        train['text'] = train['text'].str.lower()
        train['text'] = train['text'].replace('[^a-zA-Z0-9]', ' ', regex=True)
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(train['text'])
        cats = ['communication', 'leadership', 'team_work', 'adaptability', 'problem_solving', 'interpersonal_skill', 'loyalty']
        ans = []
        for category in cats:
            X_train, X_test, y_train, y_test = train_test_split(X, train[category], test_size=0.4, random_state = 42)
        cats = ['communication', 'leadership', 'team_work', 'adaptability', 'problem_solving', 'interpersonal_skill',
                'loyalty']
        ans = []
        for category in cats:
            X_train, X_test, y_train, y_test = train_test_split(X, train[category], test_size=0.4, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)
            new_job_description = [job_description]
            new_X = vectorizer.transform(new_job_description)
            predicted_scores = model.predict(new_X)
            ans.append(new_X)
        # Create a dictionary with the job information
        job_data = {
def create_job():
        }

        print(job_data)
            ans.append(predicted_scores[0])

        # Convert sparse matrix to dense numpy array and then to list

        # Use list_array instead of new_X
        job_data = {
            'job_title': job_title,
            'job_description': job_description,
            'job_type': job_type,
            'Communication': ans[0],
            'Leadership': ans[1],
            'Team Work': ans[2],
            'Adaptability': ans[3],
            'Problem Solving': ans[4],
            'Interpersonal Skills': ans[5],
            'Loyalty': ans[6]
        }

        print(username)
>>>>>>> Stashed changes
        # Update the user's dictionary in collection1 with the job information
        # Make sure the user already exists in collection1
        existing_user = collection1.find_one({'username': username})
@ -117,6 +159,39 @@ def review_applications():
        print(i)
    return render_template("review_applications.html", applications=i)

    x = collection.find()  # jobbee
    y = collection1.find()  # jobber
    X = []
    Y = []
    outputs = []
    for i in y:
        if i['username'] == temp:
            for l in i['jobs']:
                X.append([l['Communication'], l['Leadership'], l['Team Work'], l['Adaptability'], l['Problem Solving'],
                          l['Interpersonal Skills'], l['Loyalty']])
    for i in x:
        print(i)
        a = [i['communication'], i['leadership'], i['team_work'], i['adaptability'], i['problem_solving'],
             i['interpersonal_skill'], i['loyalty']]
        b = []
        for k in X:
            b.append(np.dot(k, a) / (norm(k) * norm(a)))
        outputs.append({'cosine': b,
                        'links': i['link'],
                        'type': i['dropdown']})

    print(outputs)
    sorted_data = []
    for i in range(len(outputs[0]['cosine'])):
        # Sort by i-th cosine similarity
        outputs.sort(key=lambda w: w['cosine'][i], reverse=True)
        sorted_data.append(outputs.copy())
    print(sorted_data)

    # return sorted_data
    return render_template("review_applications.html", sorted_data=sorted_data)
>>>>>>> Stashed changes


@app.route('/<userName>/Jobbee')
def jobbee_quiz(userName):
@ -131,6 +206,7 @@ def submit():

    # create a document with the form data
    document = {
        'name': temp,
        'link': link,
        'dropdown': dropdown,
        'communication': 0,
@ -142,44 +218,44 @@ def submit():
        'loyalty': 0
    }

    df = pd.read_csv(r"C:\Users\vigne\Downloads\dataset_doc - Sheet1 - Copy.csv")
    df = pd.read_csv("\dataset_doc - Sheet1 - Copy.csv")

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
                document['communication'] += df['communication'][(i * 3) + j] * 3
                document['leadership'] += df['leadership'][(i * 3) + j] * 3
                document['team_work'] += df['team_work'][(i * 3) + j] * 3
                document['adaptability'] += df['adaptability'][(i * 3) + j] * 3
                document['problem_solving'] += df['problem_solving'][(i * 3) + j] * 3
                document['interpersonal_skill'] += df['interpersonal_skill'][(i * 3) + j] * 3
                document['loyalty'] += df['loyalty'][(i * 3) + j] * 3
            elif qxoy == '2':
                document['communication'] += df['communication'][(i*3)+j] * 2
                document['leadership'] += df['leadership'][(i*3)+j] * 2
                document['team_work'] += df['team_work'][(i*3)+j] * 2
                document['adaptability'] += df['adaptability'][(i*3)+j] * 2
                document['problem_solving'] += df['problem_solving'][(i*3)+j] * 2
                document['interpersonal_skill'] += df['interpersonal_skill'][(i*3)+j] * 2
                document['loyalty'] += df['loyalty'][(i*3)+j] * 2
                document['communication'] += df['communication'][(i * 3) + j] * 2
                document['leadership'] += df['leadership'][(i * 3) + j] * 2
                document['team_work'] += df['team_work'][(i * 3) + j] * 2
                document['adaptability'] += df['adaptability'][(i * 3) + j] * 2
                document['problem_solving'] += df['problem_solving'][(i * 3) + j] * 2
                document['interpersonal_skill'] += df['interpersonal_skill'][(i * 3) + j] * 2
                document['loyalty'] += df['loyalty'][(i * 3) + j] * 2
            elif qxoy == '3':
                document['communication'] += df['communication'][(i*3)+j]
                document['leadership'] += df['leadership'][(i*3)+j]
                document['team_work'] += df['team_work'][(i*3)+j]
                document['adaptability'] += df['adaptability'][(i*3)+j]
                document['problem_solving'] += df['problem_solving'][(i*3)+j]
                document['interpersonal_skill'] += df['interpersonal_skill'][(i*3)+j]
                document['loyalty'] += df['loyalty'][(i*3)+j]

                document['communication'] += df['communication'][(i * 3) + j]
                document['leadership'] += df['leadership'][(i * 3) + j]
                document['team_work'] += df['team_work'][(i * 3) + j]
                document['adaptability'] += df['adaptability'][(i * 3) + j]
                document['problem_solving'] += df['problem_solving'][(i * 3) + j]
                document['interpersonal_skill'] += df['interpersonal_skill'][(i * 3) + j]
                document['loyalty'] += df['loyalty'][(i * 3) + j]

    # insert the document into the MongoDB collection
    for key, value in document.items():
        if isinstance(value, np.int64):
            document[key] = int(value)/72
            document[key] = int(value) / 72
    collection.insert_one(document)

    return 'Form submitted successfully!'


if __name__ == '__main__':
    app.run()