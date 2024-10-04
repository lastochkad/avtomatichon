from sqlalchemy import create_engine
from sqlalchemy.sql import text 
db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
db = create_engine(db_connection_string)

def test_db_connection():
    db = create_engine(db_connection_string)
    name = db.table_names()
    assert name[0] == 'app_users'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]
    assert row1["id"] == 5470
    assert row1["name"] == "Chamomile"

def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 5470).fetchall()
    assert len(rows) == 0

def test_db_connection():
    name = db.table_names()
    assert name[0] == 'company'    

