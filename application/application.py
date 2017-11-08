from flask import *
import SQLAlchemy
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
