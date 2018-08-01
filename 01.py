#!/usr/bin/python
from flask import Flask, render_template, request

app = Flask(__name__)


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
    return res

if __name__ == "__main__":
    app.run(debug=True)
