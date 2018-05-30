# -*-coding: utf-8-*-

from flask import Flask, request, jsonify
import handler

app = Flask(__name__)

@app.route("/", methods=["POST"])
def naver_talk():
    data = request.get_json()
    response = handler.get_handler(data)

    return jsonify(response), 200

@app.route(rule="/hello", methods=["GET"])
def hello():
    response = "hello world!"
    return response, 200

@app.route(rule="/world", methods=["POST"])
def world():
    response = "hello world!"
    return response, 200

if __name__ == "__main__":
    ssl_cert = '/etc/letsencrypt/live/daeta.ga/fullchain.pem'
    ssl_key =  '/etc/letsencrypt/live/daeta.ga/privkey.pem'
    contextSSL =  (ssl_cert, ssl_key)
    app.run(host='0.0.0.0', port=443, debug = True, ssl_context = contextSSL)

