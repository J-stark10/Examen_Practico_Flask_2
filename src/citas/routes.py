from flask import render_template, request, redirect, url_for, Blueprint
from src.app import db
from datetime import datetime
from src.citas.models import Cita
from src.medicos.models import Medico
from src.pacientes.models import Paciente

bp_citas = Blueprint('citas', __name__, template_folder='templates')


@bp_citas.route('/')
def index():
    citas = Cita.query.all()
    return render_template('cita/index.html', citas=citas)


@bp_citas.route('/create', methods=['GET', 'POST'])
def create():

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':

        fecha_str = request.form.get('fecha')
        hora_str = request.form.get('hora')
        medico_id = request.form.get('medico_id')
        paciente_id = request.form.get('paciente_id')

        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        hora = datetime.strptime(hora_str, '%H:%M').time()

        cita = Cita(
            fecha=fecha,
            hora=hora,
            medico_id=int(medico_id),
            paciente_id=int(paciente_id)
        )

        db.session.add(cita)
        db.session.commit()

        return redirect(url_for('citas.index'))

    return render_template(
        'cita/create.html',
        medicos=medicos,
        pacientes=pacientes
    )


@bp_citas.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    cita = Cita.query.get_or_404(id)

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':

        fecha_str = request.form.get('fecha')
        hora_str = request.form.get('hora')

        cita.fecha = datetime.strptime(
            fecha_str,
            '%Y-%m-%d'
        ).date()

        cita.hora = datetime.strptime(
            hora_str,
            '%H:%M'
        ).time()

        cita.medico_id = int(
            request.form.get('medico_id')
        )

        cita.paciente_id = int(
            request.form.get('paciente_id')
        )

        db.session.commit()

        return redirect(url_for('citas.index'))

    return render_template(
        'cita/edit.html',
        cita=cita,
        medicos=medicos,
        pacientes=pacientes
    )


@bp_citas.route('/delete/<int:id>')
def delete(id):

    cita = Cita.query.get_or_404(id)

    db.session.delete(cita)
    db.session.commit()

    return redirect(url_for('citas.index'))