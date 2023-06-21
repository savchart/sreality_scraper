from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/postgres'
db = SQLAlchemy(app)

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    image_url = db.Column(db.String(500), unique=True, nullable=False)

@app.route('/')
def home():
    ads = Ad.query.all()
    return render_template('index.html', ads=ads)



if __name__ == '__main__':
    app.run()
