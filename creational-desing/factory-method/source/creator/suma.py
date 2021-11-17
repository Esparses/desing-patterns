from .operator import Operator

__all__ = ["Suma"]
class Suma(Operator):
        def doOperation(self, a: int, b: int):
            return a + b