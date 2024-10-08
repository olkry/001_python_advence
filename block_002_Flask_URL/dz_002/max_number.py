from flask import Flask

app = Flask(__name__)

@app.route('/max_num/<path:numbers>')
def max_number(numbers:str):
    num = (int(i) for i in numbers.split('/'))
    return f"Большее из введенных чисел: {max(num)}"

if __name__ == '__main__':
    app.run(debug=True)