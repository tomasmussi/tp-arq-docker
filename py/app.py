from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return 'Hi, Im root'


if __name__ == "__main__":
    app.run()
