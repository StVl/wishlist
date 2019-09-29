from flask import Flask, jsonify, request, abort
from model import postgres_client
from model.wish import Wish
import uuid

app = Flask(__name__)


@app.route('/v1/mainPage')
def main_page():
    test = postgres_client.get_all_wishes(limit=20)
    return jsonify(test)


@app.route('v1/addWish', method='POST')
def new_wish():
    test_wish = Wish(uuid.uuid1, request.form['name'], request.form['dt_start'],
                     request.form['dt_end'], request.form['price'], request.form['description'])
    try:
        postgres_client.set_wish(test_wish)
    except:
        abort(500)
    return jsonify({"ok":"ok"})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
