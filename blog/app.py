from flask import Flask, render_template, url_for
from blog.user import views
from blog.report import views


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

""" def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app



def register_blueprints(app: Flask):
    app.register_blueprint(views.user)
    app.register_blueprint(views.report) """