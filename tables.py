from db import Database

def tables():
    region = f"""
        CREATE TABLE country(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            date TIMESTAMP DEFAULT now());"""

    filial = f"""
            CREATE TABLE city(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                county_id INT REFERENCES country(id),
                date TIMESTAMP DEFAULT now());"""

    address = f"""
            CREATE TABLE address(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                city_id INT REFERENCES city(id),
                create_date TIMESTAMP DEFAULT now());"""

    students = f"""
               CREATE TABLE customers(
                   id SERIAL PRIMARY KEY,
                   first_name VARCHAR(50),
                   last_name VARCHAR(50),
                   birth_date DATE,
                   date TIMESTAMP DEFAULT now());"""

    category = f"""
            CREATE TABLE category(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                create_date TIMESTAMP DEFAULT now());"""

    store = f"""
                CREATE TABLE store(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    create_date TIMESTAMP DEFAULT now());"""

    courses = f"""
                CREATE TABLE product(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    description TEXT,
                    price NUMERIC,
                    count INTEGER,
                    serial_number INTEGER,
                    start_date DATE,
                    end_date DATE,
                    store_id INT REFERENCES store(id),
                    category_id INT REFERENCES category(id),
                    create_date TIMESTAMP DEFAULT now());"""

    data = {
            "region": region,
            "filial": filial,
            "address": address,
            "students": students,
            "category": category,
            "store": store,
            "courses": courses}
    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")

if __name__ == "__main__":
    tables()


