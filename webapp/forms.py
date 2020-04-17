from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class data(FlaskForm):

    T1 = StringField(
        'T1 data',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "T1 Data",
            "type": "text"})

    T2 = StringField(
        'T2 data',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "T2 Data",
            "type": "text"})

    submit = SubmitField(
        'Отправить',
        render_kw={
            "class": "btn btn-outline-primary",
            "Type": "submit"})
