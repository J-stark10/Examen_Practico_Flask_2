from flask import render_template, request, redirect, url_for, Blueprint
from src.app import db
from src.medicos.models import Medico

bp_medicos = Blueprint('medicos', __name__, template_folder='templates')

@bp_medicos.route('/')
def index():
    medicos = Medico.query.all()
    return render_template('medico/index.html', medicos=medicos)

@bp_medicos.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        especialidad = request.form.get('especialidad')

        medico = Medico(nombre=nombre, especialidad=especialidad)
        db.session.add(medico)
        db.session.commit()

        return redirect(url_for('medicos.index'))

    return render_template('medico/create.html')

@bp_medicos.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    medico = Medico.query.get(id)

    if request.method == 'POST':
        medico.nombre = request.form.get('nombre')
        medico.especialidad = request.form.get('especialidad')

        db.session.commit()

        return redirect(url_for('medicos.index'))
    return render_template('medico/edit.html', medico=medico)

@bp_medicos.route('/delete/<int:id>')
def delete(id):
    medico = Medico.query.get(id)
    db.session.delete(medico)
    db.session.commit()

    return redirect(url_for('medicos.index'))

