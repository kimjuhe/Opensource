num=1
searchSt=[]

class student_Info :
    student=[]
    students=[]
    count=1

    def __init__(self):
        self.student = []
        self.count+=1

    def get_Info(self) :
        Major = (input("학과를 입력하세요 : "))
        self.student.append(Major)
        StNum = input("학번을 입력하세요 : ")
        self.student.append(StNum)
        Name = input("이름을 입력하세요 : ")
        self.student.append(Name)
        Korea = int(input("국어 점수를 입력하세요 : "))
        self.student.append(Korea)
        English = int(input("영어 점수를 입력하세요 : "))
        self.student.append(English)
        Math = int(input("수학 점수를 입력하세요 : "))
        self.student.append(Math)
        grade = input("학점을 입력하세요 : ")
        self.student.append(grade)
        self.student.append(Korea + English + Math)
        self.student.append(round((Korea + English + Math) / 3, 2))
        student_Info.students.append(self.student)

def menu_print():
    global num
    print("-----------------")  # 메뉴 출력
    print("1. 데이터 추가")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("0. 종료")
    print("-----------------")
    num = input("원하는 메뉴 : ")

def get_Info():
    name = input("추가할 학생의 이름을 입력하세요 : ")
    name = student_Info()
    name.get_Info()

def search_Std():
    global searchSt
    search = input("검색할 학생의 이름 또는 학번 : ")
    for searchSt in student_Info.students:
        if search in searchSt:  # 학생의 이름 또는 학번이 일치하는 경우를 찾는다.
            print("학과\t학번\t이름\t국어\t영어\t수학\t학점\t총점\t평균")
            for i in range(0, 9):
                print(searchSt[i], end="\t")  # 해당하는 학생의 정보를 출력
    print()

def delete_Std():
    search = input("삭제할 학생의 학번 : ")
    for student_Info.count in range(len(student_Info.students)):  # 학생의 명수에 해당하는 만큼 반복문을 돌린다.
        if search in student_Info.students[student_Info.count]:  # 삭제할 학생의 학번을 찾아서
            del (student_Info.students[student_Info.count])  # 해당하는 학생의 정보를 지운다.
            break

def print_Info():
    student_Info.students.sort(key=lambda students: students[1])  # 학번을 기준으로 정렬한다.
    print("학과\t학번\t이름\t국어\t영어\t수학\t학점\t총점\t평균")
    for i in student_Info.students:  # 학생들의 정보를 출력한다.
        for k in i:
            print(k, end='\t')
        print()

while True:  # 사용자가 종료를 원할 떄 까지 반복
    menu_print()

    if num == "1":  # 사용자에게 학생 정보를 입력 받는다.
        get_Info()

    elif num == "2":
        search_Std()

    elif num == "3":
        delete_Std()

    elif num == "4":
        print_Info()

    else:  # while문을 빠져나와 프로그램을 종료한다.
        break