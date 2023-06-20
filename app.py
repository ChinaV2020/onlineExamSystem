from flask import Flask, render_template
import os
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    data_folder = os.path.join(app.root_path, 'static', 'data')
    file_list = os.listdir(data_folder)
    return render_template('index.html', files=file_list)


@app.route('/data/<file_name>')
def show_data(file_name):
    data_folder = os.path.join(app.root_path, 'static', 'data')
    file_list = os.listdir(data_folder)
    file_path = os.path.join(data_folder, file_name)
    headers = []
    questions = {}
    result = []
    if os.path.isfile(file_path):
        excel = pd.read_excel(file_path)
        headers = excel.columns.tolist()
        data = excel.values.tolist()
        for d in data:
            questions[d[0]] = {'question': d[1], 'choices': d[2:-1]}
            result.append(d[2:-1][ord(d[-1]) - 65])

        return render_template('data.html', files=file_list, selected_file=file_name, headers=headers,
                               questions=questions, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
