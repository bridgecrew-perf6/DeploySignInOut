from django.urls import path
from .views import * 

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', signin, name='signin'),
    path('logout/', signout, name='signout'),
    path('dashboard/<str:username>', dashboard, name='dashboard'),

    path('dashboard/<str:username>/create-new-form', createNewForm, name='CreateNewForm'),

    path('dashboard/<str:username>/sign-out-form', form_signout_equipments, name='form_out'),
    path('dashboard/<str:username>/sign-in-form', form_signin_equipments, name='sign_in'),

    path('dashboard/<str:username>/period1', period_one, name='period_1'),
    path('dashboard/<str:username>/period2', period_two, name='period_2'),
    path('dashboard/<str:username>/period3', period_three, name='period_3'),
    path('dashboard/<str:username>/period4', period_four, name='period_4'),
]