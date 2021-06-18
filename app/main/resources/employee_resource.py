# thrid party apps
from werkzeug.utils import secure_filename

# flask & python apps
from flask import jsonify, request
from flask_restful import Resource

import os

# my apps
from app.main.models.person import Person, person_schema, persons_schema
from app.main.models.contract import Contract, contract_schema, contracts_schema
from app.main import db
from app.main.services.data_cleaner_service import parse_xlsx
from app.main.config import UPLOAD_FILES_FOLDER



class DetailEmployee(Resource):
    """ detalle de empleado """
    def get(self, id_user):
        person=Person.query.filter_by(id=id_user).first()
        res=person_schema.dump(person)
        return jsonify(res)


class DetailContract(Resource):
    """ detalle de contrato"""
    def get(self, id_user):
        id=id_user
        contract=Contract.query.filter_by(id_person=id_user).first()
        res=contract_schema.dump(contract)
        return jsonify(res)


class Employee(Resource):
    
    def post(self):
        """ to create new employee """
        person=Person(
            name=request.json['name'],
            birth_date=request.json['birth_date'],
            naturalization_date=request.json['naturalization_date'],
            gender=request.json['gender']
        )
        contract=Contract(
            code=request.json['code'],
            contract_date=request.json['contract_date'],
            end_date=request.json['end_date'],
            driver_license_validity=request.json['driver_license_validity'],
            person=person
        )
        db.session.add(person)
        db.session.add(contract)
        db.session.commit()
        print('ok session')
        person_schema.dump(person)
        return person_schema.jsonify(person)


class AllEmployees(Resource):

    def get(self, page_num):
        """ to get all employees by pagination """
        per_page=15
        persons=Person.query.paginate(per_page=per_page, page=page_num, error_out=True)
        result = persons_schema.dump(persons.items)
        response={
            'objects per page':per_page,
            'total pages':persons.pages,
            'current page':persons.page,
            'next':persons.next_num,
            'previous':persons.prev_num,
            'objects':result
        }
        return jsonify(response)
    

class UploadDataset(Resource):

    def post(self):
        """ To save dataset into db """
        if 'file' not in request.files:
            return {'message': 'no file recived'}
        file=request.files['file']
        if file.filename == '' or not file:
            return {'message': 'file no valid'}
        filename=secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FILES_FOLDER, 'data.xlsx'))
        print('- file "{}" recived, reading...'.format(filename))
        df = parse_xlsx(os.path.join(UPLOAD_FILES_FOLDER, 'data.xlsx'))
        print('- file "{}" prepare migration...'.format(filename))
        employees=[]
        for index, row in df.iterrows():
            name = row['name']
            birth_date = row['birth_date']
            naturalization_date = row['naturalization_date']
            gender = row['gender']
            code = row['code']
            contract_date = row['contract_date']
            end_date = row['end_date']
            driver_license_validity = row['driver_license_validity']
            person=Person(
                name=name,
                birth_date=birth_date,
                naturalization_date=naturalization_date,
                gender=gender
            )
            contract=Contract(
                code=code,
                contract_date=contract_date,
                end_date=end_date,
                driver_license_validity=driver_license_validity,
                person=person
            )
            employees.append(contract)
        db.session.add_all(employees)
        # "bulk_save_objects" is too low level api to this case with relationships
        print('- commiting...')
        db.session.commit()
        print('ok')
        return {'message': 'file saved and uploaded succesfully!'}