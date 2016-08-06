from django.conf.urls import url
from . import views
app_name = 'quoter'
urlpatterns = [
	url(r'^read',views.index,name='good_read'),
	url(r'^add_quote',views.add,name='add_quote'),
	url(r'^get_quote',views.get_quote,name='get_quote'),
	
]
