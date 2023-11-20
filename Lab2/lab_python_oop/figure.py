from abc import ABC, abstractmethod # abc = abstract


class Figure(ABC):  # Абстрактный класс «Геометрическая фигура»
    @abstractmethod
    def area(self):
        pass