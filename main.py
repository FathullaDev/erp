"""
Imthon savollari
3 ta rol(admin,teacher,student) user klassi boladi user namesi tel nomer emaili boladi login paroli boladi
Admin har doym bolsihi kerak
admin funksiyalari:
1. Teacher qoshihsh ochirish (crud) create read update delete
2. grup crud
3. student crud

Teacher funksiyalari:
1. o'ziga tegshli guruhlar korinishi kerak
2. guruhi o'quchilarini koradi
3. gurhga uyga vazifa beradi

Student fun:
1. uyga vazifasi korinadi
2. bahosi korinadi
uyga vazifa yuklash bolmaydi
"""
class User:
    def __init__(self,name,phone_number,login,parol):
        self.name=name
        self.phone_number=phone_number
        self.login=login
        self.parol=parol
        self.groups=[] # Teacher va studentning guruhlari

class Admin(User):
    def __init__(self, name, phone_number, login, parol):
        super().__init__(name, phone_number, login, parol)
        self.teachers = []
        self.students = []
        self.groups = []

    def open_group(self):
        group_name=input("Group name: ")
        if not self.teachers:
            print("O'qituvchilar yo'q!")
        else:
            print("O'qituvchilar:")
            for i,t in enumerate(self.teachers,start=1):
                print(f"{i}: {t.name}")
            teacher_index=int(input("O'qituvchi raqamini kiriting: "))-1
            if 0 <= teacher_index < len(self.teachers):
                teacher=self.teachers[teacher_index]
                new_group=Group(group_name,teacher)
                self.groups.append(new_group)
                teacher.groups.append(group_name)
                print(f"{group_name} guruhi ochildi!")
            else:
                print("Noto'g'ri tanlov")

    def show_groups(self):
        for i,g in enumerate(self.groups,start=1):
            print(f"{i}. {g.title}")

    def add_teacher(self):
        teacher_name=input("Teacher name: ")
        teacher_phone=input("Teacher phone: ")
        teacher_login=input("Teacher login: ")
        teacher_parol=input("Teacher parol: ")
        new_teacher=Teacher(teacher_name,teacher_phone,teacher_login,teacher_parol)
        self.teachers.append(new_teacher)

    def remove_teacher(self):
        self.show_teachers()
        remove_teacher=None
        teacher_index=int(input("O'qituvchi raqamini kiriting: "))
        for ind, t in enumerate(self.teachers,start=1):
            if ind==teacher_index:
                remove_teacher=t
                break
        self.teachers.remove(remove_teacher)
        print("O'qituvchi olib tashlandi")

    def show_teachers(self):
        for ind,t in enumerate(self.teachers,start=1):
            groups_name=[group for group in t.groups]
            groups=", ".join(groups_name) if groups_name else "Guruhlari yo'q"
            print(f"{ind}.",t.name,"|","Guruhlari:",groups)


    def add_student(self):
        student_name = input("Student name: ")
        student_phone = input("Student phone: ")
        student_login = input("Student login: ")
        student_parol = input("Student parol: ")
        new_student=Student(student_name,student_phone,student_login,student_parol)
        print("Studentni qaysi guruhga qo'shmoqchisiz?")
        self.show_groups()
        group_index=int(input("Guruh raqamini kiriting: "))
        to_group=None
        for i,g, in enumerate(self.groups,start=1):
            if i == group_index:
                to_group=g.title
        group=next((g for g in self.groups if g.title==to_group))

        group.students.append(new_student)
        new_student.groups.append(group)
        print(f"{new_student.name} {group.title} guruhiga qo‘shildi.")



    def remove_student(self):
        print("Guruhlar: ")
        self.show_groups()
        group = None
        group_index = int(input("Guruh raqamini tanlang: "))
        for i, g in enumerate(self.groups, start=1):
            if group_index == i:
                group = g
                break
        if group.students:
            remove_student=None
            for i, s in enumerate(group.students, start=1):
                print(f"{i}. {s.name}")
            student_index=int(input("Talaba raqamini kiriting: "))
            for ind, s in enumerate(self.students, start=1):
                if ind == student_index:
                    remove_student = s
                    break
            group.students.remove(remove_student)
            print("Talaba olib tashlandi")
        else:
            print("Guruhda talabalar yo'q")




    def show_students(self):
        print("Guruhlar: ")
        self.show_groups()
        group=None
        group_index=int(input("Guruh raqamini tanlang: "))
        for i,g in enumerate(self.groups,start=1):
            if group_index==i:
                group=g
                break
        if group.students:
            for i,s in enumerate(group.students,start=1):
                print(f"{i}. {s.name}")
        else:
            print("Guruhda talabalar yo'q")



class Teacher(User):
    def __init__(self, name, phone_number, login, parol):
        super().__init__(name, phone_number, login, parol)

    def show_groups(self): #Teacher o'zini guruhlarini ko'radi
        pass

    def show_students_in_group(self):
        pass


    def give_homework(self):
        pass

    def rating_students(self):
        pass


class Student(User):
    def __init__(self, name, phone_number, login, parol):
        super().__init__(name, phone_number, login, parol)
        self.grades={} #{'Group_title':{'less_title':mark}} studentning darsdagi bahosi

    def show_groups(self):
        pass

    def show_homework(self):
        pass

    def show_grades(self):
        pass



class Group:
    def __init__(self,title,teacher=None):
        self.title=title
        self.teacher=teacher
        self.students=[]    #Guruhdagi studentlar
        self.homeworks=[]    #guruhga berilgan vazifalar

admin=Admin("Admin","+998901234567","admin@gmail.com","admin123")
teacher=Teacher("Fathulla","+998917778899","log@gmail.com","log123")
admin.teachers.append(teacher)
admin.open_group()
