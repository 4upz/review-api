import requests
from os import getenv
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

    def search(self, query: str):
        endpoint = f'{self.baseURL}/search/movie'
        params = {'query': query}

        try:
            response = requests.get(
                endpoint, params=params, headers=self.headers)
            response_data = response.json()
            if response.status_code != 200:
                raise Exception(response_data['status_message'])
            results = response_data['results']
        except Exception as e:
            raise Exception(f'Error fetching data from TMDB. {e.args[0]}')

        #  Return first five results
        return [
            SearchResult(
                id=str(result['id']),
                title=result['title'],
                description=result['overview'],
                image_url=f'https://www.themoviedb.org/t/p/w600_and_h900_bestv2{result["poster_path"]}',
                release_date=result['release_date']
            )
            for result in results[:5]
        ]

    def getById(self, id: str) -> SearchResult:
        endpoint = f'{self.baseURL}/movie/{id}'

        try:
            response = requests.get(endpoint, headers=self.headers)
            result = response.json()
            if response.status_code != 200:
                raise Exception(response.json()['status_message'])
        except Exception as e:
            raise Exception(f'Error fetching data from TMDB. {e.args[0]}')

        return SearchResult(
            id=str(result['id']),
            title=result['title'],
            description=result['overview'],
            image_url=f'https://www.themoviedb.org/t/p/w600_and_h900_bestv2{result["poster_path"]}',
            release_date=result['release_date']
        )
