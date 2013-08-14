from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from core.forms import LoginForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.main', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'core/signin.html' , 'authentication_form' : LoginForm}),
    # {'template_name': 'core/index.html', 'authentication_form': TopLoginForm, 'extra_context': {'signup_form': FrontSignUpForm()}
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^accounts/signup/$', 'core.views.signup', name='signup'),
    url(r'^accounts/signin/$', 'core.views.signin', name='signin'),

    url(r'^main/$', 'core.views.main'),
    url(r'^home/$', 'survey.views.home'),
    url(r'^calculator/', 'survey.views.calculator'),
    url(r'^pre_start/$', 'survey.views.pre_start'),
    url(r'^start_survey/$', 'survey.views.getbaseinfo'),

    url(r'^preliminary1/$','survey.views.preliminary1'),
    url(r'^preliminary2/$','survey.views.preliminary2'),
    url(r'^preliminary3/$','survey.views.preliminary3'),
    url(r'^preliminary4/$','survey.views.preliminary4'),

    url(r'^onboarding1/$','survey.views.onboarding1'),    
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
