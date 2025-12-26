from flask import request, jsonify
from src.services.expense_service import ExpenseService

class ExpenseController:
    
    @staticmethod
    def create_expense():
        try:
            data = request.get_json()
            expense = ExpenseService.create_expense(data)
            return jsonify({
                'success': True,
                'message': 'Expense created successfully',
                'data': expense.to_dict()
            }), 201
        except ValueError as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400
        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'Internal server error',
                'error': str(e)
            }), 500
    
    @staticmethod
    def get_all_expenses():
        try:
            filters = {
                'category': request.args.get('category'),
                'start_date': request.args.get('start_date'),
                'end_date': request.args.get('end_date'),
                'min_amount': request.args.get('min_amount'),
                'max_amount': request.args.get('max_amount')
            }
            filters = {k: v for k, v in filters.items() if v is not None}
            
            expenses = ExpenseService.get_all_expenses(filters)
            return jsonify({
                'success': True,
                'count': len(expenses),
                'data': [expense.to_dict() for expense in expenses]
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'Internal server error',
                'error': str(e)
            }), 500
    
    @staticmethod
    def get_expense_by_id(expense_id):
        try:
            expense = ExpenseService.get_expense_by_id(expense_id)
            return jsonify({
                'success': True,
                'data': expense.to_dict()
            }), 200
        except ValueError as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 404
        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'Internal server error',
                'error': str(e)
            }), 500
    
    @staticmethod
    def update_expense(expense_id):
        try:
            data = request.get_json()
            expense = ExpenseService.update_expense(expense_id, data)
            return jsonify({
                'success': True,
                'message': 'Expense updated successfully',
                'data': expense.to_dict()
            }), 200
        except ValueError as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 404
        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'Internal server error',
                'error': str(e)
            }), 500
    
    @staticmethod
    def delete_expense(expense_id):
        try:
            ExpenseService.delete_expense(expense_id)
            return jsonify({
                'success': True,
                'message': 'Expense deleted successfully'
            }), 200
        except ValueError as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 404
        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'Internal server error',
                'error': str(e)
            }), 500
    
    @staticmethod
    def get_expense_summary():
        try:
            summary = ExpenseService.get_expense_summary()
            return jsonify({
                'success': True,
                'data': summary
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'Internal server error',
                'error': str(e)
            }), 500
    
    @staticmethod
    def get_expense_statistics():
        try:
            start_date = request.args.get('start_date')
            end_date = request.args.get('end_date')
            
            statistics = ExpenseService.get_expense_statistics(start_date, end_date)
            return jsonify({
                'success': True,
                'data': statistics
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': 'Internal server error',
                'error': str(e)
            }), 500
