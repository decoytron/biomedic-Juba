# biomedic_app/urls.py
from django.urls import path
from .import views
from .views import registration, medication, counseling, forum, elearning, index, create_topic, view_topic
app_name = 'biomedic'

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('medication/', medication, name='medication'),
    path('counseling/', counseling, name='counseling'),
    path('forum/', forum, name='forum'),
    path('create_topic/', create_topic, name='create_topic'),
    path('view_topic/<int:topic_id>/', view_topic, name='view_topic'),
    path('elearning/', elearning, name='elearning'),
]
