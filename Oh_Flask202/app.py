from flask import Flask

app = Flask(__name__)


@app.route('/helloworld')
def hello_world():  # put application's code here
    return 'HelloWorld'


if __name__ == '__main__':
    app.run()
