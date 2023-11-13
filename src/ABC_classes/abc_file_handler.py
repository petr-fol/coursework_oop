from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def save_vacancies(self, ):
        # берет данные из файла всех данных
        # формирует словарь с данными по экземплярам класса вакансия
        # сохраняет эти данные в другой файл
        pass

    @abstractmethod
    def get_data_hh(self, ):
        # берёт данные из файла всех данных hh
        # возвращает эти данные
        pass

    @abstractmethod
    def get_data_sj(self, ):
        # берёт данные из файла всех данных hh
        # возвращает эти данные
        pass

    @abstractmethod
    def get_vacancies_hh(self, ):
        # берёт данные из файла вакансий hh
        # возвращает эти данные
        pass

    @abstractmethod
    def get_vacancies_sj(self, ):
        # берёт данные из файла вакансий sj
        # возвращает эти данные
        pass

    @abstractmethod
    def get_sorted_vacancies_hh(self, top=1, min_salary=0, key_word='Python'):
        # сортирует данные по параметрам и возвращает их
        pass

    @abstractmethod
    def get_sorted_vacancies_sj(self, top=1, min_salary=0, key_word='Python'):
        # сортирует данные по параметрам и возвращает их
        pass
