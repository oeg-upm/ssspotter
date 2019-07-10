import os

from flask import Flask, g, request, render_template, jsonify
from werkzeug.utils import secure_filename
import requests
import random
import string
import subprocess
import logging

from spotter import spot_subject_column


logger = logging.getLogger(__name__)
app = Flask(__name__)


def get_random(size=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))


@app.route('/')
def hello_world():
    return 'Hello World! This is the simple spotter'


@app.route('/spot', methods=['GET', 'POST'])
def spot():
    if request.method == 'GET':
        return render_template('spot.html')
    else:
        uploaded_file = request.files['table']
        technique = request.form['technique']
        callback_url = request.form['callback']
        fname = get_random()+".csv"
        uploaded_file.save(os.path.join('local_uploads', fname))
        if callback_url.strip()=="":
            col_id = spot_subject_column(fname=fname, technique=technique)
            return jsonify(subject_col_id=col_id)
        else:
            python_exec = ".venv/bin/python"
            if not os.path.exists(python_exec):
                python_exec = "python"
            comm = """ %s spotter.py "%s" "%s" "%s" """ % (python_exec, fname, technique, callback_url)
            print("comm: "+comm)
            subprocess.Popen(comm, shell=True)
            return jsonify(msg="In progress, the callback url will be called once the subject column is identified")


if __name__ == '__main__':
    if 'port' in os.environ:
        app.run(debug=True, host='0.0.0.0', port=int(os.environ['port']))
    else:
        app.run(debug=True, host='0.0.0.0')






