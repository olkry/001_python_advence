import flask

app = flask.Flask(__name__)

@app.endpoint('test')
def test_endpoint():
    return 'Test endpoint'

if __name__ == '__main__':
    app.run()