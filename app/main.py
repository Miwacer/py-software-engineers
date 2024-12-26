class SoftwareEngineer:
    skills = []

    def __init__(self, name: str) -> None:
        self.name = name

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    skills = ["JavaScript", "HTML", "CSS"]

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"

class BackendDeveloper(SoftwareEngineer):
    skills = ["Python", "SQL", "Django"]

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"

class AndroidDeveloper(SoftwareEngineer):
    skills = ["Java", "Android studio"]

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    skills = BackendDeveloper.skills + FrontendDeveloper.skills

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()


full_stack = FullStackDeveloper("Oleg")

full_stack.create_web_application()
# front_dev = FrontendDeveloper("Alisa")
# print(front_dev.name)
# print(front_dev.skills)
# page = front_dev.create_awesome_web_page()
# print(page)
# engineer = SoftwareEngineer("Max")
# print(engineer.name)
# print(engineer.skills)
# engineer.learn_skill('Phyton')
# print("After add skill")
# print(engineer.skills)