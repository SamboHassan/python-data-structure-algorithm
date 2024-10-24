# Removing hardcoded URLs in templates

# tightly-coupled approach
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>


# Becomes
# you can remove a reliance on specific URL paths defined in your url configurations
# by using the {% url %} template tag:
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

# it uses the name defined here:
path("<int:question_id>/", views.detail, name="detail")


#--------- Namespacing URL names


# For example, the polls app has a
# detail view, and so might an app on the same project that is for a blog. How does one make it so that Django
# knows which app view to create for a url when using the {% url %} template tag?
# The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name
# to set the application namespace:



from . import views

app_name = "polls"

urlpatterns = [

	path("", views.index, name="index"),
	path("<int:question_id>/", views.detail, name="detail"),
	path("<int:question_id>/results/", views.results, name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
]

<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>






