from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from BeautifulSoup import BeautifulSoup
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
		output = "Something wrong with calculating"
	data = {}
	data['output'] = output
	return render_to_response('survey/calc.html', data, context_instance=RequestContext(request))
