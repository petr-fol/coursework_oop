from src.ABC_classes.abc_api import API
import requests
import json
import os


class APIHeadhunter(API):

    @staticmethod
    def save_data(area_id=113, specialization_id=1):
        """
        Получает данные о вакансиях с помощью API HeadHunter и сохраняет их в файл в формате JSON.

        :param area_id: Идентификатор региона (по умолчанию: 1 - Москва).
        :param specialization_id: Идентификатор специализации (по умолчанию: 1 - Разработка).
        """
        base_url = "https://api.hh.ru/vacancies"
        params = {
            "area": area_id,
            "specialization": specialization_id,
            "per_page": 10,  # Количество вакансий на странице
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Проверяем, был ли успешный запрос
            data = response.json()

            # Сохраняем данные в файл
            path = os.path.join("..", "data", "data_hh.json")
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            print(f"Данные успешно сохранены в файл: {'..data/data_hh.json'}")

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при запросе к API: {e}")

    # # Пример использования
    # api_key = "your_api_key"
    # file_path = "vacancies_hh.json"
    # save_data(file_path)
