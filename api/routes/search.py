import logging
from flask import Blueprint, request

from api.services.tmdb_service import TMDBService

search = Blueprint('search', __name__)
logger = logging.getLogger(__name__)

@search.route('/search/movies', methods=['GET'])
def search_movie():
    query = request.args.get('query', default='', type=str)
    try:
        movie_service = TMDBService()
        results = movie_service.search(query)
        return {'results': results}, 200
    except Exception as e:
        raise RuntimeError(e.args[0])


@search.errorhandler(RuntimeError)
def handle_service_error(error):
    logger.error(f'[SERVER ERROR] {error.args[0]}')
    return {'error': error.args[0]}, 500
