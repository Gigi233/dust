from wtforms import StringField, Field
from wtforms.validators import DataRequired, Length, Email, ValidationError

from . import JSONForm
from ..core import current_user, db
from ..models.user_planet import User


class UserRegisterForm(JSONForm):
    username = Field('name', [DataRequired(), Length(max=20, min=1)])
    password = StringField('description', [DataRequired(), Length(max=20, min=4)])
    email = StringField('email', [DataRequired(), Email()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate_username(self, field):
        e = User.query.filter_by(username=field.data).first()
        if e:
            raise ValidationError('Duplicate username')

    def validate_email(self, field):
        e = User.query.filter_by(email=field.data).first()
        if e:
            raise ValidationError('Duplicate Email')

    def save(self, uid=None):
        if uid:
            user = User.query.get_or_404(uid)
        else:
            user = User()
            db.session.add(user)
        user.username = self.username.data
        user.password = self.password.data
        user.email = self.email.data

        db.session.commit()

        return user
