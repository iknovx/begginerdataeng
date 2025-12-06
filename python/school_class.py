import random
class SchoolClasses:
    def __init__ (self, class_name, teacher, students_count):
        self.class_name = class_name
        self.teacher = teacher
        self.students_count = students_count
    def class_info(self):
        self.class_name = ['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D']
        self.teacher = ["Mr. Smith", "Ms. Johnson", "Mrs. Lee", "Mr. Brown", "Ms. Davis", "Mr. Wilson", "Mrs. Taylor", "Ms. Anderson"]
        self.students_count = [25, 30, 28, 27, 26, 29, 24, 31]
        
        random. shuffle(self.teacher)
        random. shuffle(self.students_count)
        
        classes = list(zip(self.class_name, self.teacher, self.students_count))
        classes.sort(key = lambda x: (int(x[0][0]), x[0][1]))  # Sort by class name

        for class_name, teacher, students_count in classes:
            class_info = f"Class: {class_name}, Teacher: {teacher}, Students: {students_count}"
            print(class_info)