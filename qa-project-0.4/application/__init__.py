from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:groot@35.234.132.64/flask_db'
app.config['SECRET_KEY'] = 'asdlaksfjafljf2487r2894rhwf'
db = SQLAlchemy(app)

from application import routes