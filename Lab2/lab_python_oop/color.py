class FigureColor:  # Класс «Цвет фигуры»
    def __init__(self):
        self._color = None

    @property
    def colorproperty(self):  # Getter
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):  # Setter
        self._color = value