from flask_wtf import FlaskForm
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
    name = StringField("Snack Name")
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


class NewEmployeeForm(FlaskForm):
    """Form for adding a new employee"""

    name = StringField("Employee Name")
    state = StringField("State")
    dept_code = StringField("Department Code")
