# flask apps
from flask_migrate import Migrate
from flask_restful import Api

# my apps
from app.main import create_app, db
from app.main.resources.employee_resource import (DetailEmployee,
	DetailContract,
	Employee,
	UploadDataset,
	AllEmployees
	)

app = create_app('dev')
app.app_context().push()
db.create_all()

api = Api(app)

# Endpoints definition
api.add_resource(Employee, '/api/employee/', endpoint='employee')
api.add_resource(AllEmployees, '/api/employee/all/<int:page_num>/', endpoint='all_employees')
api.add_resource(DetailContract, '/api/contract/<string:id_user>/', endpoint='detail_contract')
api.add_resource(DetailEmployee, '/api/employee/<string:id_user>/', endpoint='detail_employee')
api.add_resource(UploadDataset, '/api/employee/load-file/', endpoint='upload_data_file')


if __name__ == '__main__':
	app.run()