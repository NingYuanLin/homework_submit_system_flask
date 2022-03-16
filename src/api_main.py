# Time:2022/3/16 3:39 PM
# Author:NYL
# Describe:
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(root_path)
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from src.core.upload_file import upload_file
from src.core.history_search import history_search

app = Flask(__name__)

CORS(app, supports_credentials=True)


@app.route('/upload_file', methods=['POST'])
def api_upload_file():
    file = request.files.get('file')
    username = request.form.get('username')
    student_id = request.form.get('studentId').lower()
    filename = file.filename
    result = upload_file(username, student_id, filename, file.read())
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response


@app.route('/history_search', methods=['POST'])
def api_history_search():
    username = request.form.get('username')
    student_id = request.form.get('studentId').lower()
    result = history_search(username, student_id)
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response


if __name__ == '__main__':
    app.run('0.0.0.0', port=3600)
