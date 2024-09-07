"""
### OOP
The program is written as a collection of classes and object which are meant for communication. 
The smallest and basic entity is object and all kind of computation is performed on the objects only. 
More emphasis is on data rather procedure. It can handle almost all kind of real life problems which are today in scenario.

### Advantages
1. Data security 
2. Inheritance
3. Code reusability
4. Flexible and abstraction is also present 
"""

class Signup:
    def __init__(self):
        self.userid = 0
        self.name = ""
        self.emailid = ""
        self.sex = ""
        self.mob = 0

    def create(self, userid, name, emailid, sex, mob):
        print("Welcome to GeeksforGeeks\nLets create your account\n")
        self.userid = 132
        self.name = "Radha"
        self.emailid = "radha.89@gmail.com"
        self.sex = 'F'
        self.mob = 900558981
        print("your account has been created")


if __name__ == "__main__":
    print("GfG!")
    s1 = Signup()
    s1.create(22, "riya", "riya2@gmail.com", 'F', 89002)

"""Output 
GfG!
Welcome to GeeksforGeeks
Lets create your account

your account has been created
"""