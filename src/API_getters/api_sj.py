import json
import os

import requests

from src.ABC_classes.abc_api import API


class APISuperJob(API):

    @staticmethod
    def save_data(town_id=None, catalogues_id=33):
        """
        Получает данные о вакансиях с помощью API SuperJob и сохраняет их в файл в формате JSON.

        :param town_id: Идентификатор города (по умолчанию: 4 - Москва).
        :param catalogues_id: Идентификатор каталога (по умолчанию: 33 - Разработка).
        """
        base_url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {
            "X-Api-App-Id": os.getenv("sj_api"),  # Используйте переменную окружения для ключа API
        }

        params = {
            "town": town_id,
            "catalogues": catalogues_id,
            "count": 10,  # Количество вакансий на странице
        }

        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()  # Проверяем, был ли успешный запрос
            data = response.json()

            # Сохраняем данные в файл
            path = os.path.join("..", "data", "data_sj.json")

            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            print(f"Данные успешно сохранены в файл {path}")

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при запросе к API SuperJob: {e}")

    # # Пример использования
    # file_path_superjob = "superjob_vacancies.json"
    # save_superjob_data(file_path_superjob)
