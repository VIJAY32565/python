class college:
    collegename="ADITYA"
    def display(self):
        print("COLLEGE NAME:",self.collegename)
NEON_PINK= "\033[38;5;201;48;5;0m"
PINK="\033[38;5;201m"
RESET="\033[0m"
c=college()
c.display()
print(NEON_PINK +"COLLEGE NAME:"+ RESET , PINK +college.collegename,"UNIVERSITY" + RESET)