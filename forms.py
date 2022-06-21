from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Optional
from wtforms import (
    StringField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
)


class AddSnackForm(FlaskForm):
    """Form for adding snacks."""

    price = FloatField("Price in USD")
    name = StringField("Snack Name", validators=[
                       InputRequired(message="Snack field can't be blank")])
    is_healthy = BooleanField("This is a healthy snack")
    quantity = IntegerField("How Many?")

    # category = RadioField(
    #     "Category",
    #     choices=[
    #         ("ic", "Ice Cream"),
    #         ("chips", "Potato Chips"),
    #         ("candy", "Candy/Sweets"),
    #     ],
    # )

    category = SelectField(
        "Category",
        choices=[
            ("ic", "Ice Cream"),
            ("chips", "Potato Chips"),
            ("candy", "Candy/Sweets"),
        ],
    )

    email = StringField("Email", validators=[Optional(), Email()])


states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
          'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


class EmployeeForm(FlaskForm):
    """Form for adding a new employee"""

    name = StringField("Employee Name", validators=[
                       InputRequired(message="Name cannot be blank")])
    state = SelectField("State", choices=[(st, st) for st in states])
    dept_code = SelectField("Department Code")
