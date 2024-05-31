from db import Database
try:
    class Region:
        table_name = "region"
        def __init__(self, name):
            self.name = name

        @staticmethod
        def select():
            query = f"SELECT * FROM {Region.table_name} ORDER BY id"
            data = Database.connect(query, "select")
            for i in data:
                print(i)

        def insert(self):
            query = f"""
            INSERT INTO region(name) VALUES('{self.name}')
        """
            return Database.connect(query, "insert")

        @staticmethod
        def update(column, new, former, table) -> str:
            if column == "id":
                query = f"UPDATE {table} SET {column} = {new} WHERE {column} = {former}"
            else:
                query = f"UPDATE {table} SET {column} = '{new}' WHERE {column} = '{former}'"
            return Database.connect(query, "update")

        @staticmethod
        def delete(column, data, table):
            if column == "id":
                query = f"DELETE FROM {table} WHERE {column} = {data}"

            else:
                query = f"DELETE FROM {table} WHERE {column} = '{data}'"
            return Database.connect(query, "delete")


    class Filial(Region):
        table_name = "city"
        def __init__(self, name, region_id):
            Region.__init__(self, name)
            self.county_id = region_id

        @staticmethod
        def select():
            query = f"SELECT * FROM {Filial.table_name} ORDER BY id"
            data = Database.connect(query, "select")
            for i in data:
                print(i)




    class Students(Region):
        table_name = "customers"
        def __init__(self, first_name, last_name, username, password):
            self.first_name = first_name
            self.last_name = last_name
            self.password = password
            self.username = username


        @staticmethod
        def select():
            query = f"SELECT * FROM {Students.table_name} ORDER BY id"
            data = Database.connect(query, "select")
            for i in data:
                print(i)

        def insert(self):
            query = f"""
                INSERT INTO customers(first_name, last_name, username, password) 
                VALUES('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}')
            """
            return Database.connect(query, "insert")

        @staticmethod
        def personal_data(username, password):
            query = f"SELECT * FROM {Students.table_name} WHERE username = '{username}' and password = '{password}'"
            return Database.connect(query, "select")




        def insert(self):
            query = f"""
                    INSERT INTO category(name) 
                    VALUES('{self.name}')
                """
            return Database.connect(query, "insert")



        def insert(self):
            query = f"""
               INSERT INTO store(name) VALUES('{self.name}')
           """
            return Database.connect(query, "insert")

    class Courses(Region):
        table_name = "product"

        def __init__(self, title, description, price, count, start_date, end_date,):
            Courses.__init__(self, title)
            self.description = description
            self.price = price
            self.count = count
            self.start_date = start_date
            self.end_date = end_date


        @staticmethod
        def select():
            query = f"SELECT * FROM {Courses.table_name} ORDER BY id"
            data = Database.connect(query, "select")
            for i in data:
                print(i)
        @staticmethod
        def search(name):
            query = f"SELECT * FROM courses WHERE name '%{name}%'"
            return Database.connect(query, "select")
        def insert(self):
            query = f"""
                        INSERT INTO product(name, description, price, count, start_date, end_date) 
                        VALUES('{self.title}', '{self.description}', {self.price}, {self.count}, {self.start_date}', '{self.end_date}')
                    """
            return Database.connect(query, "insert")



except Exception as error:
    print(f"Error!: {error}")

