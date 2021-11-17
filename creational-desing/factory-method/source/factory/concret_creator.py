from .creator import Creator
from creator import Suma, Multiplicacion, Division
__all__ = ['SumaCreator', 'DivisionCreator', 'MultiplicacionCreator']

class SumaCreator(Creator):
    def crearOperator(self):
        return Suma()

class DivisionCreator(Creator):
    def crearOperator(self):
        return Division()

class MultiplicacionCreator(Creator):
    def crearOperator(self):
        return Multiplicacion()

