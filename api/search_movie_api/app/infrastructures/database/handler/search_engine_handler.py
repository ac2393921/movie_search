from abc import ABC, abstractmethod


class SearchEngineHandler(ABC):
    @abstractmethod
    def search(self, index, query):
        pass
