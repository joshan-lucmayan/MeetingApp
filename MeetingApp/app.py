from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

import subprocess
import os
import platform

# CREATE APP FIRST
app = Flask(__name__, instance_relative_config=True)

db_path = os.path.join(app.instance_path, "meetings.db")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_path
db = SQLAlchemy(app)

# MODEL
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.String(50), nullable=False)

# ROUTES
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/setup_meeting', methods=['POST'])
def setup_meeting():
    data = request.json
    payload = f"{data['host']}|{data['date_time']}"
    print('HOST NAME ' + data['host'])

    if platform.system() == "Windows":
        exe_path = os.path.join(os.getcwd(), "sign.exe")
    else:
        exe_path = os.path.join(os.getcwd(), "sign")
    result = subprocess.run([exe_path, payload], capture_output=True, text=True)

    new_meeting = Meeting(name=data['name'], host=data['host'], date_time=data['date_time'])
    db.session.add(new_meeting)
    db.session.commit()

    return jsonify({"status": "signed", "signature": result.stdout.strip()})

# RUN APP
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)