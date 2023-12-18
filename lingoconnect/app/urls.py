from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.home,name="home"),
    path("quizes/",views.Quizes,name="quizes"),
    path("Quiz/<int:quiz_id>/",views.quiz,name="Quiz"),
    path('submit-quiz/<int:quiz_id>/',views.submit_quiz,name='submit_quiz'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

]
