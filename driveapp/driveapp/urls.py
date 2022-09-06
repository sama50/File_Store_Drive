from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/',views.uploadFile,name="upload"),
    path('',views.home,name='drive'),
    path('accounts/profile/',views.redirectview),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
     path('login/', auth_views.LoginView.as_view(template_name='./login.html',authentication_form=LoginForm), name='login'),
    path('<slug:name>/',views.inside),
    path('<slug:name1>/<slug:name2>/',views.twoinside),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
