from abc import ABC, abstractmethod
from typing import List

# ==========================================
# 1. Observer Pattern for Notifications
# ==========================================

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# ==========================================
# 2. Factory Method for User Roles
# ==========================================

class User(Observer):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display_dashboard(self):
        pass

class Student(User):
    def display_dashboard(self):
        print(f"[Student Dashboard] Welcome {self.name}. View courses, assignments, and grades.")

    def update(self, message: str):
        print(f"Notification for Student {self.name}: {message}")

class Teacher(User):
    def display_dashboard(self):
        print(f"[Teacher Dashboard] Welcome {self.name}. Manage courses, grade assignments, and post announcements.")

    def update(self, message: str):
        print(f"Notification for Teacher {self.name}: {message}")

class Parent(User):
    def display_dashboard(self):
        print(f"[Parent Dashboard] Welcome {self.name}. Monitor academic progress and attendance.")

    def update(self, message: str):
        print(f"Notification for Parent {self.name}: {message}")

class Admin(User):
    def display_dashboard(self):
        print(f"[Admin Dashboard] Welcome {self.name}. Manage users, system settings, and integrations.")

    def update(self, message: str):
        print(f"Notification for Admin {self.name}: {message}")

class UserFactory:
    @staticmethod
    def create_user(role: str, name: str) -> User:
        role = role.lower()
        if role == "student":
            return Student(name)
        elif role == "teacher":
            return Teacher(name)
        elif role == "parent":
            return Parent(name)
        elif role == "admin":
            return Admin(name)
        else:
            raise ValueError(f"Unknown user role: {role}")

# ==========================================
# Integrating the System (Example)
# ==========================================

class Course(Subject):
    def __init__(self, course_name: str):
        super().__init__()
        self.course_name = course_name

    def post_announcement(self, announcement: str):
        print(f"\n--- Posting Announcement to {self.course_name} ---")
        self.notify(f"[{self.course_name}] New Announcement: {announcement}")

    def upload_grades(self):
        print(f"\n--- Uploading Grades for {self.course_name} ---")
        self.notify(f"[{self.course_name}] Grades have been uploaded.")

# ==========================================
# Main Execution
# ==========================================
if __name__ == "__main__":
    # 1. Create users using Factory Pattern
    factory = UserFactory()
    student1 = factory.create_user("student", "Alice")
    student2 = factory.create_user("student", "Bob")
    teacher = factory.create_user("teacher", "Mr. Smith")
    parent = factory.create_user("parent", "Alice's Mom")

    # Display dashboards (polymorphism via Factory)
    print("--- Dashboards ---")
    student1.display_dashboard()
    teacher.display_dashboard()
    parent.display_dashboard()

    # 2. Setup Course and Observers (Observer Pattern)
    math_course = Course("Mathematics 101")
    
    # Subscribe users to course notifications
    math_course.attach(student1)
    math_course.attach(student2)
    math_course.attach(parent)
    # The teacher who posts might not need notifications of their own post, but we can add them
    math_course.attach(teacher)

    # Trigger events that notify users automatically
    math_course.post_announcement("Midterm exam scheduled for next Friday.")
    math_course.upload_grades()
