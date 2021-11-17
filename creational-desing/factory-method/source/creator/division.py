from .operator import Operator

__all__ = ["Division"]
class Division(Operator):

    def doOperation(self, a: int, b: int):
            return a / b
    