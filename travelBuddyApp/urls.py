from django.urls import path     
from . import views
urlpatterns = [
	path('', views.register),
	path('createuser', views.createuser),
	path('travels', views.travels),
	path('login', views.login), 
	path('travels/add', views.newtrip),
	path('addtrip', views.addtrip),
	path('jointravel/<travelId>', views.join),
	path('trips/<travelId>', views.display),	
	path('logout', views.logout),
]