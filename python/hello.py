class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}  # 과목별 성적을 딕셔너리로 관리

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

# 사용 예제
student1 = Student("Alice", 20)
student1.add_grade("Math", 95)
student1.add_grade("English", 88)

student2 = Student("Bob", 22)
student2.add_grade("Math", 90)
student2.add_grade("English", 92)

# 각 학생의 평균 성적 출력
print(f"{student1.name}'s average grade: {student1.get_average_grade()}")
print(f"{student2.name}'s average grade: {student2.get_average_grade()}")