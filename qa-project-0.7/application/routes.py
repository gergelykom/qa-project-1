from application import app, db
from application.models import Species
from flask import render_template, request, redirect, url_for
from application.forms import TaskForm
@app.route('/')
@app.route('/home')
def home():
    all_species = Species.query.all()
    output = ''
    return render_template('index.html', title='Home', all_species = all_species)

@app.route('/create', methods = ['GET', 'POST'])
def create():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Species(description = form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html', title = 'Create', form = form)



@app.route('/confirm/<int:id>')
def confirm(id):
    task = Species.query.filter_by(id=id).first()
    task.confirmed = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/unconfirmed/<int:id>')
def unconfirmed(id):
    task = Species.query.filter_by(id=id).first()
    task.confirmed = False
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods = ['GET','POST'])
def update(id):
    form = TaskForm()
    task = Species.query.filter_by(id=id).first()
    if request.method == 'POST':
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('update.html', form=form, title='Updated Task', task=task)

@app.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    task = Species.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))