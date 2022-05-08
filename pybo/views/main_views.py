from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def home():
    return render_template('main/Home.html')


@bp.route('/about')
def about():
    return render_template('main/about.html')


@bp.route('/feedback')
def feedback():
    return render_template('main/feedback.html')


@bp.route('/Enter_URL_Before')
def Enter_URL_Before():
    return render_template('main/Enter_URL_Before.html')
