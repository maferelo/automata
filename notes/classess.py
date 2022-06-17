class SoftwareEngineer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)


eng1 = SoftwareEngineer("John", 25, "Python")
eng1.add_skill("Python")
eng1.add_skill("Java")
eng1.add_skill("C++")
