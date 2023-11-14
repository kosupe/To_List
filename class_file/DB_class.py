import sqlite3

class DBClass():
    _con = None
    _cur = None
    
    def _start_db():
        DBClass._con = sqlite3.connect("tutorial.db")
        DBClass._cur = DBClass._con.cursor()
    
    def _fin_db():
        DBClass._cur.close()
    

    def drop_tb():
        DBClass._start_db()
        DBClass._cur.execute("""
        DROP TABLE tasktable;
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    
    def create_tb():
        DBClass._start_db()
        DBClass._cur.execute("""
        CREATE TABLE tasktable(
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            checkflg BOOL NOT NULL
        );
        """)
        DBClass._con.commit()
        DBClass._fin_db()

    def select_all():
        DBClass._start_db()
        res = DBClass._cur.execute("""
        SELECT * FROM tasktable;
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result

    def select_next_id():
        DBClass._start_db()
        res = DBClass._cur.execute("""
        SELECT MAX(id) FROM tasktable GROUPBY;
        """)
        result = res.fetchall()
        max_id = result[0][0]
        DBClass._con.commit()
        DBClass._fin_db()
        return max_id + 1

    def insert(id,task_value,flg):
        DBClass._start_db()
        DBClass._cur.execute(f"""
        INSERT INTO tasktable VALUES({id},'{task_value}',{flg})
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    
    def update_task(task_value,id):
        DBClass._start_db()
        DBClass._cur.execute(f"""
        UPDATE tasktable SET task='{task_value}' WHERE id={id};
        """)
        DBClass._con.commit()
        DBClass._fin_db()

    def update_flg(flg, id):
        DBClass._start_db()
        DBClass._cur.execute(f"""
        UPDATE tasktable SET checkflg={flg} WHERE id={id};
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    
    def delete(id):
        DBClass._start_db()
        DBClass._cur.execute(f"""
        DELETE FROM tasktable WHERE id = {id};
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    

if __name__ == "__main__":
    task_value = "11:30から面接"
    flg = False
    
    
    
    DBClass.update_task(task_value="11:00から面接",id=1)

    tasks = DBClass.select_all()
    print(tasks)