from task_9_checks import Checks
cks
class Example1(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Example2(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Example3(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Example4(Checks):
    def __init__(self, loc):
        super().__init__(loc)

example1 = Example1("Loc1")
example2 = Example2("Loc2")
example3 = Example3("Loc3")
example4 = Example4("Loc4")

print(example1.check_text())
print(example2.check_text())
print(example3.check_text())
print(example4.check_text())
