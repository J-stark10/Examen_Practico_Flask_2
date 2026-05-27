from flask import render_template, request, redirect, url_for, Blueprint
from src.app import db
from src.pacientes.models import Paciente

bp_pacientes = Blueprint('pacientes', __name__, template_folder='templates')

@bp_pacientes.route('/')
def index():
    pacientes = Paciente.query.all()
    return render_template('paciente/index.html', pacientes=pacientes)

@bp_pacientes.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')

        paciente = Paciente(nombre=nombre, telefono=telefono)
        db.session.add(paciente)
        db.session.commit()

        return redirect(url_for('pacientes.index'))

    return render_template('paciente/create.html')

@bp_pacientes.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    paciente = Paciente.query.get(id)

    if request.method == 'POST':
        paciente.nombre = request.form.get('nombre')
        paciente.telefono = request.form.get('telefono')

        db.session.commit()

        return redirect(url_for('pacientes.index'))
    return render_template('paciente/edit.html', paciente=paciente)

@bp_pacientes.route('/delete/<int:id>')
def delete(id):
    paciente = Paciente.query.get(id)
    db.session.delete(paciente)
    db.session.commit()

    return redirect(url_for('pacientes.index'))