from flask import Flask

app = Flask(__name__)

# 'абра-кадабра' 'абра._кадабра' 'абра..-кадабра.' 'а..бра..-ка..даб.ра' 'абра.....-кад..абр...а' 'а....бра-..кадабр....а'

@app.route('/des/<text>')
def descryption(text:str):
    result = []

    for char in text:
        result.append(char)

        if len(result) > 2 and (result[-1], result[-2]) == ('.','.'):
            result.pop()
            result.pop()
            if result:
                result.pop()

    decr = ''.join(ch for ch in result if ch != '.')

    return str(decr)

if __name__ == '__main__':
    app.run(debug=True)
