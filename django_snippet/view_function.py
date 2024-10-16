from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from polls.models import Poll


def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")
        # Return a "created" (201) response code.
        # return HttpResponse(status=201)


def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, "polls/detail.html", {"poll": p})


# --------------- Async views
# views can also be asynchronous (“async”) functions, normally
# defined using Python’s async def syntax. Django will automatically detect these and run them in an async
# context. However, you will need to use an async server based on ASGI to get their performance benefits.


async def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)


from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def my_view(request):
    pass
