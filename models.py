from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1Cowbirds@localhost:5432/the-growing-place'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
key = Fernet.generate_key()

encoded_key = key.decode()

os.environ['ENCRYPTION_KEY'] = encoded_key
encryption_key = os.environ.get('ENCRYPTION_KEY')
cipher_suite = Fernet(encryption_key)


class Application(db.Model):

    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(25), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    middle_initial = db.Column(db.String(1), nullable=False)
    street_address = db.Column(db.String(50), nullable=False)
    apartment_unit_number = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String(40), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    date_available = db.Column(db.Date, nullable=False)
    social_security_number = db.Column(db.String(14), nullable=False)
    desired_pay = db.Column(db.Float, nullable=False)
    position_applied_for = db.Column(db.String(30), nullable=False)
    legally_eligible = db.Column(db.Boolean, nullable=False)
    felony = db.Column(db.Boolean, nullable=False)
    explanation = db.Column(db.String(225), nullable=True)
    high_school = db.Column(db.String(40), nullable=True)
    address = db.Column(db.String(40), nullable=True)
    hs_from = db.Column(db.Date, nullable=True)
    hs_to = db.Column(db.Date, nullable=True)
    hs_graduate_bool = db.Column(db.Boolean, nullable=False, default=False)
    college = db.Column(db.String(40), nullable=True)
    co_address = db.Column(db.String(40), nullable=True)
    co_from = db.Column(db.Date, nullable=True)
    co_to = db.Column(db.Date, nullable=True)
    co_graduate_bool = db.Column(db.Boolean, nullable=True, default=False)
    degree = db.Column(db.String(50), nullable=True)
    other_ed = db.Column(db.String(50), nullable=True)
    other_address = db.Column(db.String(50), nullable=True)
    other_from = db.Column(db.Date, nullable=True)
    other_to = db.Column(db.Date, nullable=True)
    other_graduate_bool = db.Column(db.Boolean, nullable=True, default=False)
    other_degree = db.Column(db.String(50), nullable=True)
    cpr_firstaid = db.Column(db.String(225), nullable=True)
    early_childhood = db.Column(db.String(225), nullable=True)
    early_childhood_classes = db.Column(db.String(225), nullable=True)
    adjudicated = db.Column(db.String(10), nullable=True)  
    sex_offender = db.Column(db.String(10), nullable=True) 
    dcf = db.Column(db.String(225), nullable=False)
    parental_rights = db.Column(db.String(10), nullable=False) 
    resume_path = db.Column(db.String(255), nullable=True)
    signature_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, server_default=db.func.current_date(), nullable=False)

    def set_social_security_number(self, ssn):
        # Encrypt the SSN
        social_security_number = cipher_suite.encrypt(ssn.encode())
        self.encrypted_ssn = social_security_number.decode()

    def get_social_security_number(self):
        # Decrypt and return the SSN
        decrypted_ssn = cipher_suite.decrypt(self.social_security_number.encode())
        return decrypted_ssn.decode()

    def __repr__(self):
        return f"FIRST NAME: {self.first_name}"


class Employment(db.Model):

    __tablename__ = 'employments'

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

class Reference(db.Model):

    __tablename__ = 'references'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    relationship = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    application = db.relationship('Application', backref=db.backref('references', lazy=True))