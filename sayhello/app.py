from flask import Flask, Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .db import Session, Message

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    session = Session()
    # Adds message to database on POST.
    if request.method == 'POST':
        text = request.form['message_form_input']
        if len(text) > 0:
            session.add(Message(text=text, date_posted=datetime.utcnow()))
            session.commit()
        return redirect(url_for('index'))

    # Displays the messages on GET.
    messages = session.query(Message.text).order_by(Message.date_posted.desc())
    return render_template('index.html', messages=messages)


@app.teardown_appcontext
def remove_session(ctx):
    # The session is removed after each request.
    Session.remove()


__all__ = ['app']
