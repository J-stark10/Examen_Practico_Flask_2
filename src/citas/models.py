from src.app import db

class Cita(db.Model):
    __tablename__ = 'citas'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)

    paciente = db.relationship('Paciente', back_populates='citas')
    medico = db.relationship('Medico', back_populates='citas')

    def __repr__(self):
        return f'<Cita: {self.fecha} - {self.hora} = Paciente: {self.paciente.nombre} - Médico: {self.medico.nombre}>'
