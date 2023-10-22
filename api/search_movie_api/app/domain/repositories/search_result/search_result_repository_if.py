from abc import ABC, abstractmethod

from app.domain.entities.search_result import SearchResult


class SearchResultRepositoryIf(ABC):
    @abstractmethod
    def search(self, keyword: str) -> SearchResult:
        raise NotImplementedError
