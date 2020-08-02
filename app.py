from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new-data')
def new():
    return render_template('form.html')


@app.route('/record-data', methods=['POST'])
def record():
    #import create_db
    name = request.form['name']
    import record_face as rf
    rf.record(name)
    return render_template('index.html')


@app.route('/recognise')
def recognise():
    import training
    import face_recognisor

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
