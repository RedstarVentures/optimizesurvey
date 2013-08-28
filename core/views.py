from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext, Context, Template, loader
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from core.forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from core.models import EmailUser
from survey.models import Preliminary4, Preliminary1
import datetime

def get_user_type(u):
  userinfo = EmailUser.objects.get(email=u)
  return userinfo.user_type

@login_required
def main(request):
  data={}
  user = request.user
  userinfo = EmailUser.objects.get(email=user)
  
  if userinfo.user_type == 1: # client
    data['client']=userinfo
    return render_to_response("core/base_client.html", data, context_instance=RequestContext(request))
  
  else: # coach
    
    # search his client
    client_list = EmailUser.objects.filter(coach=userinfo.id)
    not_match_client_list = EmailUser.objects.filter(coach__exact=None, user_type=1)
    all_client_list = EmailUser.objects.all()
    # send it using data
    data['clients'] = client_list
    data['not_clients'] = not_match_client_list
    data['all_clients'] = all_client_list
    

    return render_to_response("core/base_coach.html", data, context_instance=RequestContext(request))    

    

@login_required
def physical(request):
  data={}
  return render_to_response("core/measurement.html", data, context_instance=RequestContext(request))

@login_required
def activity(request):
  data={}
  return render_to_response("core/activity.html", data, context_instance=RequestContext(request))

@login_required
def nutrition(request):
  data={}
  data['user_type'] = get_user_type(request.user)
  return render_to_response("core/nutrition.html", data, context_instance=RequestContext(request))

@login_required
def cvd(request):
  data={}
  data['lifespan'] = 0

  # if expected_life exist
  # return
  # else send a msg to client
  return render_to_response("core/cvd.html", data, context_instance=RequestContext(request))

@login_required
def bloodwork(request):
  data={}
  return render_to_response("core/bloodwork.html", data, context_instance=RequestContext(request))

@login_required
def personal(request):
  data={}
  user = request.user
  client = EmailUser.objects.get(email=user)
  data['client'] = client

  try:
    last_answer = Preliminary4.objects.get(user=client.id)
    data['last_submit'] = last_answer.last_submit_time
  except:
    data['last_submit'] = ''
    pass

  # calculator age module
  try:
    today=datetime.date.today()
    age = today.year - client.date_of_birth.year
    # unpassed more minus 1
    if client.date_of_birth.month >= today.month:
      if client.date_of_birth.day > today.day:
        age = age-1
    data['age'] = age
  except:
    data['age'] = '?'

  return render_to_response("core/personal.html", data, context_instance=RequestContext(request))


def signup(request):
  data = {}
  # login and redirect to homepage
  form = SignUpForm(request.POST or None)
  
  if form.is_valid():
    form.save()
    user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
    login(request, user)
    return HttpResponseRedirect(reverse('core.views.main'))

  # if didn't login, return error
  data["signup_form"] = form
  data["next"] = reverse("core.views.main")
  return render(request, "core/signup.html", data)


def signin(request):
  data = {}
  data["form"] = LoginForm()
  data["next"] = reverse("core.views.main")
  return render_to_response('core/signin.html', data, context_instance=RequestContext(request))
