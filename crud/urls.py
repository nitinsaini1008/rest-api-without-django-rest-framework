
from django.urls import path,include
from .import views

urlpatterns = [
	path('api/<id>',views.myclass.as_view(),name='api'),
	path('api/',views.my_class_2.as_view(),name='api_2'),
	]
