from flask import Blueprint
from src.controllers.expense_controller import ExpenseController

api = Blueprint('api', __name__, url_prefix='/api/expenses')

@api.route('/', methods=['POST'])
def create_expense():
    return ExpenseController.create_expense()

@api.route('/', methods=['GET'])
def get_all_expenses():
    return ExpenseController.get_all_expenses()

@api.route('/<int:expense_id>', methods=['GET'])
def get_expense_by_id(expense_id):
    return ExpenseController.get_expense_by_id(expense_id)

@api.route('/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    return ExpenseController.update_expense(expense_id)

@api.route('/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    return ExpenseController.delete_expense(expense_id)

@api.route('/summary', methods=['GET'])
def get_expense_summary():
    return ExpenseController.get_expense_summary()

@api.route('/statistics', methods=['GET'])
def get_expense_statistics():
    return ExpenseController.get_expense_statistics()
