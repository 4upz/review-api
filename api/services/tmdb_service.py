import requests
from os import getenv
from typing import Any, Coroutine, List
from dotenv import load_dotenv
from api.models import SearchResult
from .service_base import Service

# Load env variables
load_dotenv()


class TMDBService(Service):
    BASE_URL = 'https://api.themoviedb.org/3'

    def __init__(self) -> None:
        self.token = getenv('TMDB_API_TOKEN')
        if self.token is None:
            raise Exception('The TMDB_API_TOKEN was not found')
        super().__init__(base_url=self.BASE_URL, token=self.token)

    async def search(self, query: str):
        endpoint = f'{self.baseURL}/search/movie'
        params = {'query': query}

        results = []

        try:
            response = await requests.get(
                endpoint, params=params, headers=self.headers)
            if response.text.error:
                raise Exception(response.text.error)
            results = response.text.results
        except Exception as e:
            raise Exception('Error fetching data from TMDB: ', e)

        #  Return first five results
        return [
            SearchResult(
                id=str(result['id']),
                title=result['title'],
                description=result['overview'],
                image=f'https://www.themoviedb.org/t/p/w600_and_h900_bestv2{result["poster_path"]}',
                date=result['release_date']
            )
            for result in results[:5]
        ]

    def getById(self, id: str) -> SearchResult:
        pass
