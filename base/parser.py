import orjson
from ninja.parser import Parser

from django.http import HttpResponse


class ORJSONParser(Parser):
    def parser_body(self, request: HttpResponse):
        return orjson.loads(request.body)
