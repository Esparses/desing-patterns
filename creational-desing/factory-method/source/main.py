from factory import *
from creator import *


if __name__ == "__main__":
    suma = SumaCreator()
    suma.doOperation(9, 3)

    division = DivisionCreator()
    division.doOperation(9, 3)

    multiplicacion = MultiplicacionCreator()
    multiplicacion.doOperation(9, 3)

