from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '563278159357aedcff53698751259bca'

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:password@mysql:3306/blog'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes

retry = 128
for x in range(retry):
	try:
		tables = db.engine.table_names()
		break
	execpt:
		if x < retry -1:
			time.sleep(1)
			pass
		else:
			print("db connection failed after max retries")
			exit()
		
try:
	tables.remove('alembic_version')
except ValueError:
	pass

if len(tables) == 0:
	db.create_all()
	db.session.commit()
