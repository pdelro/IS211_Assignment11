from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import re
import pickle

app = Flask(__name__)

todo_list = [
    ("Buy Eggs", "a@gmail.com", "High"),
    ("Get Vaccine", "b@gmail.com", "High"),
    ("Watch TV", "a@gmail.com", "Low"),
]


@app.route('/')
def display_list():
    #display
    return render_template("todo.html", todo_list=todo_list)


@app.route('/submit', methods=["POST"])
def submit():
    """
    Processing the data
    """
    global todo_list

    task = request.form['task']
    email = request.form['email']
    priority= request.form['priority']

    if not re.match(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
        print ("Invalid email.  Please enter valid email.")
        return redirect(url_for('display_list'))
    elif request.form['priority'] not in ("High", "Medium", "Low"):
        print ("Please select priority level.")

        return redirect(url_for('display_list'))
    else:
        todo_list.append((task, email, priority))
        return redirect(url_for('display_list'))


@app.route('/clear', methods=["POST"])
def clear():
    """
    Clear the list
    """
    global todo_list

    del todo_list[:]
    return redirect(url_for('display_list'))


if __name__ == '__main__':
    app.run(debug=True)