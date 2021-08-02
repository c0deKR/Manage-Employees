from PyQt5.QtSql import *
from datetime import datetime


class Database:
    is_instantiated = False

    def __init__(self):
        if not Database.is_instantiated:

            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(
                "database/ManageEmployeeDatabase.db")
            self.db.open()
            Database.is_instantiated = True

        else:
            print('has been already created')

    def get_employee_id(slef):

        query = QSqlQuery()
        query.prepare("""SELECT max(id) FROM employee;""")
        query.exec()
        if query.next():
            return query.value(0)

    def insert_employee(self, EmployeeInof):
        query = QSqlQuery()

        query.prepare("""INSERT INTO employee (First_name,last_name,brithday,department_name)
                             VALUES (:fn,:ln,:birthday,:department);""")

        query.bindValue(":fn", EmployeeInof.first_name)
        query.bindValue(":ln", EmployeeInof.last_name)
        query.bindValue(":birthday", EmployeeInof.birthday)
        query.bindValue(":department", EmployeeInof.department)
        query.exec()

        id = self.get_employee_id()

        query.prepare("""INSERT INTO log_position  (employee_id,position,date)
         VALUES (:e_id,:position,:date);
                        """)

        query.bindValue(":e_id", id)
        query.bindValue(":position", EmployeeInof.position)
        query.bindValue(
            ":date", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        query.exec()

        query.prepare("""INSERT INTO log_salary (employee_id,salary,date)
                         VALUES (:e_id,:salary,:date);
                        """)
        query.bindValue(":e_id", id)
        query.bindValue(":salary", EmployeeInof.salary)
        query.bindValue(
            ":date", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        query.exec()

    def get_employee_salary(self, id):
        query = QSqlQuery()
        salary_query_string = """SELECT First_name AS "First name", last_name AS "Last name" , department_name AS "Department" , log_salary.salary
                        AS "Salary",log_salary.date AS "Date" , log_salary.raison AS "Raison"
                        FROM employee,log_salary WHERE employee.id = log_salary.employee_id AND employee.id = :id;  """
        query.prepare(salary_query_string)
        query.bindValue(":id", id)
        query.exec()

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sub_list = []
            for i in range(column_number):
                sub_list.append(query.value(i))
            result_list.append(sub_list)
        return [header_list, result_list]

    def delete_employee(self, id):
        query = QSqlQuery()
        query_string = """DELETE from employee
                        WHERE employee.id ="""
        query_string += str(id) + ';'
        query.exec(query_string)

        query_string = """DELETE from log_position
                        WHERE employee_id ="""
        query_string += str(id) + ';'
        query.exec(query_string)

        query_string = """DELETE from log_salary
                        WHERE employee_id ="""
        query_string += str(id) + ';'
        query.exec(query_string)

    def get_employee_position(self, id):
        query = QSqlQuery()
        position_query_string = """SELECT First_name AS "First name", last_name AS "Last name" , department_name AS "Department" , log_position.position
                                AS "Position",log_position.date AS "Date"
                                FROM employee,log_position WHERE employee.id = log_position.employee_id AND employee.id = :id"""

        query.prepare(position_query_string)
        query.bindValue(":id", id)
        query.exec()

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sub_list = []
            for i in range(column_number):
                sub_list.append(query.value(i))
            result_list.append(sub_list)
        return [header_list, result_list]

    def get_employe_full_info(self, conditions_list):
        query = QSqlQuery()
        query_string = """SELECT employee.id AS "ID" , employee.First_name AS "First Name" ,employee.last_name AS "Last Name",employee.brithday AS "Birthday"
                ,employee.department_name AS "Department Name",log_salary.salary AS "salary" , log_position.position AS "Position"
                FROM employee,log_position,log_salary
                WHERE employee.id = log_position.employee_id AND employee.id = log_salary.employee_id
                AND log_position.date = (SELECT max(date) FROM log_position WHERE employee_id = employee.id)
                AND log_salary.date = (SELECT max(date) FROM log_salary WHERE employee_id = employee.id)  """

        condition_string = ""
        if conditions_list:
            for i in range(len(conditions_list)-1):

                condition_string += conditions_list[i][0]
                condition_string += ' = '
                condition_string += conditions_list[i][1]
                condition_string += ' AND '
            condition_string += conditions_list[len(conditions_list)-1][0]
            condition_string += ' = '
            condition_string += conditions_list[len(conditions_list)-1][1]
            condition_string += ' ; '

            if conditions_list:
                query_string += ' AND  ' + condition_string

        result = query.exec(query_string)

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sub_list = []
            for i in range(column_number):
                sub_list.append(query.value(i))
            result_list.append(sub_list)
        return [header_list, result_list]

    def insert_new_position(self, position_record):
        query = QSqlQuery()
        query_string = """
                    INSERT INTO log_position (employee_id,position,date)
                    VALUES (:em_id,:position,:date)
                     """
        query.prepare(query_string)
        query.bindValue(':em_id', position_record.employee_id)
        query.bindValue(':position', position_record.position)
        query.bindValue(
            ':date', datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        query.exec()

    def insert_new_salary(self, salary_record):
        query = QSqlQuery()
        query_string = """INSERT INTO log_salary (employee_id,salary,date,raison) VALUES 
                            (:em_id,:salary,:date,:raison)
                        """
        query.prepare(query_string)

        query.bindValue(':em_id', salary_record.employee_id)
        query.bindValue(':salary', salary_record.salary)
        query.bindValue(':raison', salary_record.raison)
        query.bindValue(
            ':date', datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        query.exec()

    def get_salary_stats(self):
        result_list = [0, 0, 0]

        query = QSqlQuery()
        query.exec("""SELECT max(salary) from log_salary""")
        if query.next():
            result_list[2] = query.value(0)

        query = QSqlQuery()
        query.exec("""SELECT  avg(salary) from log_salary""")
        if query.next():
            result_list[1] = query.value(0)

        query = QSqlQuery()
        query.exec("""SELECT  min(salary) from log_salary""")
        if query.next():
            result_list[0] = query.value(0)

        return result_list

    def get_total_department_salries(self):
        query = QSqlQuery()

        query.exec("""
                    SELECT employee.department_name , sum(log_salary.salary) FROM employee,log_salary WHERE 
                    log_salary.employee_id = employee.id 
                    GROUP BY employee.department_name
                    """)
        list = []
        while query.next():
            sublist = []
            for i in range(2):
                sublist.append(query.value(i))
            list.append(sublist)
        return list
