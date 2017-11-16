import sqlite3

class Database():
    db = sqlite3.connect('files/dojo.db')
    def __init__(self):
        self.con = self.db.cursor()
    
    # create rooms table
    def create_tables(self):
        """this method to create the necessary tables. 
              if need be to add a new table the create statement will be added here.
                This method will only be run when installing the app for the first time.    
            """
        # create rooms table
        self.con.execute('''CREATE TABLE rooms(
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT
            )''')
            
        # create employees table
        self.con.execute('''CREATE TABLE employees(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            type TEXT,
            need_accomodation BOOLEAN
            )''')
            
        # create allocations table
        self.con.execute('''CREATE TABLE allocations(
            employee_id INTEGER,
            room_id INTEGER,
            FOREIGN KEY(employee_id) REFERENCES employees(id),
            FOREIGN KEY(room_id) REFERENCES rooms(id)
            )''')
        
        self.con.execute('''CREATE TABLE unallocations(
            employee_id INTEGER,
            FOREIGN KEY(employee_id) REFERENCES employees(id)
            )''')
            
    # create allocations tabe
    def insert_room(self,name,type):
        """this method inserts a new record to rooms"""
        self.con.execute("INSERT INTO rooms (name,type) VALUES (?,?)",(name,type))
        
    def insert_employee(self):
        pass
    
    def insert_unallocations(self):
        pass
    
    def insert_allocations(self):
        pass
    
    def db_load(self):
        self.con.execute("INSERT INTO rooms (name,type) VALUES ('RED','Office')")
        
    def read_people(self):
        for row in self.con.execute('SELECT * FROM rooms ORDER BY id'):
            print(row)
        for emp in self.con.execute('SELECT * FROM employees ORDER BY id'):
            print(emp)
            