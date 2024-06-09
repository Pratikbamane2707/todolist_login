from django.urls import path
from . import views

urlpatterns = [

    path('',views.home1,name='home1'),
    path('signup/',views.signup1,name='signup1'),
    path('login/',views.login_view,name='login1'),
    path('logout/',views.logout_view,name='logout1'),
    path('index/',views.Index,name='Index'),
    path('create/',views.todo_create,name='todo_create'),
    path('<int:id>/update/',views.todo_update,name='todo_update'),
    path('<int:id>/delete/',views.todo_delete,name='todo_delete'),

]