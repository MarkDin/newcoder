#!/usr/bin/python
from flask import Flask, render_template, request, make_response, flash, get_flashed_messages
from werkzeug.utils import redirect
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.secret_key = 'dk'


@app.route('/index/')  # 指定某个页面路径的处理函数
@app.route('/')
def run():
    return render_template('test.html')


@app.route('/profile/<uid>/', methods=['Get', 'POST'])
def profile(uid):
    list = ['a', 'b', 'c', 'd']
    d = {'name': 'dk', 'age': '12'}
    return render_template('profile.html', uid=uid, list=list, d=d)


@app.route('/requests')
def get_requests():
    res = request.args.get('key', 'hahah') + '<br>'
    res += request.url + '-----' + request.path + '<br>'
    for property in dir(request):
        res = res + str(property) + ' : ' + str(eval('request.' + property)) + '<br>'
    response = make_response(render_template('test.html'))
    # response.headers['X-Parachutes'] = 'parachutes are cool'
    # response.set_cookie('my_id', 'jj34646436')
    return response


@app.route('/newpath')
def new():
    return "newpath"


@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code)


@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html', url=request.url), 404


@app.route('/ok')
def ok():
    res = ''
    for msg, category in get_flashed_messages(with_categories=True):
        res = res + category + msg + '<br>'
    res += 'hello'
    return res


@app.route('/login')
def login():
    flash('123456', 'info')
    # return redirect('/ok')
    return "ok"


@app.route('/log/<level>/<msg>')
def log(level, msg):
    dict = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if level in dict.keys():
        app.logger.log(dict[level], msg)
    return 'logged:' + msg


def set_logger():
    info_file_handler = RotatingFileHandler('C:\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('C:\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('C:\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == "__main__":
    set_logger()
    app.run(debug=True)
