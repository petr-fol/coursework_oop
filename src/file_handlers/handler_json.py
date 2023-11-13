import os
from src.ABC_classes.abc_file_handler import Handler
import json

from src.file_handlers.vacancy import Vacancy


class JSONHandler(Handler):

    @staticmethod
    def save_vacancies_hh():
        """
        Преобразует данные из файла с вакансиями в экземпляры класса Vacancy и сохраняет в новый файл.

        """
        try:
            path = os.path.join("..", "data", "data_hh.json")
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Преобразовываем данные в экземпляры класса Vacancy
            vacancies = []
            for item in data["items"]:
                vacancy_data = item
                vacancy = Vacancy(
                    profession=vacancy_data["name"],
                    url=vacancy_data["url"],
                    salary_min=vacancy_data["salary"]["from"] if vacancy_data["salary"] and "from" in vacancy_data[
                        "salary"] else 0,
                    salary_max=vacancy_data["salary"]["to"] if vacancy_data["salary"] and "to" in vacancy_data[
                        "salary"] else 0,
                    currency=vacancy_data["salary"]["currency"] if vacancy_data["salary"] else "",
                    requirement=vacancy_data["snippet"]["requirement"] if vacancy_data["snippet"] and "requirement" in
                    vacancy_data["snippet"] else ""
                )
                vacancies.append(vacancy)

            # Упаковываем экземпляры класса Vacancy в новые JSON словари
            formatted_vacancies = []
            for vacancy in vacancies:
                formatted_vacancy = {
                    "profession": vacancy.profession,
                    "url": vacancy.url,
                    "salary_min": vacancy.salary_min,
                    "salary_max": vacancy.salary_max,
                    "currency": vacancy.currency,
                    "requirement": vacancy.requirement
                }
                formatted_vacancies.append(formatted_vacancy)

            # Сохраняем новые данные в файл
            path = os.path.join("..", "data", "vacancies_hh.json")
            with open(path, "w", encoding="utf-8") as output_file:
                json.dump(formatted_vacancies, output_file, ensure_ascii=False, indent=2)

            print(f"Данные успешно сохранены в файл: {'..data/vacancies_hh.json'}")

        except FileNotFoundError:
            print(f"Файл {path} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {path}. Проверьте корректность формата данных.")

    @staticmethod
    def save_vacancies_sj():
        """
        Преобразует данные из файла с вакансиями в экземпляры класса Vacancy и сохраняет в новый файл.

        """
        try:
            path = os.path.join("..", "data", "data_sj.json")
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Преобразовываем данные в экземпляры класса Vacancy
            vacancies = []
            for item in data["objects"]:
                vacancy_data = item
                vacancy = Vacancy(
                    profession=vacancy_data["profession"],
                    url=vacancy_data["link"],
                    salary_min=vacancy_data["payment_from"] if "payment_from" in vacancy_data else 0,
                    salary_max=vacancy_data["payment_to"] if "payment_to" in vacancy_data else 0,
                    currency=vacancy_data["currency"] if "currency" in vacancy_data else "",
                    requirement=vacancy_data["work"] if "work" in vacancy_data else ""
                )
                vacancies.append(vacancy)

            # Упаковываем экземпляры класса Vacancy в новые JSON словари
            formatted_vacancies = []
            for vacancy in vacancies:
                formatted_vacancy = {
                    "profession": vacancy.profession,
                    "url": vacancy.url,
                    "salary_min": vacancy.salary_min,
                    "salary_max": vacancy.salary_max,
                    "currency": vacancy.currency,
                    "requirement": vacancy.requirement
                }
                formatted_vacancies.append(formatted_vacancy)

            # Сохраняем новые данные в файл
            path = os.path.join("..", "data", "vacancies_sj.json")
            with open(path, "w", encoding="utf-8") as output_file:
                json.dump(formatted_vacancies, output_file, ensure_ascii=False, indent=2)

            print(f"Данные успешно сохранены в файл: {path}")

        except FileNotFoundError:
            print(f"Файл {path} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {path}. Проверьте корректность формата данных.")

    @staticmethod
    def get_data_hh():
        """
        Берет данные из файла и возвращает их.

        :return: Данные из файла в виде словаря.
        """
        try:
            path = os.path.join("..", "data", "data_hh.json")
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Файл {path} не найден.")
            return None
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {path}. Проверьте корректность формата данных.")
            return None

    @staticmethod
    def get_data_sj():
        """
        Берет данные из файла и возвращает их.

        :return: Данные из файла в виде словаря.
        """
        try:
            path = os.path.join("..", "data", "data_sj.json")
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Файл {path} не найден.")
            return None
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {path}. Проверьте корректность формата данных.")
            return None

    @staticmethod
    def get_vacancies_hh() -> list:
        """
        Берет данные из файла вакансий и возвращает их.

        :return: Данные из файла в виде списка вакансий.
        """
        try:
            path = os.path.join("..", "data", "vacancies_hh.json")
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            vacancies = []
            for vacancy_data in data:
                vacancy = Vacancy(
                    profession=vacancy_data["profession"],
                    url=vacancy_data["url"],
                    salary_min=vacancy_data["salary_min"],
                    salary_max=vacancy_data["salary_max"],
                    currency=vacancy_data["currency"],
                    requirement=vacancy_data["requirement"]
                )
                vacancies.append(vacancy)
                print(vacancy.profession, vacancy.requirement)  # Исправлено здесь
            # Используйте список vacancies по вашему усмотрению
            return vacancies
        except FileNotFoundError:
            print(f"Файл {'..data/vacancies_hh.json'} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {'..data/vacancies_hh.json'}. "
                  f"Проверьте корректность формата данных.")

    @staticmethod
    def get_vacancies_sj() -> list:
        """
        Берет данные из файла вакансий и возвращает их.

        :return: Данные из файла в виде списка вакансий.
        """
        try:
            path = os.path.join("..", "data", "vacancies_sj.json")
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            vacancies = []
            for vacancy_data in data:
                vacancy = Vacancy(
                    profession=vacancy_data["profession"],
                    url=vacancy_data["url"],
                    salary_min=vacancy_data["salary_min"],
                    salary_max=vacancy_data["salary_max"],
                    currency=vacancy_data["currency"],
                    requirement=vacancy_data["requirement"]
                )
                vacancies.append(vacancy)

            # Используйте список vacancies по вашему усмотрению
            return vacancies
        except FileNotFoundError:
            print(f"Файл {path} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {path}. "
                  f"Проверьте корректность формата данных.")

    @staticmethod
    def get_sorted_vacancies_hh(top=1, min_salary=0, key_word='Python') -> list:
        try:
            # Получение вакансий из файла
            vacancies = JSONHandler.get_vacancies_hh()
            print(vacancies)
            # Фильтрация по зарплате и ключевому слову
            filtered_vacancies = [vacancy for vacancy in vacancies
                                  if vacancy.salary_max >= min_salary
                                  and (key_word.lower() in vacancy.profession.lower() or
                                       key_word.lower() in vacancy.requirement.lower())]

            # Сортировка по убыванию зарплаты
            sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x.salary_max, reverse=True)

            # Выбор указанного количества вакансий
            result_vacancies = sorted_vacancies[:top]

            return result_vacancies

        except Exception as e:
            print(f"Ошибка при получении отсортированных вакансий: {e}")
            return []

    @staticmethod
    def get_sorted_vacancies_sj(top=1, min_salary=0, key_word='Python') -> list:
        try:
            # Получение вакансий из файла
            vacancies = JSONHandler.get_vacancies_sj()

            # Фильтрация по зарплате и ключевому слову
            filtered_vacancies = [vacancy for vacancy in vacancies
                                  if vacancy.salary_max >= min_salary
                                  and (key_word.lower() in vacancy.profession.lower() or
                                       key_word.lower() in vacancy.requirement.lower())]

            # Сортировка по убыванию зарплаты
            sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x.salary_max, reverse=True)

            # Выбор указанного количества вакансий
            result_vacancies = sorted_vacancies[:top]

            return result_vacancies

        except Exception as e:
            print(f"Ошибка при получении отсортированных вакансий: {e}")
            return []
