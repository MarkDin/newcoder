#!/usr/bin/python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/')  # 指定某个页面路径的处理函数
@app.route('/')
def run():
    return "hello"


@app.route('/profile/<uid>/', methods=['Get', 'POST'])
def profile(uid):
    return render_template('profile.html', uid=uid)


if __name__ == "__main__":
    app.run(debug=True)
