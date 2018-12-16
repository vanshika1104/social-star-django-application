from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    #login-logout urls
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'registration/logout.html'}, name='logout'),
    url(r'^logout_then_login/$', auth_views.logout_then_login, name='logout_then_login'),
    #password change URLs
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    #restore password URLs
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    #user profile URLs
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/follow/$', views.user_follow, name='user_follow'),
    url(r'^users/profile/$', views.profile_view, name='profile_view'),
    url(r'^users/pictures/$',views.picture_view, name='picture_view'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
]
