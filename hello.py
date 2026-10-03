class Department:

    def __init__(self, sections):
        self.sections = sections

    def __add__(self,section):
        return self.sections + section.sections    

    def __str__(self):
        return f"Section: {self.sections}"

    def __len__(self):
        return len(self.sections)

a = Department(10)
b = Department(20)

show = Department(("A", "B", "C", "D", "E"))
print(a + b)

print(len(show))
print(show)

section = Department("A")
print(section
      )
