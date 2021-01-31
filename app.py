from flask import Flask, jsonify, request, render_template

from max_gather import get_max_apples

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(data=(get_max_apples([3, 1, 10, 30, 1, 1], 2, 3))), 200
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
