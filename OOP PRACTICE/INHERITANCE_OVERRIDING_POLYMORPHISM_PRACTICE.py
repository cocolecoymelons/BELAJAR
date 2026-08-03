
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

    def raise_salary(self,amount):
        return amount

class Company(Employees):
    def __init__(self):
        self.Company_Name = "IHI GROUP"
        self.Company_Income = 0
        self.Company_Liability = 1000
        self.Company_Assets = 5000
        self.Company_Expenses = 2100
        self.Company_Revenue = 8000
        self.Salary_Sum = 0

    def get_salary(self,i):
        self.Salary_Sum += i.salary 
        return self.Salary_Sum
    
    def CompanyTotalExpenditures(self):
        total_expenditures = self.Company_Expenses + self.Company_Liability + self.Salary_Sum
        return total_expenditures

    def CompanyAssetsSum(self):
        self.Company_Assets += self.Company_Income
        return self.Company_Assets
    
    def CompanyIncomeCalculate(self):
        self.Company_Income = self.Company_Revenue - (self.CompanyTotalExpenditures())
        return self.Company_Income

    def HighestEmployeeSalary(self,i):
        list_i = [sorted(i, reverse=True)]
        print(f"""
        The highest Salary in {self.Company_Name} is {list_i[0]}
        """)

    def CompanyReport(self):
        print(f"""
               {self.Company_Name} Company Report
        -------------------------------
        Company Revenue         : {self.Company_Revenue}
        Company Expenditures    : {self.CompanyTotalExpenditures()}
        __________________________________+
        Company Income          : {self.CompanyIncomeCalculate()}
        Company Assets          : {self.CompanyAssetsSum()}

        """)



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

Com = Company()
Dev = Developer("Bahlil",30,3500,"Developer",'C++')
Des = Designer("Jokowi",26,3000,"Designer","Adobe Photoshop")
Man = Manager("Prabowo",45,4000,"Manager",'Too Large')
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
                0. Add or Edit Employees Information    
                1. Show Employees
                2. Work
                3. Raise or Lower Salary
                4. Company Report
                5. Edit Company Report Data
                6. Exit
            """)
            if decision == '0':
                decision_EditOrAdd = input("1.Add\n2.Edit?\n ")
                if decision_EditOrAdd == '1':
                    Name, Age, Salary, Role, Extras = input("Insert Name, Age, Salary, Role, Extras(separate with commas): ").split(",")
                    role_for_object = input("Insert Object Name: ")
                    if Role == 'Developer':
                        role_for_object = Developer(Name, int(Age), int(Salary), Role, Extras)
                    elif Role == 'Designer':
                        role_for_object = Developer(Name, int(Age), int(Salary), Role, Extras)
                    elif Role == 'Manager':
                        role_for_object = Developer(Name, int(Age), int(Salary), Role, Extras)
                    employees_available.append(role_for_object)
                    print("Success")

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
                
                add_salary = int(input("Raise or lower amount of salary: "))
                if employees_available[selected_role].salary + add_salary < 0:
                    print("Why not just fire, Boss?")
                    continue
                employees_available[selected_role].salary += add_salary
                print("Sucsess")
            
            elif decision == '4':
                total_employees = len(employees_available)

                print(f"""
                        Company Report
                ----------------------------------
                Total Employees: {total_employees}
                """)

                for i in employees_available:
                    Com.get_salary(i)
                    print(f"""
                        {i.introduce()}
                    """)

                Com.CompanyReport()

            elif decision == '5':
                print("Insert a letter to escape.")

                Com.Company_Income = int(input("Insert Income:"))
                Com.Company_Liability = int(input("Insert Liabilty: "))
                Com.Company_Assets = int(input("Insert Assets: "))
                Com.Company_Expenses = int(input("Insert Expenses: "))
                Com.Company_Revenue = int(input("Insert Revenue: "))

            elif decision == '6':
                print("See you later!")
                break
            else:
                print("Unknown menu!")
        except ValueError:
            print("Please input a number!")
        except IndexError:
            print("Unknown Employees role!")
        