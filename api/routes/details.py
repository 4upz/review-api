import logging
from flask import Blueprint, request

from api.services.tmdb_service import TMDBService

details = Blueprint('details', __name__)
logger = logging.getLogger(__name__)


@details.route('/details/movie/<id>', methods=['GET'])
def get_movie_details(id):
    try:
        movie_service = TMDBService()
        result = movie_service.getById(id)
        return {'result': result}, 200
    except Exception as e:
        raise RuntimeError(e.args[0])


@details.errorhandler(RuntimeError)
def handle_service_error(error):
    logger.error(f'[SERVER ERROR] {error.args[0]}')
    return {'error': error.args[0]}, 500
