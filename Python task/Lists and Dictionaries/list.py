class StudentDatabase:
    def __init__(self):
        self.students = {}

    def create(self, student_id, name, age, grades):
        self.students[student_id] = {"name": name, "age": age, "grades": grades}

    def read(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student ID: {student_id}\nName: {student['name']}\nAge: {student['age']}\nGrades: {student['grades']}")
        else:
            print("Student not found!")

    def update(self, student_id, name=None, age=None, grades=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student["name"] = name
            if age:
                student["age"] = age
            if grades:
                student["grades"] = grades
        else:
            print("Student not found!")

    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            print("Student not found!")

db = StudentDatabase()

db.create(1, "Harsh", 22, [85, 90, 92])
db.create(2, "Rohit", 22, [88, 91, 89])
db.create(3, "Rishabh", 23, [88, 91, 89])

db.read(1)
db.read(3)

db.update(1, age=21, grades=[90, 95, 93])
db.read(1)

db.delete(2)
db.read(2)
