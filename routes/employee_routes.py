from flask import Blueprint, request, jsonify
from models.employee import db, Employee

employee_bp = Blueprint('employee_bp', __name__)

# ------------------ CREATE EMPLOYEE (POST) ------------------
@employee_bp.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    name = data.get('name')
    email = data.get('email')
    salary = data.get('salary')

    if not name or not email or not salary:
        return jsonify({"error": "Name, email and salary are required"}), 400

    # Check if email already exists
    if Employee.query.filter_by(email=email).first():
        return jsonify({"error": "Employee with this email already exists"}), 409

    employee = Employee(name=name, email=email, salary=salary)

    db.session.add(employee)
    db.session.commit()

    return jsonify({
        "message": "Employee added successfully",
        "employee": {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "salary": employee.salary
        }
    }), 201


# ------------------ GET ALL EMPLOYEES (GET) ------------------
@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()

    return jsonify([
        {
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "salary": emp.salary
        } for emp in employees
    ]), 200


# ------------------ GET EMPLOYEE BY ID (GET) ------------------
@employee_bp.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({
        "id": employee.id,
        "name": employee.name,
        "email": employee.email,
        "salary": employee.salary
    }), 200


# ------------------ UPDATE EMPLOYEE (PATCH) ------------------
@employee_bp.route('/employees/<int:employee_id>', methods=['PATCH'])
def update_employee_patch(employee_id):
    employee = Employee.query.get(employee_id)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    if 'name' in data:
        employee.name = data['name']

    if 'email' in data:
        existing = Employee.query.filter_by(email=data['email']).first()
        if existing and existing.id != employee_id:
            return jsonify({"error": "Email already in use"}), 409
        employee.email = data['email']

    if 'salary' in data:
        employee.salary = data['salary']

    db.session.commit()

    return jsonify({
        "message": "Employee updated successfully (PATCH)",
        "employee": {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "salary": employee.salary
        }
    }), 200


# ------------------ UPDATE EMPLOYEE (PUT) ------------------
@employee_bp.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee_put(employee_id):
    employee = Employee.query.get(employee_id)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    name = data.get('name')
    email = data.get('email')
    salary = data.get('salary')

    if not name or not email or not salary:
        return jsonify({"error": "Name, email and salary are required"}), 400

    existing = Employee.query.filter_by(email=email).first()
    if existing and existing.id != employee_id:
        return jsonify({"error": "Employee with this email already exists"}), 409

    employee.name = name
    employee.email = email
    employee.salary = salary

    db.session.commit()

    return jsonify({
        "message": "Employee updated successfully (PUT)",
        "employee": {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "salary": employee.salary
        }
    }), 200


# ------------------ DELETE EMPLOYEE (DELETE) ------------------
@employee_bp.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()

    return jsonify({"message": "Employee deleted successfully"}), 200
