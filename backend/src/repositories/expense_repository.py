from src.models.expense import Expense, db
from datetime import datetime

class ExpenseRepository:
    
    @staticmethod
    def create(expense_data):
        expense = Expense(**expense_data)
        db.session.add(expense)
        db.session.commit()
        return expense
    
    @staticmethod
    def get_all(filters=None):
        query = Expense.query
        
        if filters:
            if 'category' in filters:
                query = query.filter_by(category=filters['category'])
            if 'start_date' in filters:
                query = query.filter(Expense.date >= filters['start_date'])
            if 'end_date' in filters:
                query = query.filter(Expense.date <= filters['end_date'])
            if 'min_amount' in filters:
                query = query.filter(Expense.amount >= filters['min_amount'])
            if 'max_amount' in filters:
                query = query.filter(Expense.amount <= filters['max_amount'])
        
        return query.order_by(Expense.date.desc()).all()
    
    @staticmethod
    def get_by_id(expense_id):
        return Expense.query.get(expense_id)
    
    @staticmethod
    def update(expense_id, expense_data):
        expense = Expense.query.get(expense_id)
        if expense:
            for key, value in expense_data.items():
                setattr(expense, key, value)
            expense.updated_at = datetime.utcnow()
            db.session.commit()
        return expense
    
    @staticmethod
    def delete(expense_id):
        expense = Expense.query.get(expense_id)
        if expense:
            db.session.delete(expense)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_total_by_category():
        from sqlalchemy import func
        result = db.session.query(
            Expense.category,
            func.sum(Expense.amount).label('total')
        ).group_by(Expense.category).all()
        
        return [{'category': r.category, 'total': float(r.total)} for r in result]
    
    @staticmethod
    def get_statistics(start_date=None, end_date=None):
        from sqlalchemy import func
        query = db.session.query(
            func.sum(Expense.amount).label('total'),
            func.avg(Expense.amount).label('average'),
            func.count(Expense.id).label('count')
        )
        
        if start_date:
            query = query.filter(Expense.date >= start_date)
        if end_date:
            query = query.filter(Expense.date <= end_date)
        
        result = query.first()
        
        return {
            'total': float(result.total) if result.total else 0,
            'average': float(result.average) if result.average else 0,
            'count': result.count if result.count else 0
        }
