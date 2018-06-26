"""django_meetup_job_board_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from dmjb import views
from registration.backends.simple.views import RegistrationView


# Create a new class that redirects the user to the index page, #if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/dmjb/'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dmjb/', include('dmjb.urls')),
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^activate/', include('registration.backends.default.urls')),
    url(r'^accounts/register/$',
        MyRegistrationView.as_view(), name='registration_register'),

    # url(r'^activate/complete/$',
    #     TemplateView.as_view(template_name='registration/activation_complete.html'),
    #     name='registration_activation_complete'),
    # url(r'^activate/(?P<activation_key>\w+)/$',
    #     ActivationView.as_view(),
    #     name='registration_activate'),
    # url(r'^register/complete/$',
    #     TemplateView.as_view(template_name='registration/registration_complete.html'),
    #     name='registration_complete'),
]
