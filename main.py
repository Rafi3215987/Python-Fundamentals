
student : tuple[tuple[str, str, int, dict[str, int]]]  =(
    (
        "S001", "A", 21,
        {
            "Math" : 85,
            "Science" : 92,
            "English" : 78,
            "History" : 88,
            "Bangla" : 95,

        }
    ),

    (
        "S002", "B", 22,
        {
            "Math" : 83,
            "Science" : 77,
            "English" : 91,
            "History" : 82,
            "Bangla" : 63,

        }
    ),

    (
        "S003", "C", 19,
        {
            "Math" : 98,
            "Science" : 92,
            "English" : 78,
            "History" : 67,
            "Bangla" : 78,

        }
    ),
    (
        "S004", "D", 22,
        {
            "Math" : 77,
            "Science" : 86,
            "English" : 75,
            "History" : 93,
            "Bangla" : 92,
        }
    ),
    (
        "S005", "E", 21,
        {
            "Math" : 83,
            "Science" : 91,
            "English" : 88,
            "History" : 81,
            "Bangla" : 89,

        }
    ),
)



class Student:

    def __init__(self, id: str, name: str, age: int, marks: dict[str, int]):
        self.id = id
        self.name = name
        self.age = age
        self.marks = marks

    def total_obtained_marks(self) -> int:
        sum : int = 0 
        for s in self.marks.values():
            sum += s
        return sum
    
    def calculate_percentage(self, totalmarks : int) -> int:
        return (self.total_obtained_marks() / totalmarks) * 100
    
    def calculate_grade(self) :

        print(f"ID: {self.id}, Name: {self.name}, Average Marks: {percentage}, Grade: ")
        percentage = self.calculate_percentage(500)

        print(percentage)

        if percentage >= 80 :
            print('A')
        elif percentage >= 70 :
            print('B')
        elif percentage >=60 :
            print('C')
        else :
            print('F')


def main():
    
    students : list[Student] = []

    for s in student:
        students.append(s)

    print(students)

    for s in students:
        s.calculate_grade()

main()