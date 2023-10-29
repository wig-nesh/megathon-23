import json
from flask import Flask, render_template

json_file_path = "package.json"

try:
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print(f"File '{json_file_path}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(r'profile.html', occupation=data['occupation'], name=data['full_name'], imageURL=data['profile_pic_url'], location=(data['city'] + ', ' + data['country']), experiences=data.get('experiences', []))

if __name__ == '__main__':
    app.run()