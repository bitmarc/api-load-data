from .. import db, ma


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    birth_date = db.Column(db.Date())
    naturalization_date = db.Column(db.Date(), nullable=True)
    gender = db.Column(db.String(6))
    
    def __init__(self, name, birth_date, naturalization_date, gender):
        self.name = name
        self.birth_date = birth_date
        self.naturalization_date = naturalization_date
        self.gender = gender


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Person
    
    id = ma.auto_field()
    name=ma.auto_field()
    birth_date = ma.auto_field()
    naturalization_date = ma.auto_field()
    gender = ma.auto_field()
    #contract = ma.auto_field()
    contract = ma.List(ma.HyperlinkRelated("detail_contract",url_key='id_user'))


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
