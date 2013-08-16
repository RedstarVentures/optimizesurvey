from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext, Context, Template, loader
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from core.forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from core.models import EmailUser

def get_user_type(u):
  userinfo = EmailUser.objects.get(email=u)
  return userinfo.user_type

@login_required
def main(request):
  data={}
  data['user_type'] = get_user_type(request.user)

  return render_to_response("core/base_main.html", data, context_instance=RequestContext(request))

def nutrition(request):
  data={}
  data['user_type'] = get_user_type(request.user)
  return render_to_response("core/nutrition.html", data, context_instance=RequestContext(request))

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
