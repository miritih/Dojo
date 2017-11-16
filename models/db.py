import sqlite3

class Database():
    db = sqlite3.connect('files/dojo.sqlite')
    def __init__(self):
        self.con = self.db.cursor()
    
    # create rooms table
    def create_tables(self):
        """this method to create the necessary tables. 
              if need be to add a new table the create statement will be added here.
                This method will only be run when installing the app for the first time.    
            """
        # create rooms table
        self.con.execute('''CREATE TABLE IF NOT EXISTS rooms(
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT
            )''')
            
        # create employees table
        self.con.execute('''CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            type TEXT,
            need_accomodation BOOLEAN
            )''')
            
        # create allocations table
        self.con.execute('''CREATE TABLE IF NOT EXISTS allocations(
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            room_id INTEGER,
            FOREIGN KEY(employee_id) REFERENCES employees(id),
            FOREIGN KEY(room_id) REFERENCES rooms(id)
            )''')
        
        self.con.execute('''CREATE TABLE IF NOT EXISTS unallocations(
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            FOREIGN KEY(employee_id) REFERENCES employees(id)
            )''')
            
    # create allocations tabe
    def insert_room(self,name,type_):
        """this method inserts a new record to rooms"""
        self.con.execute("INSERT INTO rooms (name,type) VALUES (?,?)",(name,type_))
        self.db.commit()
    
    def insert_employee(self,fname,lname,type_,need_accomodation):
        """This method creates a new employee. inserts to employee table"""
        self.con.execute("INSERT INTO employees (first_name,last_name,type,need_accomodation) VALUES (?,?,?,?)",(fname,lname,type_,need_accomodation))
        self.db.commit()
    
    def insert_unallocations(self,userid):
        """ inserts into unallocations"""
        self.con.execute("INSERT INTO unallocations (employee_id) VALUES (?)",(userid))
        self.db.commit()
    
    def insert_allocations(self,userid,roomid):
        """Inserts into allocations"""
        self.con.execute("INSERT INTO allocations (employee_id,room_id) VALUES (?,?)",(userid,roomid))
        self.db.commit()
    
    def read_people(self):
        for row in self.con.execute('SELECT * FROM rooms ORDER BY id'):
            print(row)
        for emp in self.con.execute('SELECT * FROM employees ORDER BY id'):
            print(emp)
            
app=Database()
app.create_tables()
# app.insert_room('RED',"Office")
# app.insert_employee('mwenda','eric','Staff', 1)
app.read_people()
