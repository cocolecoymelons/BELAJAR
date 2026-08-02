
class Employees:
    def __init__(self,name,age,salary,role):
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
    def introduce(self):

        print(f"""
            {self.name}
        ------------------------      
        Age     : {self.age}
        Salary  : {self.salary}
        
        Work as a {self.role}.
""")
    def work(self):
        pass

    def get_salary(self):
        pass

    def raise_salary(self,amount):
        return amount


class Developer(Employees):
    def __init__(self,name,age,salary,role,language):
        super().__init__(name,age,salary,role)
        self.language = language
        pass

    def work(self):
        print(f"Developing API requests on {self.language}...")
        self.debug()

    def debug(self):
        print("Fixing program errors...")

class Designer(Employees):
    def __init__(self,name,age,salary,role,software):
        super().__init__(name,age,salary,role)
        self.software = software
        pass
        
    def work(self):
        print("Working one UI designs flow...")
        self.design()

    def design(self):
        print(f"Designing UI with {self.software}...")
        

class Manager(Employees):
    def __init__(self,name,age,salary,role,team_size):
        super().__init__(name,age,salary,role)
        self.team_size = team_size
        pass

    def work(self):
        print("Managing employees and projects..")
        self.meeting()

    def meeting(self):
        print(f"Have a meeting with {self.team_size} team.")

Dev = Developer("DAVID",30,3500,"Developer",'C++')
Des = Designer("ALICE",26,3000,"Designer","Adobe Photoshop")
Man = Manager("REGGY",45,4000,"Manager",'Too Large')
employees_available = [
    Dev,
    Des,
    Man
]

while True:
    # for i in employees_available:
        try:
            decision = input("""
                --------MENU--------
                0. Edit Employees Information    
                1. Show Employees
                2. Work
                3. Raise Salary
                4. Company Report
                5. Exit
            """)
            if decision == '0':
                print("Coming soon.")

            elif decision == '1':
                for i in employees_available:
                    i.introduce()

            elif decision == '2':
                for i in employees_available:
                    i.work()

            elif decision == '3':
                selected_role = int(input("0. Developer\n1. Designer\n2. Manager\n"))
                if selected_role < 0 or selected_role > len(employees_available) - 1:
                    raise IndexError
                add_salary = int(input("Raise amount of salary: "))
                employees_available[selected_role].salary += add_salary
                print("Sucsess")
            
            elif decision == '4':
                print("Coming soon.")

            elif decision == '5':
                print("See you later!")
                break
            else:
                print("Unknown menu!")
        except ValueError:
            print("Please input a number!")
        except IndexError:
            print("Unknown Employees role!")
        