from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request: HttpRequest):
    if request.method != "GET":
        return HttpResponseNotAllowed(permitted_methods="GET")

    return HttpResponse("<h1>Working Method</h1>")


@cache_page(60 * 1)
def demo(request: HttpRequest) -> HttpResponse:
    if request.method != "GET":
        return HttpResponseNotAllowed(permitted_methods="GET")

    return HttpResponse("<h1>Cached page</h1>")


@csrf_exempt
def no_response(request) -> HttpResponse:
    if request.method == "GET":
        return HttpResponse("<h1>Hello GET Request</h1>")

    return HttpResponseNotAllowed(permitted_methods="GET")
