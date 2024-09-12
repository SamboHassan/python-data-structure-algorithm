from django.http import HttpResponse, HttpResponseNotFound


def my_view(request):
    # ...

    if foo:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")


def my_view(request):
    # ...
    # Return a "created" (201) response code.
    return HttpResponse(status=201)


# If you raise Http404 at any point in a view function,
# Django will catch it and return the standard error page
# for your application, along with an HTTP error code 404
from django.http import Http404
from django.shortcuts import render
from polls.models import Poll


def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, "polls/detail.html", {"poll": p})


# This template will then be served when DEBUG
# is set to False.


# Specify the handlers as seen below in your URLconf (setting them anywhere
# else will have no effect).

# The page_not_found() view is overridden by handler404:
handler404 = "mysite.views.my_custom_page_not_found_view"

# The server_error() view is overridden by handler500:


"""
handler500 = "mysite.views.my_custom_error_view"
The permission_denied() view is overridden by handler403:
handler403 = "mysite.views.my_custom_permission_denied_view"
The bad_request() view is overridden by handler400:
handler400 = "mysite.views.my_custom_bad_request_view"
See also:
Use the CSRF_FAILURE_VIEW setting to override the CSRF error view.

"""

# Testing custom error views
# To test the response of a custom error handler, raise the appropriate exception in a test view. For example:


from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path
def response_error_handler(request, exception=None):
return HttpResponse("Error handler content", status=403)
def permission_denied_view(request):
raise PermissionDenied


urlpatterns = [
path("403/", permission_denied_view),
]
handler403 = response_error_handler
# ROOT_URLCONF must specify the module that contains handler403 = ...
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):
def test_handler_renders_template_response(self):
response = self.client.get("/403/")


# Make assertions on the response here. For example:
self.assertContains(response, "Error handler content", status_code=403)
