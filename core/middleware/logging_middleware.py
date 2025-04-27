import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = datetime.now()

        method = request.method
        path = request.get_full_path()
        user_id = 'Anonymous'

        user = getattr(request, 'user', None)
        if user and hasattr(user, 'id') and user.id is not None:
            user_id = user.id

        logger.info(f"Request Started | Method: {method} | Path: {path} | User ID: {user_id}")

    def process_response(self, request, response):
        method = request.method
        path = request.get_full_path()

        duration = "-"
        if hasattr(request, 'start_time'):
            duration = (datetime.now() - request.start_time).total_seconds()

        user_id = 'Anonymous'
        user = getattr(request, 'user', None)
        if user and hasattr(user, 'id') and user.id is not None:
            user_id = user.id

        logger.info(f"Request Ended | Method: {method} | Path: {path} | Status: {response.status_code} | User ID: {user_id} | Duration: {duration}s")

        return response
