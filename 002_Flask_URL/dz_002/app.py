from flask import Flask

app = Flask(__name__)
file_path = '../test/output_file.txt'

@app.route('/summary')

def get_summary_rss():
    units = ['']