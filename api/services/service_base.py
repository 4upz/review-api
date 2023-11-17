from typing import Optional, List
from abc import ABC, abstractmethod
from api.models import SearchResult


class Service(ABC):
    """
    Abstract base class for a service.
    """

    def __init__(self, base_url: str, token: Optional[str] = None) -> None:
        """
        Initializes the Service with a base URL and an optional token.

        :param base_url: The base URL for the service.
        :param token: An optional authentication token.
        """
        self.baseURL = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def setAuthHeader(self, token: str, client_id: Optional[str]) -> None:
        """
        Sets the default authorization header used for each request.

        :param token: The token to be used for this service.
        :param client_id: The optional clientId to be used.
        """
        self.headers['Authorization'] = f"Bearer {token}"
        if client_id:
            self.headers['Client-ID'] = client_id

    @abstractmethod
    async def search(self, query: str) -> List[SearchResult]:
        """
        Searches the API service using the provided query string. (Abstract method)

        :param query: Term to search for.
        :return: List of search results.
        """
        pass

    @abstractmethod
    async def getById(self, id: str) -> SearchResult:
        """
        Fetches a resource from the API service by a given ID. (Abstract method)

        :param id: The resource ID to fetch.
        :return: The search result.
        """
        pass
