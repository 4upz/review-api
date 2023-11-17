
from flask import Blueprint, request
import time

health = Blueprint('health', __name__)


@health.route('/health')
def health_check():
    return {'status': 'ok'}, 200
