class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, new_class):
        self.classes.append(new_class)

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        print(f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes")