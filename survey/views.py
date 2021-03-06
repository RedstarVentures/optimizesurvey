from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from BeautifulSoup import BeautifulSoup

from survey.models import PreAdd, JoyModel1, Preliminary1, Preliminary2, Preliminary3, Preliminary4, Onboarding1, Onboarding2, Onboarding3, Onboarding4
from survey.forms import PreAdd_Questionnaire, JoyForm, Preliminary_1_Questionnaire, Preliminary_2_Questionnaire, Preliminary_3_Questionnaire, Preliminary_4_Questionnaire, Onboarding_1_Questionnaire, Onboarding_2_Questionnaire, Onboarding_3_Questionnaire, Onboarding_4_Questionnaire
from core.models import EmailUser
from core.views import get_user_type
from django import template
import urllib2, urllib, mechanize, datetime, random, csv

register = template.Library()

def preaddq(request):
  data = {}
  form = PreAdd_Questionnaire(request.POST or None, instance=None)
  
  if form.is_valid():
    # form save
    form.save()
    # sync table with user info
    return render_to_response("survey/finish.html", data, context_instance=RequestContext(request))

  data["form"] = form
  return render_to_response("survey/preadd.html", data, context_instance=RequestContext(request))


def joy(request):
  data = {}

  form = JoyForm(request.POST or None, instance=None)

  if form.is_valid():
    # form save
    form.save()
    # sync the table with user information
    return render_to_response("survey/finish.html", data,
                                  context_instance=RequestContext(request))

  data["form"] = form

  return render_to_response("survey/joy.html", data,
                                  context_instance=RequestContext(request))


def calculate_age(month, day, year):
  today=datetime.date.today()
  age = today.year - year
  # unpassed more minus 1
  if month >= today.month:
    if day > today.day:
      age = age-1
  return age

def get_verbose_name(instance, field_name):
  return instance._meta.get_field(field_name).verbose_name
register.filter(get_verbose_name)

def export_csv(request):
  
  coach_email = request.user
  coach = EmailUser.objects.get(email=coach_email)
  client_list = EmailUser.objects.filter(coach=coach.id)


  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="export.csv"'
  writer = csv.writer(response)

  #question list
  
  flag = 0
  #answer list
  for client in client_list:
    try:
      pre1 = Preliminary1.objects.get(user=client)
      pre2 = Preliminary2.objects.get(user=client)
      pre3 = Preliminary3.objects.get(user=client)
      pre4 = Preliminary4.objects.get(user=client)
      on1 = Onboarding1.objects.get(user=client)
      on2 = Onboarding2.objects.get(user=client)
      on3 = Onboarding3.objects.get(user=client)
      on4 = Onboarding4.objects.get(user=client)
    except: # some questionnaire wasn't finished.
      continue
    
    if flag ==0: # the first line of csv file.
      temp_output = []    
      #pre1
      temp_output.append(pre1._meta.get_field("user").verbose_name)
      temp_output.append(pre4._meta.get_field("last_submit_time").verbose_name)
      temp_output.append(pre1._meta.get_field("first_name").verbose_name) 
      temp_output.append(pre1._meta.get_field("last_name").verbose_name)
      temp_output.append(pre1._meta.get_field("gender").verbose_name)
      temp_output.append(pre1._meta.get_field("date_of_birth").verbose_name)
      temp_output.append(pre1._meta.get_field("marital_status").verbose_name)
      temp_output.append(pre1._meta.get_field("in_person_contact").verbose_name)
      temp_output.append(pre1._meta.get_field("formal_education").verbose_name)
      temp_output.append(pre1._meta.get_field("new_relation").verbose_name)
      temp_output.append(pre1._meta.get_field("cope_stress").verbose_name)
      temp_output.append(pre1._meta.get_field("source_of_stress").verbose_name)
      temp_output.append(pre1._meta.get_field("current_work").verbose_name)
      temp_output.append(pre1._meta.get_field("work_hour").verbose_name)
      temp_output.append(pre1._meta.get_field("work_week").verbose_name)
      temp_output.append(pre1._meta.get_field("brain_activity").verbose_name)
      #pre2
      temp_output.append(pre2._meta.get_field("air_pollution").verbose_name)
      temp_output.append(pre2._meta.get_field("seatbelt").verbose_name)
      temp_output.append(pre2._meta.get_field("coffee").verbose_name)
      temp_output.append(pre2._meta.get_field("second_smoke").verbose_name)
      temp_output.append(pre2._meta.get_field("often_smoke").verbose_name)
      temp_output.append(pre2._meta.get_field("many_smoke").verbose_name)
      temp_output.append(pre2._meta.get_field("exposure_smoke").verbose_name)
      temp_output.append(pre2._meta.get_field("lung_disease").verbose_name)
      temp_output.append(pre2._meta.get_field("day_alcohol").verbose_name)
      temp_output.append(pre2._meta.get_field("glass_alcohol").verbose_name)
      temp_output.append(pre2._meta.get_field("aspirin").verbose_name)
      temp_output.append(pre2._meta.get_field("floss_teeth").verbose_name)
      temp_output.append(pre2._meta.get_field("sunscreen").verbose_name)
      temp_output.append(pre2._meta.get_field("body_mass_index").verbose_name)
      #pre3

      #pre4


      writer.writerow(temp_output)

    flag = 1 # finish the first line
    
    # detailed contents (client's answer)
    temp_output=[]
    # pre1
    temp_output.append(getattr(pre1,"user"))
    temp_output.append(getattr(pre4,"last_submit_time"))
    temp_output.append(getattr(pre1,"first_name"))
    temp_output.append(getattr(pre1,"last_name"))
    temp_output.append(pre1._meta.get_field("gender").choices[pre1.gender-1][1])
    temp_output.append(getattr(pre1,"date_of_birth"))
    temp_output.append(pre1._meta.get_field("marital_status").choices[pre1.marital_status-1][1])
    temp_output.append(pre1._meta.get_field("in_person_contact").choices[pre1.in_person_contact-1][1])
    temp_output.append(pre1._meta.get_field("formal_education").choices[pre1.formal_education-1][1])
    temp_output.append(pre1._meta.get_field("new_relation").choices[pre1.new_relation-1][1])
    temp_output.append(pre1._meta.get_field("cope_stress").choices[pre1.cope_stress-1][1])
    text = ""
    for m2m_item in on2.snack.values():
      text += m2m_item['name']+ ", "
    temp_output.append(text)
    temp_output.append(pre1._meta.get_field("current_work").choices[pre1.current_work-1][1])
    temp_output.append(pre1._meta.get_field("work_hour").choices[pre1.work_hour-1][1])
    temp_output.append(pre1._meta.get_field("work_week").choices[pre1.work_week-1][1])
    temp_output.append(pre1._meta.get_field("brain_activity").choices[pre1.brain_activity-1][1])
    #pre2
    temp_output.append(pre2._meta.get_field("air_pollution").choices[pre2.air_pollution-1][1])
    temp_output.append(pre2._meta.get_field("seatbelt").choices[pre2.seatbelt-1][1])
    temp_output.append(pre2._meta.get_field("coffee").choices[pre2.coffee-1][1])
    temp_output.append(pre2._meta.get_field("second_smoke").choices[pre2.second_smoke-1][1])
    temp_output.append(pre2._meta.get_field("often_smoke").choices[pre2.often_smoke-1][1])
    temp_output.append(pre2._meta.get_field("many_smoke").choices[pre2.many_smoke-1][1])
    temp_output.append(pre2._meta.get_field("exposure_smoke").choices[pre2.exposure_smoke-1][1])
    temp_output.append(pre2._meta.get_field("lung_disease").choices[pre2.lung_disease-1][1])
    temp_output.append(pre2._meta.get_field("day_alcohol").choices[pre2.day_alcohol-1][1])
    temp_output.append(pre2._meta.get_field("glass_alcohol").choices[pre2.glass_alcohol-1][1])
    temp_output.append(pre2._meta.get_field("aspirin").choices[pre2.aspirin-1][1])
    temp_output.append(pre2._meta.get_field("floss_teeth").choices[pre2.floss_teeth-1][1])
    temp_output.append(pre2._meta.get_field("sunscreen").choices[pre2.sunscreen-1][1])
    temp_output.append(pre2._meta.get_field("body_mass_index").choices[pre2.body_mass_index-1][1])
    #pre3

    #pre4

    writer.writerow(temp_output)

  return response

@login_required
def preliminary(request, client_id):
  # coach want to see preliminary of client_id
  data = {}
  # are you coach ?
  user = request.user
  try:
    user = EmailUser.objects.get(email=user)
  except:
    raise Http404
  if user.user_type != 2: # if not coach
    raise Http404

  try:
    user = EmailUser.objects.get(id=client_id)
  except:
    raise Http404

  data['client'] = user
  try:
    pre1 = Preliminary1.objects.get(user=user)
  except:
    raise Http404

  data['pre1'] = pre1
  return render_to_response('survey/pre.html', data, context_instance=RequestContext(request))


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
    userinfo.gender = sync_user.gender
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
def assignment(request, client_id):
  # client id
  coach_email = request.user
  coach = EmailUser.objects.get(email=coach_email)
  client = EmailUser.objects.get(id=client_id)
  client.coach = coach
  client.save()  
  return HttpResponseRedirect(reverse('index'))

@login_required
def unassignment(request, client_id):
  # client id
  client = EmailUser.objects.get(id=client_id)
  client.coach = None
  client.save()
  return HttpResponseRedirect(reverse('index'))



@login_required
def onboarding1(request, client_id):
  # don't confuse  client and coach
  coach = request.user
  
  # if client_id is null, go 404
  try:
    client = EmailUser.objects.get(id=client_id)
  except:
    raise Http404

  data = {}

  try:
    pre_demo = Onboarding1.objects.get(user=client)
  except Onboarding1.DoesNotExist:
    pre_demo = None

  form = Onboarding_1_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.onboarding2', kwargs={'client_id':client_id} ))

  if pre_demo is None:
    form.initial['user'] = client

  data["form"] = form

  return render_to_response("survey/on_1.html", data,
                                  context_instance=RequestContext(request))


@login_required
def onboarding2(request, client_id):
  coach = request.user
  # if client_id is null, go 404
  try:
    client = EmailUser.objects.get(id=client_id)
  except:
    raise Http404

  data = {}

  try:
    pre_demo = Onboarding2.objects.get(user=client)
  except Onboarding2.DoesNotExist:
    pre_demo = None

  form = Onboarding_2_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.onboarding3', kwargs={'client_id':client_id} ))

  if pre_demo is None:
    form.initial['user'] = client

  data["form"] = form

  return render_to_response("survey/on_2.html", data,
                                  context_instance=RequestContext(request))

@login_required
def onboarding3(request, client_id):
  coach = request.user
  # if client_id is null, go 404
  try:
    client = EmailUser.objects.get(id=client_id)
  except:
    raise Http404

  data = {}
  try:
    pre_demo = Onboarding3.objects.get(user=client)
  except Onboarding3.DoesNotExist:
    pre_demo = None

  form = Onboarding_3_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('survey.views.onboarding4', kwargs={'client_id':client_id} ))

  if pre_demo is None:
    form.initial['user'] = client

  data["form"] = form
  return render_to_response("survey/on_3.html", data,
                                  context_instance=RequestContext(request))

@login_required
def onboarding4(request, client_id):
  coach = request.user
  # if client_id is null, go 404
  try:
    client = EmailUser.objects.get(id=client_id)
  except:
    raise Http404

  data = {}

  try:
    pre_demo = Onboarding4.objects.get(user=client)
  except Onboarding4.DoesNotExist:
    pre_demo = None

  form = Onboarding_4_Questionnaire(request.POST or None, instance=pre_demo)

  if form.is_valid():

    form.save()
    #
    # aging calc and save!
    calculator(client_id)
    return HttpResponseRedirect(reverse('index'))

  if pre_demo is None:
    form.initial['user'] = client

  data["form"] = form

  return render_to_response("survey/on_4.html", data,
                                  context_instance=RequestContext(request))


def get_expected_age(request, client_id):
  data = {}
  # client_id finished pre & onboard ?

  # if not
    # you have to finish pre & onboard.
    # return

  # if yes
    # make a query for sending to livingto100.
    # get base info
    # connect - all answer to livingto100
    # return your age

  try:
    user = EmailUser.objects.get(id=client_id)
  except:
    raise Http404

  data['client'] = user
  return render_to_response('survey/calc.html', data, context_instance=RequestContext(request))


