from flask import Blueprint, render_template, request, make_response, jsonify
from flask_login import login_required, current_user

from models import db, User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@main.route("/edit/email", methods=["POST"])
@login_required
def modifier_email():
    try:
        nouveau_email = request.form.get('nouveau_email')
        admin = User.query.filter_by(id=current_user.id).first()
        admin.email = nouveau_email
        db.session.commit()
        data = {'message': 'Votre email a ete modifier', 'code': 'SUCCESS'}
        return make_response(jsonify(data), 200)
    except Exception as exc:
        print(exc)
        return make_response(jsonify({'message': 'Une erreur est survecu, veuillez ressayer plus tard.'}), 500)

