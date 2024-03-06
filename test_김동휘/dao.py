import MySQLdb
import model

class Dao:
    def __init__(self):
        self.db = None

    def connect(self):
        self.db = MySQLdb.connect('localhost', 'root', '1234', 'student_manager')
        self.cur = self.db.cursor()

    def disconnect(self):
        self.db.close()

    def register(self,student):
        self.connect()
        cur = self.db.cursor()
        sql = 'insert into student (id,student_name,email,tel,address,regdate) values (%s, %s, %s,%s,%s,%s)'
        data = (student.get_id(), student.get_name(), student.get_email(),student.get_tel(),student.get_address(),student.get_regdate())
        cur.execute(sql, data)
        self.db.commit()
        cur.close()
        self.disconnect()
