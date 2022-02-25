# pylint: disable=too-few-public-methods
import json
import logging
from django.core.handlers.wsgi import WSGIRequest


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger = logging.getLogger("requests")

        logger.debug(isinstance(request, WSGIRequest))
        logger.debug(request.META)

        content_type = request.META.get("CONTENT_TYPE")
        if content_type == "application/json":
            data = request.body.decode("utf-8")
            data = json.loads(data) if data else None
        else:
            data = None

        headers = {
            "CONTENT_TYPE": content_type,
            "HTTP_AUTHORIZATION": request.META.get("HTTP_AUTHORIZATION"),
            "HTTP_USER_AGENT": request.META.get("HTTP_USER_AGENT"),
            "HTTP_HOST": request.META.get("HTTP_HOST"),
        }

        message = {
            "path": request.path + ("?" + request.META.get("QUERY_STRING"))
            if request.META.get("QUERY_STRING")
            else request.path,
            "method": request.method,
            "headers": {**{key: value for key, value in headers.items() if value}},
            **({"data": data} if data else {}),
        }
        logger.info(
            "Received request: %s", json.dumps(message, indent=4, sort_keys=True)
        )
        return self.get_response(request)
