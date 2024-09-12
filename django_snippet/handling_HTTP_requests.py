# # Here’s a sample URLconf:
# from django.urls import path
# from . import views

urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
]

# _______________________3.3 Handling HTTP requests

"""
Create a Python module This module is pure Python code and is a mapping between 
URL path expressions to Python functions (your views).

1. It determines the urlconf to use from the ROOT_URLCONF in setting.py file, but if 
the incoming HttpRequest object has a urlconf attribute (set by middleware), its value
will be used in place of the ROOT_URLCONF setting

2. It then loads that module and look for a variable named urlpatterns. This should 
be a sequence of django.urls.path() and/or django.urls.re_path() instances.

3. Django runs through each URL pattern, in order, and stops at the first one that 
matches the requested URL, matching against path_info.

4. Once one of the URL patterns matches, Django imports and calls the given view, 
which is a Python function (or a class-based view). The view gets passed the 
following arguments:
• An instance of HttpRequest.
• If the matched URL pattern contained no named groups, then the matches from the 
  regular expression are provided as positional arguments.
• The keyword arguments are made up of any named parts matched by the path expression 
  that are provided, overridden by any arguments specified in the optional kwargs 
  argument to django. urls.path() or django.urls.re_path().

5. If no URL pattern matches, or if an exception is raised during any point in this 
process, Django invokes an appropriate error-handling view. See Error handling below.

"""


Here’s a sample URLconf:
from django.urls import path
from . import views

urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
]

"""
Notes:
• To capture a value from the URL, use angle brackets.
• Captured values can optionally include a converter type. For example, 
  use <int:name> to capture an integer parameter. If a converter isn’t included, 
  any string, excluding a / character, is matched.
• There’s no need to add a leading slash, because every URL has that. For example, 
  it’s articles, not /articles.

Example requests:

• A request to /articles/2005/03/ would match the third entry in the list. Django 
  would call the function views.month_archive(request, year=2005, month=3).
• /articles/2003/ would match the first pattern in the list, not the second one, 
  because the patterns are tested in order, and the first one is the first test to 
  pass. Feel free to exploit the ordering to insert special cases like this. Here, 
  Django would call the function views.special_case_2003(request)
• /articles/2003 would not match any of these patterns, because each pattern 
  requires that the URL end with a slash.
• /articles/2003/03/building-a-django-site/ would match the final pattern. 
  Django would call the function views.article_detail(request, year=2003, month=3,
  slug="building-a-django-site").

"""


# ............... What the URLconf searches against
"""
The URLconf searches against the requested URL, as a normal Python string. This does 
not include GET or POST parameters, or the domain name.
For example, in a request to https://www.example.com/myapp/, the URLconf will 
look for myapp/. In a request to https://www.example.com/myapp/?page=3, the URLconf 
will look for myapp/. The URLconf doesn’t look at the request method. In other words, 
all request methods –POST, GET, HEAD, etc. –will be routed to the same function 
for the same URL.

"""



# ..... Specifying defaults for view arguments
# URLconf

from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.page),
    path("blog/page<int:num>/", views.page),
]

# View (in blog/views.py)
def page(request, num=1):
    pass
  # Output the appropriate page of blog entries, according to num.


# .... Error handling

"""
The variables are:
• handler400 –See django.conf.urls.handler400.
• handler403 –See django.conf.urls.handler403.
• handler404 –See django.conf.urls.handler404.
• handler500 –See django.conf.urls.handler500.
"""


# Including other URLconfs

from django.urls import include, path

urlpatterns = [
    # ... snip ...
    path("community/", include("aggregator.urls")),
    path("contact/", include("contact.urls")),
    # ... snip ...
]


from django.urls import include, path
from apps.main import views as main_views
from credit import views as credit_views

extra_patterns = [
    path("reports/", credit_views.report),
    path("reports/<int:id>/", credit_views.report),
    path("charge/", credit_views.charge),
]
urlpatterns = [
    path("", main_views.homepage),
    path("help/", include("apps.help.urls")),
    path("credit/", include(extra_patterns)),
]


from django.urls import include, path
from . import views


urlpatterns = [
    path(
        "<page_slug>-<page_id>/", 
        include( [
            path("history/", views.history),
            path("edit/", views.edit),
            path("discuss/", views.discuss),
            path("permissions/", views.permissions),
        ]),
    ),
]

# ............ Using regular expressions

from django.urls import path, re_path
from . import views
urlpatterns = [

    path("articles/2003/", views.special_case_2003),

    re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
    re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.month_archive),
    re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$",
    views.article_detail)

]


from django.urls import re_path

urlpatterns = [
    re_path(r"^blog/(page-([0-9]+)/)?$", blog_articles), # bad
    re_path(r"^comments/(?:page-(?P<page_number>[0-9]+)/)?$", comments), # good
]


# ................ Captured parameters

# In settings/urls/main.py
from django.urls import include, path

urlpatterns = [
    path("<username>/blog/", include("foo.urls.blog")),
]


# In foo/urls/blog.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.blog.index),
    path("archive/", views.blog.archive),
]


# .................... Passing extra options to view functions

from django.urls import path
from . import views

urlpatterns = [
    path("blog/<int:year>/", views.year_archive, {"foo": "bar"}),
]


# In this example, for a request to /blog/2005/, Django will call 
# views.year_archive(request, year=2005, foo='bar').
# This technique is used in the syndication framework to pass metadata and 
# options to views.

# ------------  Passing extra options to include()

# main.py# main.py
from django.urls import include, path

urlpatterns = [
    path("blog/", include("inner"), {"blog_id": 3}),
]


# inner.py
from django.urls import path
from mysite import views

urlpatterns = [
    path("archive/", views.archive),
    path("about/", views.about),
]


# main.py
from django.urls import include, path
from mysite import views

urlpatterns = [
    path("blog/", include("inner")),
]


# inner.py
from django.urls import path

urlpatterns = [
    path("archive/", views.archive, {"blog_id": 3}),
    path("about/", views.about, {"blog_id": 3}),
]


from django.urls import include, path

urlpatterns = [
    path("blog/", include("inner"), {"blog_id": 3}),
]



# inner.py
from django.urls import path
from mysite import views

urlpatterns = [
    path("archive/", views.archive),
    path("about/", views.about),
]
