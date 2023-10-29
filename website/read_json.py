import json
from flask import Flask, render_template
import requests

json_file_path = "package.json"

try:
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print(f"File '{json_file_path}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

app = Flask(__name__)

def get_codeforces_rating(handle):
    api_url = f"https://codeforces.com/api/user.info?handles={handle}"

    try:
        response = requests.get(api_url)
        data = response.json()

        if data['status'] == 'OK':
            user_info = data['result'][0]
            rating = user_info['rating']
            return rating
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/')
def index():
    skills = data.get("skills", [])
    user_handle = "vignesh_x"
    rating = get_codeforces_rating(user_handle)

    if rating is not None:
        skills.append(f"Codeforces Rating: {rating}")

    return render_template(r'profile.html', occupation=data['occupation'], name=data['full_name'], imageURL=data['profile_pic_url'], location=(data['city'] + ', ' + data['country']), skills=skills, experiences=data.get('experiences', []), education=data.get('education', []))

if __name__ == '__main__':
    app.run()