def calculator(client_id): 

  # get client's information
  try:
    client = EmailUser.objects.get(id=client_id)
  except:
    raise Http404

  # check all data are received successfully.
  try:
    pre1 = Preliminary1.objects.get(user=client)
    pre2 = Preliminary2.objects.get(user=client)
    pre3 = Preliminary3.objects.get(user=client)
    pre4 = Preliminary4.objects.get(user=client)
    on1 = Onboarding1.objects.get(user=client)
    on2 = Onboarding2.objects.get(user=client)
    on3 = Onboarding3.objects.get(user=client)
    on4 = Onboarding4.objects.get(user=client)
    preadd = PreAdd.objects.get(user=client)

  except: # some questionnaire wasn't finished.
    raise Http404

  # user's answer matching!!




  # receive client's data from DB
  dateMonth = [str(client.date_of_birth.month)]
  dateDay = [str(client.date_of_birth.day)]
  dateYear = [str(client.date_of_birth.year)]
  gender = ['M']
  if client.gender == 2:
    gender = ['F']

  # base value 
  country_id = ['230']
  zipcode = '02215'
  accept= ['1']

  # get the age for branch
  age = datetime.date.today().year - client.date_of_birth.year
  if client.date_of_birth.month >= datetime.date.today().month:
    if client.date_of_birth.day > datetime.date.today().day:
      age = age-1

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
  br.form = list(br.forms())[0]
  
  # branch 4 - way
  if age > 38:

    list_sequence = [pre1.marital_status, #q99
                    pre1.new_relation, 
                    pre1.cope_stress,
                    pre1.source_of_stress, # manytomany
                    preadd.sleep_val,# sleep question!!!
                    pre1.formal_education,
                    pre1.work_week,
                    preadd.optimism_val,# optimistic !!!
                    pre1.brain_activity,
                    pre2.air_pollution,
                    pre2.coffee, #21
                    preadd.tea_val,# cups of tea
                    pre2.often_smoke,
                    pre2.many_smoke,
                    pre2.exposure_smoke,
                    pre2.lung_disease, #31
                    pre2.day_alcohol,
                    pre2.glass_alcohol,
                    pre2.aspirin,
                    pre2.sunscreen,
                    pre2.floss_teeth,
                    preadd.weight_val,# weight on3 weight
                    preadd.height_val,# tall on3 height
                    pre2.body_mass_index,
                    on2.many_meat,
                    on2.many_dairy, #51
                    on2.calcium,
                    on2.snack, # manyto many
                    on2.red_meat,
                    on2.sweet,
                    on2.carbohydrate,
                    on2.having_diet,
                    on2.iron,
                    on2.many_exercise,
                    on2.leisure,
                    pre3.bowel_movement,#71
                    pre3.skin_cancer,
                    preadd.hdl_val,# cholesterol (good cholesterol)
                    preadd.ldl_val,# cholesterol (bad cholesterol)
                    preadd.sysbp_val,# on3 : blood_pressure (Systolic) // choice is different male, female
                    preadd.diasbp_val,# on3 : blood_pressure (Diastolic)
                    preadd.glu_val,# fasting blood sugar level
                    pre3.heart_attack,
                    pre3.doctor_appointment,
                    pre4.immediate_family,
                    pre4.cancer_family, #91
                    pre4.family_history #93
                    ]

    if gender[0] == 'M':
      # /start/1 , over 38 and male
    
      idx = 0
      for x in range(1, 94, 2):
        if list_sequence[idx] == -1: # not decided question.
          ran = random.sample(br.form.find_control(str(x)).items, 1)
          br.form[str(x)] = [ran[0].name]
        elif x==17:
          if list_sequence[idx] == 6:
            list_sequence[idx] = 1 # there is no choice at livingto100
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==25:
          if list_sequence[idx] > 2:
            list_sequence[idx]-=1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==31:
          list_sequence[idx]+=1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==67:
          if list_sequence[idx] > 4:
            list_sequence[idx]-=1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==7: # source_of_stress : manytomany
          for checked_box in pre1.source_of_stress.values_list():
            checked_val = '7[' + str(checked_box[0]+22) + ']'
            br.form[checked_val] = [br.form.find_control(checked_val).items[0].name]
        elif x==55: ## 55 snack : manytomany (401-410) 39
          for checked_box in on2.snack.values_list():
            checked_id = checked_box[0]
            if checked_id > 44: # except popcorns
              checked_id += 1
            checked_val = '55[' + str(checked_id+363) + ']'
            br.form[checked_val] = [br.form.find_control(checked_val).items[0].name]
        else: #this is for normal radiocontrol and selectcontrol          
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        idx += 1

    else:
      # /start/2, over 38 and female
      list_sequence += [
                      pre4.fertility,
                      pre4.child_old,
                      pre4.period
                      ]
      idx = 0
      for x in range(2, 95, 2)+[95, 96, 97]:
        if list_sequence[idx] == -1: # not decided question.
          ran = random.sample(br.form.find_control(str(x)).items, 1)
          br.form[str(x)] = [ran[0].name]
        elif x==17:
          if list_sequence[idx] == 6:
            list_sequence[idx] = 1 # there is no choice at livingto100
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==25:
          if list_sequence[idx] > 2:
            list_sequence[idx]-=1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==31:
          list_sequence[idx]+=1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==67:
          if list_sequence[idx] > 4:
            list_sequence[idx]-=1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==8: # source_of_stress : manytomany
          for checked_box in pre1.source_of_stress.values_list():
            checked_val = '8[' + str(checked_box[0]+45) + ']'
            br.form[checked_val] = [br.form.find_control(checked_val).items[0].name]
        elif x==56: ## 55 snack : manytomany
          for checked_box in on2.snack.values_list():
            checked_id = checked_box[0]
            if checked_id > 44: # except popcorns
              checked_id += 1
            checked_val = '56[' + str(checked_id+373) + ']'
            br.form[checked_val] = [br.form.find_control(checked_val).items[0].name]
        else: #this is for normal radiocontrol and selectcontrol          
          try:
            br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
          except:
            pass
        idx += 1
  else:
    list_sequence = [pre1.marital_status, # q99
                      pre1.in_person_contact, #q101
                      -1,# how many new relationship
                      pre1.cope_stress, #q105
                      preadd.sleep_val, #q107 sleep question!!!
                      pre1.formal_education, #q109
                      pre1.work_hour, #q111
                      pre1.work_week, #q113
                      preadd.sleep_val,# optimistic !!!
                      pre2.air_pollution,
                      pre2.seatbelt,
                      pre2.coffee, # 121
                      preadd.tea_val,# cups of tea
                      pre2.second_smoke,
                      pre2.often_smoke,
                      pre2.many_smoke,
                      pre2.exposure_smoke,
                      pre2.lung_disease,
                      pre2.day_alcohol,
                      pre2.glass_alcohol,
                      pre2.aspirin,
                      pre2.sunscreen,# 141
                      preadd.sexdrug_val,# risky sexual behavior and illegal drug
                      pre2.floss_teeth,
                      preadd.weight_val,# weight on3 weight
                      preadd.height_val,# tall on3 height
                      pre2.body_mass_index,
                      on2.many_meat,
                      on2.how_bbq,
                      on2.many_dairy,
                      on2.calcium,
                      on2.snack, # manyto many 161
                      on2.red_meat,
                      on2.sweet,
                      on2.carbohydrate,
                      on2.having_diet,
                      on2.iron,
                      on2.many_exercise, # different
                      on2.leisure,
                      pre3.bowel_movement,
                      pre3.skin_cancer,
                      preadd.hdl_val,# cholesterol (good cholesterol)  # 181
                      preadd.ldl_val,# cholesterol (bad cholesterol)
                      preadd.totchol_val,# total cholesterol level
                      preadd.sysbp_val,# on3 : blood_pressure (Systolic)
                      preadd.diasbp_val,# on3 : blood_pressure (Diastolic)
                      preadd.glu_val,# fasting blood sugar level
                      pre3.heart_attack,
                      pre3.doctor_appointment,
                      pre4.immediate_family,
                      pre4.cancer_family,
                      -2,# complex question (how old and how healthy is/was your mother)
                      -3,# complex question (how old and how healthy is/was your father)
                      pre4.long_live
                      ]

    if gender[0] =='M':
      # /start/3 (99~205), male under 38
      idx = 0
      for x in range(99,206,2):
        if list_sequence[idx] == -1: # not decided question.
          ran = random.sample(br.form.find_control(str(x)).items, 1)
          br.form[str(x)] = [ran[0].name]
        elif list_sequence[idx] == -2: # complex mother
          if pre4.mother_alive == 1: # live
            if pre4.mother_depend == 1: # depend yes
              if pre4.mother_old == 1: # under 80
                br.form[str(x)] = ['7']
              elif pre4.mother_old ==2:
                br.form[str(x)] = ['8']
              elif pre4.mother_old ==3:
                br.form[str(x)] = ['9']
              elif pre4.mother_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.mother_old ==5:
                br.form[str(x)] = ['5']
            else: #no depend
              if pre4.mother_old == 1: # under 80
                br.form[str(x)] = ['1']
              elif pre4.mother_old ==2:
                br.form[str(x)] = ['2']
              elif pre4.mother_old ==3:
                br.form[str(x)] = ['3']
              elif pre4.mother_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.mother_old ==5:
                br.form[str(x)] = ['5']
          elif pre4.mother_alive == 2: # pass away
            if pre4.mother_cause == 1 or pre4.mother_cause == 2:
              br.form[str(x)] = ['6']
            elif pre4.mother_passed_old ==1:
              br.form[str(x)] = ['10']
            elif pre4.mother_passed_old ==2:
              br.form[str(x)] = ['11']
            elif pre4.mother_passed_old ==3:
              br.form[str(x)] = ['12']
            elif pre4.mother_passed_old ==4:
              br.form[str(x)] = ['13']
            elif pre4.mother_passed_old ==5:
              br.form[str(x)] = ['14']
          else: # adopt
            br.form[str(x)] = ['15']

        elif list_sequence[idx] == -3: # complex father
          if pre4.father_alive == 1: # live
            if pre4.father_depend == 1: # depend yes
              if pre4.father_old == 1: # under 80
                br.form[str(x)] = ['7']
              elif pre4.father_old ==2:
                br.form[str(x)] = ['8']
              elif pre4.father_old ==3:
                br.form[str(x)] = ['9']
              elif pre4.father_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.father_old ==5:
                br.form[str(x)] = ['5']
            else: #no depend
              if pre4.father_old == 1: # under 80
                br.form[str(x)] = ['1']
              elif pre4.father_old ==2:
                br.form[str(x)] = ['2']
              elif pre4.father_old ==3:
                br.form[str(x)] = ['3']
              elif pre4.father_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.father_old ==5:
                br.form[str(x)] = ['5']
          elif pre4.father_alive == 2: # pass away
            if pre4.father_cause == 1 or pre4.father_cause == 2:
              br.form[str(x)] = ['6']
            elif pre4.father_passed_old ==1:
              br.form[str(x)] = ['10']
            elif pre4.father_passed_old ==2:
              br.form[str(x)] = ['11']
            elif pre4.father_passed_old ==3:
              br.form[str(x)] = ['12']
            elif pre4.father_passed_old ==4:
              br.form[str(x)] = ['13']
            elif pre4.father_passed_old ==5:
              br.form[str(x)] = ['14']
          else: # adopt
            br.form[str(x)] = ['15']

        elif x==173: # many_exercise
          if list_sequence[idx] == 8: # swap 8, 9
            list_sequence[idx] = 10
          elif list_sequence[idx] > 8:
            list_sequence[idx] -= 1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==161: ## 161 snack : manytomany (1000-1008) 39
          for checked_box in on2.snack.values_list():
            checked_id = checked_box[0]
            if checked_id > 44: # except popcorns
              checked_id += 1
            checked_val = '161[' + str(checked_id+961) + ']'
            br.form[checked_val] = [br.form.find_control(checked_val).items[0].name]
        else: #this is for normal radiocontrol and selectcontrol          
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        idx += 1

    else:
      # /start/4, female under 38
      list_sequence += [pre4.child_old]
      idx = 0
      for x in range(98, 207, 2):
        if list_sequence[idx] == -1: # not decided question.
          ran = random.sample(br.form.find_control(str(x)).items, 1)
          br.form[str(x)] = [ran[0].name]
        elif list_sequence[idx] == -2: # complex mother
          if pre4.mother_alive == 1: # live
            if pre4.mother_depend == 1: # depend yes
              if pre4.mother_old == 1: # under 80
                br.form[str(x)] = ['7']
              elif pre4.mother_old ==2:
                br.form[str(x)] = ['8']
              elif pre4.mother_old ==3:
                br.form[str(x)] = ['9']
              elif pre4.mother_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.mother_old ==5:
                br.form[str(x)] = ['5']
            else: #no depend
              if pre4.mother_old == 1: # under 80
                br.form[str(x)] = ['1']
              elif pre4.mother_old ==2:
                br.form[str(x)] = ['2']
              elif pre4.mother_old ==3:
                br.form[str(x)] = ['3']
              elif pre4.mother_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.mother_old ==5:
                br.form[str(x)] = ['5']
          elif pre4.mother_alive == 2: # pass away
            if pre4.mother_cause == 1 or pre4.mother_cause == 2:
              br.form[str(x)] = ['6']
            elif pre4.mother_passed_old ==1:
              br.form[str(x)] = ['10']
            elif pre4.mother_passed_old ==2:
              br.form[str(x)] = ['11']
            elif pre4.mother_passed_old ==3:
              br.form[str(x)] = ['12']
            elif pre4.mother_passed_old ==4:
              br.form[str(x)] = ['13']
            elif pre4.mother_passed_old ==5:
              br.form[str(x)] = ['14']
          else: # adopt
            br.form[str(x)] = ['15']

        elif list_sequence[idx] == -3: # complex father
          if pre4.father_alive == 1: # live
            if pre4.father_depend == 1: # depend yes
              if pre4.father_old == 1: # under 80
                br.form[str(x)] = ['7']
              elif pre4.father_old ==2:
                br.form[str(x)] = ['8']
              elif pre4.father_old ==3:
                br.form[str(x)] = ['9']
              elif pre4.father_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.father_old ==5:
                br.form[str(x)] = ['5']
            else: #no depend
              if pre4.father_old == 1: # under 80
                br.form[str(x)] = ['1']
              elif pre4.father_old ==2:
                br.form[str(x)] = ['2']
              elif pre4.father_old ==3:
                br.form[str(x)] = ['3']
              elif pre4.father_old ==4:
                br.form[str(x)] = ['4']
              elif pre4.father_old ==5:
                br.form[str(x)] = ['5']
          elif pre4.father_alive == 2: # pass away
            if pre4.father_cause == 1 or pre4.father_cause == 2:
              br.form[str(x)] = ['6']
            elif pre4.father_passed_old ==1:
              br.form[str(x)] = ['10']
            elif pre4.father_passed_old ==2:
              br.form[str(x)] = ['11']
            elif pre4.father_passed_old ==3:
              br.form[str(x)] = ['12']
            elif pre4.father_passed_old ==4:
              br.form[str(x)] = ['13']
            elif pre4.father_passed_old ==5:
              br.form[str(x)] = ['14']
          else: # adopt
            br.form[str(x)] = ['15']

        elif x==172: # many_exercise
          if list_sequence[idx] == 8: # swap 8, 9
            list_sequence[idx] = 10
          elif list_sequence[idx] > 8:
            list_sequence[idx] -= 1
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        elif x==160: ## 160 snack : manytomany (1000-1008) 39
          for checked_box in on2.snack.values_list():
            checked_id = checked_box[0]
            if checked_id > 44: # except popcorns
              checked_id += 1
            checked_val = '161[' + str(checked_id+952) + ']'
            br.form[checked_val] = [br.form.find_control(checked_val).items[0].name]
        else: #this is for normal radiocontrol and selectcontrol          
          br.form[str(x)] = [br.form.find_control(str(x)).items[list_sequence[idx]-1].name]
        idx += 1
    #end for
  br.submit()

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
    client.lifespan = int(resultAge)
    client.save()
  except ValueError, e:
    raise Http404

  return int(resultAge)