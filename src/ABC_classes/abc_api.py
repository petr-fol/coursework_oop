from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def save_data(self):
        # обращается по апи,
        # сохраняет данные в файл
        pass
