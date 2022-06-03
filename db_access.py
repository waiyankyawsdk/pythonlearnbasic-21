import sqlite3

conn = sqlite3.connect("example1.db")
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY, NAME TEXT, SALARY REAL) """)
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,'ABC',80000)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(102,'PQR',70000)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(103,'XYZ',45000)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(104,'RST',30000)")

# conn.execute("COMMIT")

# c.execute(""" SELECT * FROM EMP """)
# print(next(c))
# print(next(c))

# for row in c:
#     print(row)

c.execute(" UPDATE EMP SET SALARY = 65000 WHERE ID=102")
conn.execute("COMMIT")

c.execute("SELECT * FROM EMP WHERE ID = 102")
print(next(c))

c.execute(""" DELETE FROM EMP WHERE ID = 103 """)
conn.execute("COMMIT")

c.execute(""" SELECT * FROM EMP """)
for row in c:
    print(row)