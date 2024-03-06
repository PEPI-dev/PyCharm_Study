class Student:     # 학생 정보를 담은 클래스 모델
    def __init__(self,id,name,tel,email,address,regdate):
        self.id = id
        self.name = name
        self.tel = tel
        self.email = email
        self.address = address
        self.regdate = regdate

    def set_id(self,id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_tel(self,tel):
        self.tel = tel

    def get_tel(self):
        return self.tel

    def set_email(self,email):
        self.email = email

    def get_email(self):
        return self.email

    def set_address(self,address):
        self.address = address

    def get_address(self):
        return self.address

class Grade:
    def __init__(self, id, java, python, c, regdate, total=0, average=0):
        self.id = id
        self.java = java
        self.python = python
        self.c = c
        self.regdate = regdate
        self.total = total
        self.average = average

    def set_id(self,id):
        self.id = id

    def get_id(self):
        return self.id

    def set_java(self,java):
        self.java = java

    def get_java(self):
        return self.java

    def set_python(self,python):
        self.python = python

    def get_python(self):
        return self.python

    def set_c(self,c):
        self.c = c

    def get_c(self):
        return self.c

    def get_total(self):
        return self.total

    def get_average(self):
        return self.average