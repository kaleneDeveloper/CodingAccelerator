import sqlite3 

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees
(
    Name text,
    LastName text,
    Salary int
)        
""")

# d = {"name": "Paul", "lastName": "Duconp", "salary": 20000}
# c.execute("INSERT INTO employees VALUES (:name, :lastName, :salary)", d)

# d = {"salary": 25000, "name": "Paul", "lastName": "Duconp"}

# c.execute("UPDATE employees SET Salary=:salary WHERE Name=:name AND LastName=:lastName", d)

c.execute("DELETE FROM employees WHERE name='Paul'")

d = {"a": "Paul" and "test"}
c.execute("SELECT * FROM employees WHERE name=:a", d)
data = c.fetchall()
print(data)
print(type(type))
conn.commit()
conn.close()   

