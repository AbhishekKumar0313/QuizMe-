from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('home/',views.home_view,name='homepage'),
    path('logout/',views.logout_view,name='logout'),
    path('start/',views.start_view,name='start'),
    path('question/<int:session_id>/<int:question_number>/',views.get_question,name='question'),
    path('submit/<int:session_id>/<int:question_number>/',views.submit_answer,name='submit_answer'),
    path('result/<int:session_id>/',views.result_view,name='result'),
 
 ]
