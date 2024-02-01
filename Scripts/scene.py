from abc import ABC, abstractclassmethod

class Scene(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def display(self) -> None:
        pass
    
    @abstractclassmethod
    def update(self) -> None:
        pass

    @abstractclassmethod
    def check_events(self) -> None:
        pass