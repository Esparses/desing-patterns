from .operator import Operator

__all__ = ["Multiplicacion"]
class Multiplicacion(Operator):

    def doOperation(self, a: int, b: int):
            return a * b