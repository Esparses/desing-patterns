
from __future__ import annotations
from abc import ABC, abstractmethod 


class Operator(ABC):

    @abstractmethod
    def doOperation(self, a: int, b: int):
        pass