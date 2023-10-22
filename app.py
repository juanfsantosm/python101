from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


@app.route('/')
def welcome():  # put application's code here
    return render_template("welcome.html", name="fer", employees=db)

@app.route('/employee/<int:index>')
def employee_view(index):
    try:
        employee = db[index]
        return render_template("employee.html",
                               employee=employee,
                               index=index,
                               max_index=len(db)-1)
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run()
