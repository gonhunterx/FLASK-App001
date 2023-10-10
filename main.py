# we will run this when we want to start our website
# we can do this call because we put an init file in the folder
# it initalized it into a python package
from website import create_app

app = create_app()


# you do this if name == in python to make sure
# that it is this exact file that runs it not some other one
if __name__ == "__main__":
    app.run(debug=True)
    # debug=True will automatically rerun the server its like nodemon
