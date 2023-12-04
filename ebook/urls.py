from django.template.context_processors import static
from django.urls import path
from django.contrib.auth import views as auth_views
from Boook import settings
from .views import *
from . import  views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'ebook'
urlpatterns = [
    path('livres/index', livreList.as_view() , name='index' ),
    path('test/home', home , name='home' ),
    path('ebook/test/login', login_user , name='login' ),
    path('ebook/test/register', registerview , name='register' ),
    path('ebook/test/afterLogin',categorieList.as_view(),name='afterLogin'),
    path('test/showBooks/<int:pk>/',categorieDetail.as_view(),name='showBooks'),
    path('test/PageLecture/<int:pk>/',livreDetail.as_view(),name='pageLecture'),
    path('test/showPDF/<int:pk>/',livreDetailpdf.as_view(),name='showPDF'),
    path('test/touslivres',livreList2.as_view(),name='touslivres'),
    path('test/contact',conList.as_view(),name='contact'),
    path('test/profilee/<int:pk>/',userDetail.as_view(),name='profilee'),
    path('test/EditPassword/<int:pk>/',userdt.as_view(),name='EditPassword'),
    path('ebook/password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('ebook/password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('ebook/password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('ebook/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('ebook/reset/<uidb64>/<token>/ ',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('ebook/reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),



]

urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
