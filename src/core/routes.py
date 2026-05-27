from flask import render_template, Blueprint

from src.citas.models import Cita
from src.pacientes.models import Paciente
from src.medicos.models import Medico

bp_core = Blueprint('core', __name__, template_folder='templates')

@bp_core.route('/')
def index():

    total_pacientes = Paciente.query.count()
    total_medicos = Medico.query.count()
    total_citas = Cita.query.count()

    return render_template('core/index.html', total_pacientes=total_pacientes, total_medicos=total_medicos, total_citas=total_citas)