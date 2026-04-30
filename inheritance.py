NEON_PINK= "\033[38;5;201;48;5;0m"
NEON_RED="\033[38;5;196;48;5;0m"
PINK="\033[38;5;201m"
BLUE="\033[38;5;27m"
RESET="\033[0m"
class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def works(self):
        print( BLUE + "employees do the work" + RESET)
class manager(employee):
    def works(self):
        print(BLUE + self.name + RESET ,NEON_RED +"managers manage the team" + RESET)
class tester(employee):
    def works(self):
        print(NEON_PINK + self.name + RESET ,NEON_RED+ "testers test the software" + RESET)
def employee_details(emp):
    emp.works()
m=manager("john", 101)
t=tester("alice", 102)
employee_details(m)
employee_details(t)