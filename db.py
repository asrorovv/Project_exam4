import psycopg2 as psql

try:
    class Database:
        @staticmethod
        def connect(query: str, query_type: str):
            db = psql.connect(
                database='exam4',
                user='postgres',
                password='muhammad0077',
                host='localhost',
                port='5432'
            )

            cursor = db.cursor()
            cursor.execute(query)
            data = ['create', 'delete', 'update', "insert", 'alter']
            if query_type in data:
                db.commit()
            else:
                return cursor.fetchall()


    class Check:
        @staticmethod
        def check(username: str, password: str):
            try:
                query = f"SELECT * FROM customers WHERE username = '{username}' and password = '{password}'"
                data = Database.connect(query, "select")
                if len(data) == 1:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error: {e}")


    def add_column():
        query = f"""
            INSERT INTO customers(first_name, last_name, username, password, birth_date) 
            VALUES('Jack', 'Martins', 'Jackson', 'Jack00', '2004-09-12')"""
        return Database.connect(query, "insert")
    def insert_column():
        query = f"""
            INSERT INTO product(title, description, price, count, start_date, end_date) VALUES('Samsung', 's24 ultra', 1200, 30, 23432, '2024-02-28', '2025-03-01', 34, 12)"""
        return Database.connect(query, 'insert')

except Exception as e:
    print(f"Error!: {e}")




if __name__ == "__main__":
    print()


