from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from BeautifulSoup import BeautifulSoup

from survey.models import Preliminary1, Preliminary2, Preliminary3, Preliminary4, Onboarding1, Onboarding2, Onboarding3, Onboarding4
from survey.forms import Preliminary_1_Questionnaire, Preliminary_2_Questionnaire, Preliminary_3_Questionnaire, Preliminary_4_Questionnaire, Onboarding_1_Questionnaire, Onboarding_2_Questionnaire, Onboarding_3_Questionnaire, Onboarding_4_Questionnaire
from core.models import EmailUser
from core.views import get_user_type
import urllib2, urllib, mechanize, datetime, random

def home(request):
	data = {}

	return render_to_response('core/home.html', data, context_instance=RequestContext(request))


def calculate_age(month, day, year):
	today=datetime.date.today()
	age = today.year - year
	# unpassed more minus 1
	if month >= today.month:
		if day > today.day:
			age = age-1
		
	return age

def pre_start(request):
	data = {}
	return render_to_response('survey/pre.html', data, context_instance=RequestContext(request))

@login_required
def preliminary(request, client_id):

  return


@login_required
def preliminary1(request):
  u = request.user
  data = {}
  data['user_type'] = get_user_type(u)
  userinfo = EmailUser.objects.get(email=u)
  try:
    pre_demo = Preliminary1.objects.get(user=u)
  except Preliminary1.DoesNotExist:
    pre_demo = None

  form = Preliminary_1_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    # form save
    form.save()
    # sync the table with user information
    sync_user = Preliminary1.objects.get(user=u)
    userinfo.first_name = sync_user.first_name
    userinfo.last_name = sync_user.last_name
    userinfo.date_of_birth = sync_user.date_of_birth
    userinfo.save()

    return HttpResponseRedirect(reverse('survey.views.preliminary2'))

  if pre_demo is None:
    form.initial['user'] = u

  data["form"] = form

  return render_to_response("survey/pre_1.html", data,
                                  context_instance=RequestContext(request))

@login_required
def preliminary2(request):
  u = request.user
  
  data = {}
  data['user_type'] = get_user_type(u)
  try:
    pre_demo = Preliminary2.objects.get(user=u)
  except Preliminary2.DoesNotExist:
    pre_demo = None

  form = Preliminary_2_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.preliminary3'))

  if pre_demo is None:
    form.initial['user'] = u

  data["form"] = form

  return render_to_response("survey/pre_2.html", data,
                                  context_instance=RequestContext(request))

@login_required
def preliminary3(request):
  u = request.user
  data = {}
  data['user_type'] = get_user_type(u)
  
  try:
    pre_demo = Preliminary3.objects.get(user=u)
  except Preliminary3.DoesNotExist:
    pre_demo = None

  form = Preliminary_3_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.preliminary4'))

  if pre_demo is None:
    form.initial['user'] = u

  data["form"] = form
  return render_to_response("survey/pre_3.html", data,
                                  context_instance=RequestContext(request))

@login_required
def preliminary4(request):
  u = request.user
  data = {}
  data['user_type'] = get_user_type(u)
  try:
    pre_demo = Preliminary4.objects.get(user=u)
  except Preliminary4.DoesNotExist:
    pre_demo = None

  form = Preliminary_4_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():

    form.save()
    return render_to_response("survey/finish.html", data, context_instance=RequestContext(request))

  if pre_demo is None:
    form.initial['user'] = u

  data["form"] = form

  return render_to_response("survey/pre_4.html", data,
                                  context_instance=RequestContext(request))

@login_required
def manage_client(request):
  data = {}
  coach = request.user

  #is he a real coach?
  checkinfo = EmailUser.objects.get(email=coach)
  if checkinfo.user_type >= 2:
    
    # search his client
    client_list = EmailUser.objects.filter(coach=checkinfo.id)
    not_match_client_list = EmailUser.objects.filter(coach__exact=None, user_type=1)
    # send it using data
    data['clients'] = client_list
    data['not_clients'] = not_match_client_list
    data['user_type'] = checkinfo.user_type

    return render_to_response('survey/manage_client.html', data, context_instance=RequestContext(request))

  else: # he is not a coach !
    raise Http404

