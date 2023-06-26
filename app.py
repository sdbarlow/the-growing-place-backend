from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1Cowbirds@localhost/the-growing-place'
db = SQLAlchemy(app)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    middle_initial = db.Column(db.String, nullable=False)
    street_address = db.Column(db.String, nullable=False)
    apartment_unit_number = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    date_available = db.Column(db.Date, nullable=False)
    social_security_number = db.Column(db.String, nullable=False)
    desired_pay = db.Column(db.Float, nullable=False)
    position_applied_for = db.Column(db.String, nullable=False)
    legally_eligible = db.Column(db.Boolean, nullable=False)
    felony = db.Column(db.Boolean, nullable=False)
    explanation = db.Column(db.String, nullable=True)

class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11))
    address = db.Column(db.String, nullable=False)
    supervisor = db.Column(db.String(25), nullable=False)
    job_title = db.Column(db.String(50), nullable=False)
    starting_pay = db.Column(db.Float, nullable=True)
    ending_pay = db.Column(db.Float, nullable=True)
    responsibilities = db.Column(db.String(225), nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)
    reason_for_leaving = db.Column(db.String(256), nullable=False)
    permission_to_contact = db.Column(db.Boolean, nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    application = db.relationship('Application', backref=db.backref('employments', lazy=True))






@app.route("/")
def hello():
    return "Hello, World"



if __name__ == '__main__':
    app.run()