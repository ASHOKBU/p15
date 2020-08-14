from django.urls import path
app_name="myapp"
from myapp import views

urlpatterns=[
    path('base/',views.base,name='base'),
    path('profile/', views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('img_upld/',views.img_upld, name='img_upld'),
    path('img_disp/',views.img_disp,name='img_disp'),
]