@login_required
def assignment(request, client_id):
  # client id
  coach_email = request.user
  coach = EmailUser.objects.get(email=coach_email)
  client = EmailUser.objects.get(id=client_id)
  client.coach = coach
  client.save()  
  return HttpResponseRedirect('/main/manage_client/')

@login_required
def deassignment(request, client_id):
  # client id
  client = EmailUser.objects.get(id=client_id)
  client.coach = None
  client.save()
  return HttpResponseRedirect('/main/manage_client/')

@login_required
def onboarding1(request, client_id):
  # don't confuse  client and coach
  coach = request.user
  
  # if u is null, go 404
  if client_id =='':
    raise Http404

  data = {}
  data['user_type'] = get_user_type(coach)
  try:
    pre_demo = Onboarding1.objects.get(user=client_id)
  except Onboarding1.DoesNotExist:
    pre_demo = None

  form = Onboarding_1_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.Onboarding2'))

  if pre_demo is None:
    form.initial['user'] = client_id

  data["form"] = form

  return render_to_response("survey/on_1.html", data,
                                  context_instance=RequestContext(request))


@login_required
def onboarding2(request):
  u = request.POST.get('user','')
  # if u is null, go 404
  if u =='':
    raise Http404

  data = {}
  data['user_type'] = get_user_type(u)
  try:
    pre_demo = Onboarding2.objects.get(user=u)
  except Onboarding2.DoesNotExist:
    pre_demo = None

  form = Onboarding_2_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.Onboarding3'))

  if pre_demo is None:
    form.initial['user'] = u

  data["form"] = form

  return render_to_response("survey/on_2.html", data,
                                  context_instance=RequestContext(request))

@login_required
def onboarding3(request):
  u = request.POST.get('user','')
  # if u is null, go 404
  if u =='':
    raise Http404
  
  data = {}
  data['user_type'] = get_user_type(u)
  try:
    pre_demo = Onboarding3.objects.get(user=u)
  except Onboarding3.DoesNotExist:
    pre_demo = None

  form = Onboarding_3_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.Onboarding4'))

  if pre_demo is None:
    form.initial['user'] = u

  data["form"] = form
  return render_to_response("survey/on_3.html", data,
                                  context_instance=RequestContext(request))

@login_required
def onboarding4(request):
  u = request.POST.get('user','')
  # if u is null, go 404
  if u =='':
    raise Http404
  
  data = {}
  data['user_type'] = get_user_type(u)
  try:
    pre_demo = Onboarding4.objects.get(user=u)
  except Onboarding4.DoesNotExist:
    pre_demo = None

  form = Onboarding_4_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():

    form.save()
    return render_to_response("survey/finish.html", data, context_instance=RequestContext(request))

  if pre_demo is None:
    form.initial['user'] = u

  data["form"] = form

  return render_to_response("survey/on_4.html", data,
                                  context_instance=RequestContext(request))


def get_expected_age(request, client_id):
  data = {}
  # client_id finished pre & onboard ?

  # if not

  # if yes
    # make a query for sending to livingto100.
    # get base info
    # connect - all answer to livingto100
    #
  data['output'] = 'Your calculated life expectancy is 132. Unbelievable !!'
  return render_to_response('survey/calc.html', data, context_instance=RequestContext(request))

def getbaseinfo(request):
	data = {}
	date_month=request.POST.get('date[month]', '')
	date_day=request.POST.get('date[day]', '')
	date_year=request.POST.get('date[year]', '')
	gender=request.POST.get('gender', '')
	country_id=request.POST.get('country_id', '')
	zipcode=request.POST.get('zipcode', '')
	
	if date_month=='' or date_day=='' or date_year=='' or gender=='' or country_id=='' or zipcode=='':
		return HttpResponse("error : blank form")

	age = calculate_age(int(date_month), int(date_day), int(date_year))
	if age < 13 or age > 99:
		return HttpResponse("unsupporting age : 13~99, your age is %s" % age)

	data['date'] = date_month
	return render_to_response('survey/question.html', data, context_instance=RequestContext(request))

