# <div class="question">
#     <p>Question 1: You discover your colleague might be leaking confidential company data for personal gain. How do you handle this situation?</p>
#     <input type="number" id="q1o1" name="q1" value="option1" min="1" max="3">
#     <label for="q1o1">Confront the colleague directly to address and resolve the breach.</label><br>
#     <input type="number" id="q1o2" name="q1" value="option2" min="1" max="3">
#     <label for="q1o2">Ignore the situation to avoid conflict or potential negative repercussions.</label><br>
#     <input type="number" id="q1o3" name="q1" value="option3" min="1" max="3">
#     <label for="q1o3">Hold the information and observe for further evidence before taking action.</label><br>
# </div>

import pandas as pd


def csv_to_html(csv_file):
    df = pd.read_csv(csv_file)
    html = ''
    for i, row in df.iterrows():
        html += f'''
        <div class="question">
            <p>Question {i + 1}: {row[0]}</p>
            <input type="number" id="q{i + 1}o1" name="q{i + 1}o1" value="option1" min="1" max="3">
            <label for="q{i + 1}o1">{row[1]}</label><br>
            <input type="number" id="q{i + 1}o2" name="q{i + 1}o2" value="option2" min="1" max="3">
            <label for="q{i + 1}o2">{row[2]}</label><br>
            <input type="number" id="q{i + 1}o3" name="q{i + 1}o3" value="option3" min="1" max="3">
            <label for="q{i + 1}o3">{row[3]}</label><br>
        </div>
        '''
    return html


# Use the function
html = csv_to_html(r"C:\Users\vigne\Downloads\dataset_doc - Sheet1.csv")
print(html)
