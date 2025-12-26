from src.repositories.expense_repository import ExpenseRepository
from datetime import datetime

class ExpenseService:
    
    @staticmethod
    def create_expense(data):
        if 'date' in data and isinstance(data['date'], str):
            data['date'] = datetime.fromisoformat(data['date'].replace('Z', '+00:00'))
        
        required_fields = ['title', 'amount', 'category']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        if data['amount'] <= 0:
            raise ValueError("Amount must be greater than 0")
        
        return ExpenseRepository.create(data)
    
    @staticmethod
    def get_all_expenses(filters=None):
        processed_filters = {}
        
        if filters:
            if 'category' in filters:
                processed_filters['category'] = filters['category']
            if 'start_date' in filters:
                processed_filters['start_date'] = datetime.fromisoformat(filters['start_date'].replace('Z', '+00:00'))
            if 'end_date' in filters:
                processed_filters['end_date'] = datetime.fromisoformat(filters['end_date'].replace('Z', '+00:00'))
            if 'min_amount' in filters:
                processed_filters['min_amount'] = float(filters['min_amount'])
            if 'max_amount' in filters:
                processed_filters['max_amount'] = float(filters['max_amount'])
        
        return ExpenseRepository.get_all(processed_filters)
    
    @staticmethod
    def get_expense_by_id(expense_id):
        expense = ExpenseRepository.get_by_id(expense_id)
        if not expense:
            raise ValueError(f"Expense with id {expense_id} not found")
        return expense
    
    @staticmethod
    def update_expense(expense_id, data):
        expense = ExpenseRepository.get_by_id(expense_id)
        if not expense:
            raise ValueError(f"Expense with id {expense_id} not found")
        
        if 'date' in data and isinstance(data['date'], str):
            data['date'] = datetime.fromisoformat(data['date'].replace('Z', '+00:00'))
        
        if 'amount' in data and data['amount'] <= 0:
            raise ValueError("Amount must be greater than 0")
        
        return ExpenseRepository.update(expense_id, data)
    
    @staticmethod
    def delete_expense(expense_id):
        success = ExpenseRepository.delete(expense_id)
        if not success:
            raise ValueError(f"Expense with id {expense_id} not found")
        return success
    
    @staticmethod
    def get_expense_summary():
        total_by_category = ExpenseRepository.get_total_by_category()
        statistics = ExpenseRepository.get_statistics()
        
        return {
            'statistics': statistics,
            'by_category': total_by_category
        }
    
    @staticmethod
    def get_expense_statistics(start_date=None, end_date=None):
        if start_date:
            start_date = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
        if end_date:
            end_date = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
        
        return ExpenseRepository.get_statistics(start_date, end_date)
