import mysql.connector
import logging
from contextlib import contextmanager
from logging_setup import setup_logger
from dotenv import load_dotenv
load_dotenv()

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
    
         host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
        
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()
    
def fetch_expenses_for_date(expense_date):  
    logger.info(f'fetch_expenses_for_date called with {expense_date}')
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses
    
def delete_expenses_for_date(expense_date):
    logger.info(f'delete_expenses_for_date called with {expense_date}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date = %s",(expense_date,))
        
def insert_expenses_for_date(expense_date, amount, category, notes):
    logger.info(f'insert_expenses_for_date called with {expense_date}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "insert into expenses (expense_date,amount, category, notes) values (%s,%s,%s,%s)",
            (expense_date, amount, category, notes)
            )
        

def fetch_expense_summary(start_date,end_date):
    logger.info(f'fetch_expenses_for_date called with start:{start_date} and end:{end_date}')
    with get_db_cursor() as cursor:
        cursor.execute(
            '''select category, sum(amount) as total from expenses where expense_date
            between %s and %s group by category''',(start_date,end_date))
        data=cursor.fetchall()
        return data
        
    
   
# if __name__ == '__main__':
#     expenses = insert_expenses_for_date('2025-08-01',40,"Food",'ate tast samosa')
#     print(expenses) 