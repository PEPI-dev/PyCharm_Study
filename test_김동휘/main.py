import MySQLdb
import model
import dao

class Service:
    def __init__(self):
        self.dao = dao.Dao()

    def register_service(self):
        name = input('이름 : ')
        tel =  input('연락처 : ')
        email = input('email : ')
        address = input('주소 : ')

        student = model.Student(id,name,tel,email,address)
        self.dao.insert(student)