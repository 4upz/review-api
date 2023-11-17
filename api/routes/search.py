from flask import Blueprint, request

from api.services.tmdb_service import TMDBService

search = Blueprint('search', __name__)


@search.route('/search/movies', methods=['GET'])
def search_movie():
    query = request.args.get('query', default='', type=str)
    movie_service = TMDBService()
    results = movie_service.search(query)
    return {'results': results}, 200
