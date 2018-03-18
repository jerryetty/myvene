from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'my_allowance'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^privacy_policy/$', views.privacy_policy, name='privacy_policy'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^who_we_are/$', views.who_we_are, name='who_we_are'),
	url(r'^earn/$', views.earn, name='earn'),
	
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^add_child/$', views.add_child, name='add_child'),
	url(r'^pay_history/$', views.pay_history, name='pay_history'),
	url(r'^pay_methods/$', views.pay_methods, name='pay_methods'),
	url(r'^notifications/$', views.notifications, name='notifications'),
	url(r'^refer/$', views.refer, name='refer'),
	url(r'^settings/$', views.settings, name='settings'),

	url(r'^account/$', views.account, name='account'),
	url(r'^password/$', views.password, name='password'),
	url(r'^not_preferences/$', views.not_preferences, name='not_preferences'),

]