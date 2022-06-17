from crypt import methods
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddSnackForm, NewEmployeeForm
from models import (
    db,
    connect_db,
    Department,
    Employee,
    Project,
    EmployeeProject,
    get_directory,
    get_directory_join,
    get_directory_join_class,
    get_directory_all_join,
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///employees_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenz123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
deb = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/phones")
def list_phones():
    emps = Employee.query.all()
    return render_template("phones.html", emps=emps)


@app.route("/snacks/new", methods=["GET", "POST"])
def add_snack():
    form = AddSnackForm()
    if form.validate_on_submit():
        raise
        # Is this a POST request AND is the token valid?
        name = form.name.data
        price = form.price.data
        flash(f"Created new snack: name is {name}, price is ${price}")
        return redirect("/")
    else:
        return render_template("add_snack_form.html", form=form)


@app.route("/employees/new", methods=["GET", "POST"])
def add_employee():
    form = NewEmployeeForm()

    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data

        emp = Employee(name=name, state=state, dept_code=dept_code)
        db.session.add(emp)
        db.session.commit()
        return redirect("/phones")
    else:
        return render_template("add_employee_form.html", form=form)
