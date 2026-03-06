from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import subprocess
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetings.db'
db = SQLAlchemy(app)

# Model definition
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.String(50), nullable=False)

@app.route('/setup_meeting', methods=['POST'])
def setup_meeting():
    data = request.json
    payload = f"{data['host']}|{data['date_time']}"
    print('HOST NAME' + data['host'])
    
    # Securely call the C utility using the correct relative path
    exe_path = os.path.join(os.getcwd(), 'sign', 'sign.exe')
    result = subprocess.run([exe_path, payload], capture_output=True, text=True)
    
    # Save to database
    new_meeting = Meeting(name=data['name'], host=data['host'], date_time=data['date_time'])
    db.session.add(new_meeting)
    db.session.commit()
    
    return jsonify({"status": "signed", "signature": result.stdout.strip()})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)