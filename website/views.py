# anything you can navigate to will be here
from flask import Blueprint, render_template

# blueprints means it has urls inside it and seperates app out

views = Blueprint("views", __name__)


# its called a 'decorator'
# the function below a @ statement will run when you go there
@views.route("/")
def home():
    return render_template("home.html")
