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

    # account
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'core/signin.html' , 'authentication_form' : LoginForm}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/signup/$', 'core.views.signup', name='signup'),
    url(r'^accounts/signin/$', 'core.views.signin', name='signin'),

    # main and sidebar
    url(r'^main/$', 'core.views.main', name='main'),
    url(r'^physical/$', 'core.views.physical', name='physical'),
    url(r'^activity/$', 'core.views.activity', name='activity'),
    url(r'^nutrition/$', 'core.views.nutrition', name='nutrition'),
    url(r'^cvd/$', 'core.views.cvd', name='cvd'),
    url(r'^bloodwork/$', 'core.views.bloodwork', name='bloodwork'),

    # top nav bar
    url(r'^personal/$', 'core.views.personal', name='personal'),


    
    url(r'^pre_start/$', 'survey.views.pre_start'),
    

    # questionnaire
    url(r'^main/(?P<client_id>\d+)/preliminary$','survey.views.preliminary', name='preliminary'),
    url(r'^main/preliminary1/$','survey.views.preliminary1', name='preliminary1'),
    url(r'^main/preliminary2/$','survey.views.preliminary2'),
    url(r'^main/preliminary3/$','survey.views.preliminary3'),
    url(r'^main/preliminary4/$','survey.views.preliminary4'),

    # coach view
    url(r'^main/manage_client/$','survey.views.manage_client', name='manage_client'),
    url(r'^main/assignment/(?P<client_id>\d+)$','survey.views.assignment', name='assignment'),
    url(r'^main/deassignment/(?P<client_id>\d+)$','survey.views.deassignment', name='deassignment'),

    url(r'^main/(?P<client_id>\d+)/onboarding1/$','survey.views.onboarding1', name='onboarding1'),
    url(r'^main/(?P<client_id>\d+)/onboarding2/$','survey.views.onboarding2'),
    url(r'^main/(?P<client_id>\d+)/onboarding3/$','survey.views.onboarding3'),
    url(r'^main/(?P<client_id>\d+)/onboarding4/$','survey.views.onboarding4'),
    
    url(r'^main/(?P<client_id>\d+)/age/$','survey.views.get_expected_age'),

    # test
    url(r'^main/(?P<client_id>\d+)/calculator/$', 'survey.views.calculator'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
