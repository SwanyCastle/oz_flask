from flask import request, render_template, redirect, url_for, abort

from db import db
from models import User

from datetime import datetime
import pytz

def routing_app(app):
    @app.route('/')
    def index():
        users = User.query.all()
        datas = [
            {
                'id': user.id,
                'name': user.name,
                'age': user.age,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            } for user in users
        ]
        return render_template('index.html', users=datas)

    @app.route('/add', methods=['GET', 'POST'])
    def add():
        if request.method == 'POST':
            name = request.form['username']
            age = request.form['age']
            localtime = pytz.timezone('Asia/Seoul')
            user = User(name=name, age=age, created_at=datetime.now(localtime))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add_user.html')

    @app.route('/edit/<username>', methods=['GET', 'POST'])
    def edit(username):
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "Not Found")
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']

            localtime = pytz.timezone('Asia/Seoul')
        
            user.name = name
            user.age = age
            user.updated_at = datetime.now(localtime)

            db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit_user.html', user=user)

    @app.route('/delete/<username>')
    def delete(username):
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "Not Found")
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))