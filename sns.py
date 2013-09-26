from flask import Flask, redirect, url_for, send_from_directory, request, jsonify
app = Flask(__name__)
import json

@app.route("/", methods=['POST'])
def home():
    resp = {}
    if request.method == 'POST':
        with open("sns-messages.log", "a") as myfile:
            myfile.write(request.data)
            myfile.write("\n")
        resp['success'] = True
    else:
        resp['success'] = False
    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
