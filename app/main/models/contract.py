from .. import db, ma


class Contract(db.Model):
    __tablename__ = 'contract'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    contract_date = db.Column(db.Date(), nullable=True)
    end_date = db.Column(db.Date(), nullable=True)
    driver_license_validity = db.Column(db.Date(), nullable=True)
    id_person = db.Column(
        db.Integer,
        db.ForeignKey('person.id'),
        nullable=False)
    person = db.relationship('Person', backref='contract')

    def __init__(self, code, contract_date, end_date, driver_license_validity, person):
        self.code = code
        self.contract_date = contract_date
        self.end_date = end_date
        self.driver_license_validity = driver_license_validity
        self.person = person

class ContractSchema(ma.SQLAlchemySchema):

    class Meta:
        model=Contract
        include_fk=True

    id=ma.auto_field()
    code = ma.auto_field()
    contract_date=ma.auto_field()
    end_date=ma.auto_field()
    driver_license_validity=ma.auto_field()
    id_person=ma.auto_field()

    
contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)