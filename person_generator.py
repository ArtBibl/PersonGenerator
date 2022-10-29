import random
import csv

FILE = "persons.txt"

MALE_NAME_FILE = "male_name.txt"
FEMALE_NAME_FILE = "female_name.txt"
SECOND_NAME = "second_name.txt"
CITY_OF_BIRTHDAY = "city_ukraine.txt"
PROFESSION = "profession.txt"
BEST_BOOKS = "best_books.txt"

SEX = ("Чоловіча", "Жіноча")
VACCINATED = ("Вакцинован", "Не вакцинован")
PETS = ("Ні", "Так")
HIGHER_EDUCATION = ("Відсутня вища освіта", "Вища освіта")


class Person:
    def __init__(self) -> None:
        self.person_in_string = None
        self.all_info = None
        self.name = None
        self.second_name = None
        self.patronymic_name = None
        self.age = 0
        self.sex = None
        self.profession = None
        self.city_of_birthday = None
        self.vaccinated = None
        self.pets = None
        self.higher_education = None
        self.favorite_book = None

    def get_person_in_string(self, order_="sn, n, pn, a, s, pro, cb, v, pet, he, bb") -> str:
        """Return a string from the function 'get_person_in_list'."""
        self.person_in_string = ', '.join(self.get_person_in_list(order_))
        return self.person_in_string

    def get_person_in_list(self, order_="sn, n, pn, a, s, pro, cb, v, pet, he, bb") -> list[str]:
        """Creating a list with 'str'."""
        self.all_info = []
        self.sex = random.choice(SEX)
        self.age = random.randint(1, 80)
        flag = ""
        for ind, element in enumerate(order_):
            flag += element
            if element == " " or element == ":":
                flag = ""
                continue
            elif element == ",":
                flag = flag[:-1]
                self.all_info.append(self.__add_value_of_person(flag))
                flag = ""
            elif ind == (len(order_) - 1):
                self.all_info.append(self.__add_value_of_person(flag))
        return self.all_info

    def __add_value_of_person(self, flag) -> str or int:
        """Forming a list by flags"""
        if flag == "n":
            return self.__generate_name()
        elif flag == "sn":
            self.second_name = random.choice(self.__read_files(SECOND_NAME))
            return self.second_name
        elif flag == "pn":
            return self.__patronymic_name()
        elif flag == "a":
            return str(self.age)
        elif flag == "s":
            return self.sex
        elif flag == "pro":
            return self.__profession()
        elif flag == "cb":
            self.city_of_birthday = random.choice(self.__read_files(CITY_OF_BIRTHDAY))
            return self.city_of_birthday
        elif flag == "v":
            return self.__vaccinated()
        elif flag == "pet":
            self.pets = random.choice(PETS)
            return self.pets
        elif flag == "he":
            return self.__higher_education()
        elif flag == "bb":
            return self.__favorite_book()

    def __generate_name(self) -> str:
        """Selecting a name from a file by sex."""
        if self.sex == SEX[0]:
            self.name = random.choice(self.__read_files(MALE_NAME_FILE))
        else:
            self.name = random.choice(self.__read_files(FEMALE_NAME_FILE))
        return self.name

    def __patronymic_name(self) -> str:
        """Creating a patronymic name."""
        self.patronymic_name = random.choice(self.__read_files(MALE_NAME_FILE))
        if self.sex == SEX[0]:
            if self.patronymic_name == "Михайло":
                self.patronymic_name = "Михайлович"
            elif self.patronymic_name == "Микола":
                self.patronymic_name = "Миколайович"
            else:
                self.patronymic_name = self.patronymic_name + 'ович'
        else:
            if self.patronymic_name == "Григорій":
                self.patronymic_name = "Григорівна"
            elif self.patronymic_name == "Микола":
                self.patronymic_name = "Миколаївна"
            else:
                self.patronymic_name = self.patronymic_name + 'івна'
        return self.patronymic_name

    def __profession(self) -> str:
        """The profession is only for people aged 17 to 60."""
        if self.age > 60:
            self.profession = "Пенсіонер"
        elif self.age < 17:
            self.profession = "Дитина"
        else:
            self.profession = random.choice(self.__read_files(PROFESSION))
        return self.profession

    def __vaccinated(self) -> str:
        """Adding the letter "a" if the person is female."""
        vac = random.choice(VACCINATED)
        self.vaccinated = vac + 'а' if self.sex == SEX[1] else vac
        return self.vaccinated

    def __higher_education(self) -> str:
        """Until 22 year higher education not possible. Then 50-50."""
        if self.age > 22:
            self.higher_education = random.choice(HIGHER_EDUCATION)
        else:
            self.higher_education = HIGHER_EDUCATION[0]
        return self.higher_education

    def __favorite_book(self) -> str:
        if self.age < 10:
            self.favorite_book = "Не вміє читати"
        else:
            self.favorite_book = random.choice(self.__read_files(BEST_BOOKS))
        return self.favorite_book

    def __read_files(self, file) -> list[str]:
        """Read files and generate list. Seems its like polymorphism..."""
        with open(file, "r") as f:
            self.memory = []
            for line in f:
                self.memory.append(line.strip())
        return self.memory


if __name__ == '__main__':
    person = Person()

    header = [["Прізвище:", "Ім'я:", "Ім'я по батькові:", "Вік:", "Стать:",
               "Професія", "Місто народження:", "Вакцинація:",
               "Домашні тварини:", "Вища освіта:", "Улюблена книга:"]]
    for i in range(10):
        print(person.get_person_in_string(order_="n, sn, pn, a, s, pro, cb, v, pet, he, bb"))

        # header.append(person.get_person_in_string())

    # with open('persons.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    #     for row in header:
    #         writer.writerow(row)
    #         repr(print(row))
