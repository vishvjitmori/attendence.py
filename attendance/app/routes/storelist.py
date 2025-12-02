from flask import Blueprint, render_template,session
from app import db
from app.model import Store


storelist_bp = Blueprint('storelist', __name__)

@storelist_bp.route("/storelist", methods = ["GET","POST"])
def storelist():

    stores = Store.query.all()
    print(stores)
    return render_template('storelist.html', stores=stores)