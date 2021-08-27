from flask import Flask


app = Flask(__name__)

@app.route("/")
def test_request():
    return "สวัสดีๆๆๆ"


if __name__ == '__main__':
    app.run()