def calculator(request):	

	# receive user's data from DB
	# be careful of sequence
	dateMonth = ['6']
	dateDay = ['10']
	dateYear = ['1987']
	gender = ['M']
	country_id = ['230']
	zipcode = '02215'
	accept= ['1']

	# user's answer
	# At the moment, Random variable!!
	# Todo : Called from DB

	# check all data are received successfully.

	# calculate the User Age
	age = calculate_age(int(dateMonth[0]), int(dateDay[0]), int(dateYear[0]))
	# external
	if age < 13 or age > 99:
		assert "unsupported age"

	# Target site
	br = mechanize.Browser()
	url = 'https://livingto100.com'

	br.open(url+'/calculator')
	br.form = list(br.forms())[0]
	br.form['date[month]'] = dateMonth
	br.form['date[day]'] = dateDay
	br.form['date[year]'] = dateYear
	br.form['gender'] = gender
	br.form['country_id'] = country_id
	br.form['zipcode'] = zipcode
	br.form['accept'] = accept
	br.submit()

	flag=0
	br.form = list(br.forms())[0]
	# branch 4 - way
	if age > 38:
		if gender[0] == 'M':
			# /start/1
			for x in range(1, 94, 2):
				if x != 7 and x != 55:
					#this is for normal radiocontrol and selectcontrol
					ran = random.sample(br.form.find_control(str(x)).items, 1)
					br.form[str(x)] = [ran[0].name] # warning of list
				elif x==7:
					#this is for checkbox control
					br.form['7[23]'] = ['E']
					# for until 7[45]
				else:
					#another checkbox control
					br.form['55[401]'] = ['I']
					# for until 55[410]
		else:
			# /start/2
			for x in range(2, 95, 2)+[95, 96, 97]:
				if x != 8 and x != 56:
					ran = random.sample(br.form.find_control(str(x)).items, 1)
					br.form[str(x)] = [ran[0].name] # warning of list
				elif x==8:
					br.form['8[46]'] = ['E']
					#for until 8[68]
				else:
					br.form['56[411]'] = ['I']
					#for until 56[420]
	else:
		if gender[0] =='M':
			# /start/3 (99~205)
			for x in range(99,206,2):
				if x == 161:
					br.form['161[1000]'] = ['F']
					#for until 161[1008]
				else:
					ran = random.sample(br.form.find_control(str(x)).items, 1)
					br.form[str(x)] = [ran[0].name] # warning of list
		else:
			# /start/4
			for x in range(98, 207, 2):
				if x == 160:
					br.form['160[991]'] = ['F']
					#for until 160[999]
				else:
					ran = random.sample(br.form.find_control(str(x)).items, 1)
					br.form[str(x)] = [ran[0].name] # warning of list


	br.submit()
	# usage of mechanize
	# len(br.form.find_control('190').items)
	# br.form.find_control('190').items[0].name
	# a = random.sample(br.form.find_control('190').items, 1)
	# a[0].name
	
	# Temporary login module to livingto100
	br.open(url+'/users/sign_in')
	br.form = list(br.forms())[0]
	br.form['user[email]'] = 'optme@optme.com'
	br.form['user[password]'] = 'redstar123'
	submitLogin = br.submit()
	
	# Result Analysis start
	soup = BeautifulSoup(submitLogin)
	image_tags = soup.findAll('img')

	resultAge = image_tags[2]['alt']
	try:
		check = int(resultAge)
		output = "Your calculated life expectancy is "+ resultAge
	except ValueError, e:
		output = "Something wrong with calculating ! It needs repair"
	data = {}
	data['output'] = output
	return render_to_response('survey/calc.html', data, context_instance=RequestContext(request))
