from flask import Blueprint, render_template
from app import db
from app.model import Employee,Store



employeelist_bp = Blueprint ('employeelist', __name__)

@employeelist_bp.route("/employeelist", methods = ["GET","POST"])
def employeelist():
    employees = Employee.query.all()
    print(employees)
    return render_template('employeelist.html', employees=employees)