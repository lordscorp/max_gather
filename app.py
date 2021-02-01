from flask import Flask, jsonify, request, render_template

from flask_cors import CORS

from max_gather import get_max_apples

app = Flask(__name__)

# ativar CORS (somente para facilitar os testes em ambientes de desenvolvimento)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return jsonify(data=(get_max_apples(request.form['A'], request.form['K'], request.form['L']))), 200
    else:
        return render_template('index.html'), 200


if __name__ == '__main__':
    app.run()
