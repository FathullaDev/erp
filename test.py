# ==== Base Classes ====
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.groups = []


class Group:
    def __init__(self, name, teacher=None):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.homeworks = []


# ==== Role Classes ====
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def create_teacher(self, teachers_list):
        username = input("Yangi teacher username: ")
        password = input("Parol: ")
        teacher = Teacher(username, password)
        teachers_list.append(teacher)
        print(f"Teacher {username} qo'shildi.")

    def create_student(self, students_list):
        username = input("Yangi student username: ")
        password = input("Parol: ")
        student = Student(username, password)
        students_list.append(student)
        print(f"Student {username} qo'shildi.")

    def create_group(self, groups_list, teachers_list):
        name = input("Guruh nomi: ")
        print("O'qituvchilar:")
        for i, t in enumerate(teachers_list):
            print(f"{i+1}. {t.username}")
        teacher_index = int(input("O'qituvchi raqamini kiriting: ")) - 1
        if 0 <= teacher_index < len(teachers_list):
            teacher = teachers_list[teacher_index]
            group = Group(name, teacher)
            groups_list.append(group)
            teacher.groups.append(group)
            print(f"Guruh {name} yaratildi.")
        else:
            print("Xato: noto‘g‘ri raqam.")

    def add_student_to_group(self, students_list, groups_list):
        print("Talabalar:")
        for i, s in enumerate(students_list):
            print(f"{i+1}. {s.username}")
        student_index = int(input("Talaba raqamini kiriting: ")) - 1

        print("Guruhlar:")
        for i, g in enumerate(groups_list):
            print(f"{i+1}. {g.name}")
        group_index = int(input("Guruh raqamini kiriting: ")) - 1

        if 0 <= student_index < len(students_list) and 0 <= group_index < len(groups_list):
            student = students_list[student_index]
            group = groups_list[group_index]
            group.students.append(student)
            student.groups.append(group)
            print(f"{student.username} {group.name} guruhiga qo‘shildi.")
        else:
            print("Xato: noto‘g‘ri tanlov.")


class Teacher(User):
    def __init__(self, username, password):
        super().__init__(username, password, "teacher")

    def view_groups(self):
        if not self.groups:
            print("Sizda guruh yo‘q.")
        for g in self.groups:
            print(f"- {g.name}")

    def view_students_in_group(self):
        self.view_groups()
        group_name = input("Qaysi guruhdagi talabalarni ko‘rmoqchisiz: ")
        for g in self.groups:
            if g.name == group_name:
                if not g.students:
                    print("Bu guruhda talaba yo‘q.")
                for s in g.students:
                    print(f"- {s.username}")

    def give_homework(self):
        self.view_groups()
        group_name = input("Qaysi guruhga vazifa berasiz: ")
        for g in self.groups:
            if g.name == group_name:
                hw = input("Uyga vazifa: ")
                g.homeworks.append(hw)
                print(f"{group_name} guruhiga vazifa qo‘shildi.")


class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password, "student")

    def view_homeworks(self):
        for g in self.groups:
            print(f"{g.name} guruh vazifalari:")
            for hw in g.homeworks:
                print(f"  - {hw}")

    def view_grades(self):
        print("Baholar funksiyasi hali yozilmagan.")


# ==== Auth System ====
def login(users_list):
    username = input("Login: ")
    password = input("Parol: ")
    for u in users_list:
        if u.username == username and u.password == password:
            print(f"{u.role.title()} sifatida kirdingiz.")
            return u
    print("Login yoki parol xato!")
    return None


# ==== Main ====
if __name__ == "__main__":
    # Dastlabki foydalanuvchilar
    admin1 = Admin("admin", "123")
    teacher1 = Teacher("teacher", "111")
    student1 = Student("student", "000")

    users = [admin1, teacher1, student1]
    teachers = [teacher1]
    students = [student1]
    groups = []

    while True:
        print("\n=== Tizimga kirish ===")
        user = login(users)
        if not user:
            continue

        if user.role == "admin":
            while True:
                print("\n--- Admin menyu ---")
                print("1. Teacher qo‘shish")
                print("2. Student qo‘shish")
                print("3. Guruh yaratish")
                print("4. Studentni guruhga qo‘shish")
                print("0. Chiqish")
                choice = input("Tanlang: ")
                if choice == "1":
                    user.create_teacher(teachers)
                    users.extend(teachers)
                elif choice == "2":
                    user.create_student(students)
                    users.extend(students)
                elif choice == "3":
                    user.create_group(groups, teachers)
                elif choice == "4":
                    user.add_student_to_group(students, groups)
                elif choice == "0":
                    break

        elif user.role == "teacher":
            while True:
                print("\n--- Teacher menyu ---")
                print("1. Guruhlarni ko‘rish")
                print("2. Guruhdagi talabalarni ko‘rish")
                print("3. Uyga vazifa berish")
                print("0. Chiqish")
                choice = input("Tanlang: ")
                if choice == "1":
                    user.view_groups()
                elif choice == "2":
                    user.view_students_in_group()
                elif choice == "3":
                    user.give_homework()
                elif choice == "0":
                    break

        elif user.role == "student":
            while True:
                print("\n--- Student menyu ---")
                print("1. Uyga vazifani ko‘rish")
                print("2. Baholarni ko‘rish")
                print("0. Chiqish")
                choice = input("Tanlang: ")
                if choice == "1":
                    user.view_homeworks()
                elif choice == "2":
                    user.view_grades()
                elif choice == "0":
                    break
