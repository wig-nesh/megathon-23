from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
# client = MongoClient('mongodb://localhost:27017/')  # connect to your MongoDB server
# db = client['your_database']  # replace 'your_database' with your database name
# collection = db['your_collection']  # replace 'your_collection' with your collection name

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
    return render_template("jobber_home.html")

@app.route('/create_job', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        # handle form submission here
        pass
    return render_template("create_job.html")

@app.route('/review_applications')
def review_applications():
    # fetch data from MongoDB and pass to template
    return render_template("review_applications.html")

@app.route('/<userName>/Jobbee')
def jobbee_quiz(userName):
    return render_template("jobbee_quiz.html")

# @app.route('/submit', methods=['POST'])
# def submit():
#     link = request.form.get('link')
#     q1 = request.form.get('q1')
#     dropdown = request.form.get('dropdown')
#     # add more variables here for the rest of your questions
#
#     # create a document with the form data
#     document = {
#         'link': link,
#         'q1': q1,
#         'dropdown': dropdown,
#         # add more fields here for the rest of your questions
#     }
#
#     # insert the document into the MongoDB collection
#     collection.insert_one(document)
#
#     return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run()
