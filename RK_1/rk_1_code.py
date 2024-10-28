# классы данных
class Department:
    def __init__(self, dep_id: int, name: str):
        self.dep_id = dep_id
        self.name = name

    def __repr__(self):
        return f"Department(ID={self.dep_id}, Name={self.name})"


class Teacher:
    def __init__(self, teacher_id: int, full_name: str, groups: list, departments: list):
        self.teacher_id = teacher_id
        self.full_name = full_name
        self.groups = groups
        self.departments = departments

    def __repr__(self):
        return f"Teacher(ID={self.teacher_id}, Name={self.full_name}, Groups={self.groups}, Departments={self.departments})"


class Department_Teacher:
    def __init__(self, dep_id: int, teacher_id: int):
        self.dep_id = dep_id
        self.teacher_id = teacher_id

    def __repr__(self):
        return f"DepartmentTeacher(DepartmentID={self.dep_id}, TeacherID={self.teacher_id})"


# тестовые данные
departments = [
    Department(1, "ГЗ"),
    Department(2, "А_УЛК"),
    Department(3, "Э"),
    Department(4, "ХИМЛАБ"),
    Department(5, "А_Новый")
]

teachers = [
    Teacher(1, "Иванов Иван Иванович", ["ИУ5-35Б", "ИУ6-35Б"], [1, 3, 5]),
    Teacher(2, "Петров Петр Петрович", ["ИУ5-35Б", "ИУ5-34Б", "ИУ5-33Б", "ИУ5-32Б", ], [1, 2, 4]),
    Teacher(3, "Сидоров Сидор Сидорович", ["ИУ5-34Б", "ИУ5-33Б", "ИУ5-32Б", ], [1, 4, 5]),
    Teacher(4, "Кузнецов Алексей Павлович", ["ИУ6-35Б", "ИУ6-34Б", "ИУ6-33Б", "ИУ6-32Б", "ИУ6-31Б"], [1, 4]),
    Teacher(5, "Смирнов Николай Александрович", ["ИУ5-35Б"], [1, 2, 5, 4])
]

department_teachers = []
for teacher in teachers:
    for dep_id in teacher.departments:
        department_teachers.append(Department_Teacher(dep_id, teacher.teacher_id))


# Запрос 1: Вывести все отделы, у которых название начинается с буквы "А", и работающих в них преподавателей
departments_with_a = [d for d in departments if d.name[0] == "А"]
result_1 = {
    dep.name: [t for t in teachers if dep.dep_id in t.departments]
    for dep in departments_with_a
}

print("\nЗапрос 1: Отделы с названием на 'А' и работающие преподаватели:")
for dep, t_list in result_1.items():
    print(f"{dep}: {[t.full_name for t in t_list]}")
print("-" * 50)


# Запрос 2: Список отделов с максимальным количеством групп преподавателей в каждом отделе, отсортированный по максимальному количеству групп
max_groups_in_departments = [
    (dep.name, max([len(t.groups) for t in teachers if dep.dep_id in t.departments]))
    for dep in departments
]
max_groups_in_departments.sort(key=lambda x: x[1], reverse=True)

#немножко красоты
def get_group_word(count: int) -> str:
    if 11 <= count % 100 <= 19:
        return "групп"
    else:
        if count % 10 == 1:
            return "группа"
        elif 2 <= count % 10 <= 4:
            return "группы"
        else:
            return "групп"

print("\nЗапрос 2: Отделы с максимальным количеством групп:")
for dep, groups in max_groups_in_departments:
    print(f"{dep}: {groups}: {get_group_word(groups)};")
print("-" * 50)


# Запрос 3: Список всех связанных преподавателей и отделов, отсортированный по сумме групп в каждом корпусе
department_teacher_relationship = [
    (dep.name, [t.full_name for t in teachers if dep.dep_id in t.departments], 
     sum([len(t.groups) for t in teachers if dep.dep_id in t.departments]))
    for dep in departments
]
department_teacher_relationship.sort(key=lambda x: x[2], reverse=True)

print("\nЗапрос 3: Связанные преподаватели и отделы (сортировка по сумме групп):")
for dep, t_list, group_sum in department_teacher_relationship:
    print(f"Учебный корпус: {dep} (Всего {group_sum} {get_group_word(group_sum)}:)")
    if t_list:
        for teacher in t_list:
            print(f"  - Преподаватель: {teacher}")
    else:
        print("  Нет связанных преподавателей")
print("-" * 50)
print("¯\_(ツ)_/¯")