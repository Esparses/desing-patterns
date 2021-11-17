from __future__ import annotations
from abc import ABC, abstractmethod 


class Creator(ABC):

    @abstractmethod
    def crearOperator(self):
        pass

    def doOperation(self, a: int, b: int):
        op = self.crearOperator()
        print(f'Resultado de la operacion {op.doOperation(a,b)}')

