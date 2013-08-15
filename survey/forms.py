from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.forms.extras.widgets import SelectDateWidget

from survey.models import MultipleSelect, Preliminary1, Preliminary2, Preliminary3, Preliminary4, Onboarding1, Onboarding2, Onboarding3, Onboarding4
import datetime

BIRTH_YEAR_CHOICES = range(1914,2000)

class Preliminary_1_Questionnaire(forms.ModelForm):

  # model multiple
  multiple_options = MultipleSelect.objects.filter(option=MultipleSelect.OPTION_CHOICES[0][0])
  select_choices = [(s.id, s.name) for s in multiple_options]
  source_of_stress = forms.MultipleChoiceField(choices=select_choices, required=False, widget=forms.CheckboxSelectMultiple, label='Below is a list of typical sources of stress. Check all that you feel are currently stressful to you.')
  date_of_birth = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))

  class Meta:
    model = Preliminary1

  def __init__(self, *args, **kwargs):
    super(Preliminary_1_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields['gender'].widget = forms.Select(choices=Preliminary1.GENDER_CHOICES)
    
    self.fields['marital_status'].widget = forms.RadioSelect(choices=Preliminary1.MARITAL_CHOICES)
    self.fields['in_person_contact'].widget = forms.RadioSelect(choices=Preliminary1.YESNO_CHOICES)
    self.fields['formal_education'].widget = forms.RadioSelect(choices=Preliminary1.EDUCATION_CHOICES)

    self.fields['new_relation'].widget = forms.RadioSelect(choices=Preliminary1.NEW_RELATION_CHOICES) 
    self.fields['cope_stress'].widget = forms.RadioSelect(choices=Preliminary1.STRESS_CHOICES) 
    self.fields['current_work'].widget = forms.RadioSelect(choices=Preliminary1.WORKING_CHOICES) 
    self.fields['work_hour'].widget = forms.RadioSelect(choices=Preliminary1.WORKHOUR_CHOICES) 
    self.fields['work_week'].widget = forms.RadioSelect(choices=Preliminary1.WORKWEEK_CHOICES) 
    self.fields['brain_activity'].widget = forms.RadioSelect(choices=Preliminary1.BRAIN_CHOICES) 
    
class Preliminary_2_Questionnaire(forms.ModelForm):

  class Meta:
    model = Preliminary2

  def __init__(self, *args, **kwargs):
    super(Preliminary_2_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields['air_pollution'].widget = forms.RadioSelect(choices=Preliminary2.AIR_CHOICES)
    self.fields['seatbelt'].widget = forms.RadioSelect(choices=Preliminary2.SEATBELT_CHOICES)
    self.fields['coffee'].widget = forms.RadioSelect(choices=Preliminary2.COFFEE_CHOICES)
    self.fields['second_smoke'].widget = forms.RadioSelect(choices=Preliminary2.YESNO_CHOICES)
    self.fields['often_smoke'].widget = forms.RadioSelect(choices=Preliminary2.OFTEN_SMOKE_CHOICES) 
    self.fields['many_smoke'].widget = forms.RadioSelect(choices=Preliminary2.MANY_SMOKE_CHOICES) 
    self.fields['exposure_smoke'].widget = forms.RadioSelect(choices=Preliminary2.EXPOSURE_CHOICES) 
    self.fields['lung_disease'].widget = forms.RadioSelect(choices=Preliminary2.LUNG_CHOICES) 
    self.fields['day_alcohol'].widget = forms.RadioSelect(choices=Preliminary2.DAY_ALCOHOL_CHOICES) 
    self.fields['glass_alcohol'].widget = forms.RadioSelect(choices=Preliminary2.GLASS_ALCOHOL_CHOICES) 
    self.fields['aspirin'].widget = forms.RadioSelect(choices=Preliminary2.ASPIRIN_CHOICES) 
    self.fields['floss_teeth'].widget = forms.RadioSelect(choices=Preliminary2.YESNO_CHOICES) 
    self.fields['sunscreen'].widget = forms.RadioSelect(choices=Preliminary2.SUNSCREEN_CHOICES) 
    self.fields['body_mass_index'].widget = forms.RadioSelect(choices=Preliminary2.YESNO_CHOICES) 

class Preliminary_3_Questionnaire(forms.ModelForm):

  multiple_options = MultipleSelect.objects.filter(option=MultipleSelect.OPTION_CHOICES[1][0])
  select_choices = [(s.id, s.name) for s in multiple_options]
  have_disease = forms.MultipleChoiceField(choices=select_choices, required=False, widget=forms.CheckboxSelectMultiple, label='Have you ever, or do you now, have any of the following? (check all that apply)')

  class Meta:
    model = Preliminary3

  def __init__(self, *args, **kwargs):
    super(Preliminary_3_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields['bowel_movement'].widget = forms.RadioSelect(choices=Preliminary3.YESNO_CHOICES)
    self.fields['skin_cancer'].widget = forms.RadioSelect(choices=Preliminary3.YESNO_CHOICES)
    self.fields['heart_attack'].widget = forms.RadioSelect(choices=Preliminary3.HEARTATTACK_CHOICES)
    self.fields['doctor_appointment'].widget = forms.RadioSelect(choices=Preliminary3.DOCTOR_CHOICES)

class Preliminary_4_Questionnaire(forms.ModelForm):

  class Meta:
    model = Preliminary4

  def __init__(self, *args, **kwargs):
    super(Preliminary_4_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields['immediate_family'].widget = forms.RadioSelect(choices=Preliminary4.MANY_CHOICES)
    self.fields['cancer_family'].widget = forms.RadioSelect(choices=Preliminary4.MANY_CHOICES)
    self.fields['mother_alive'].widget = forms.RadioSelect(choices=Preliminary4.MOTHER_CHOICES)
    self.fields['mother_old'].widget = forms.RadioSelect(choices=Preliminary4.OLD_CHOICES)
    self.fields['mother_depend'].widget = forms.RadioSelect(choices=Preliminary4.YESNO_CHOICES) 
    self.fields['mother_passed_old'].widget = forms.RadioSelect(choices=Preliminary4.OLD_CHOICES) 
    self.fields['mother_cause'].widget = forms.RadioSelect(choices=Preliminary4.CAUSE_CHOICES)
    self.fields['father_alive'].widget = forms.RadioSelect(choices=Preliminary4.FATHER_CHOICES) 
    self.fields['father_old'].widget = forms.RadioSelect(choices=Preliminary4.OLD_CHOICES) 
    self.fields['father_depend'].widget = forms.RadioSelect(choices=Preliminary4.YESNO_CHOICES) 
    self.fields['father_passed_old'].widget = forms.RadioSelect(choices=Preliminary4.OLD_CHOICES) 
    self.fields['father_cause'].widget = forms.RadioSelect(choices=Preliminary4.CAUSE_CHOICES)
    self.fields['family_history'].widget = forms.RadioSelect(choices=Preliminary4.HISTORY_CHOICES)
    self.fields['long_live'].widget = forms.RadioSelect(choices=Preliminary4.YESNO_CHOICES) 
    self.fields['child_old'].widget = forms.RadioSelect(choices=Preliminary4.CHILD_CHOICES) 


class Onboarding_1_Questionnaire(forms.ModelForm):

  class Meta:
    model = Onboarding1

  def __init__(self, *args, **kwargs):
    super(Onboarding_1_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields['choice_reason'].widget.attrs['rows'] = '5'
    self.fields['health_goal'].widget.attrs['rows'] = '5'
    self.fields['make_change'].widget.attrs['rows'] = '5'
    self.fields['motivate_join'].widget.attrs['rows'] = '5'
    


class Onboarding_2_Questionnaire(forms.ModelForm):

  multiple_options = MultipleSelect.objects.filter(option=MultipleSelect.OPTION_CHOICES[2][0])
  select_choices = [(s.id, s.name) for s in multiple_options]
  limit_activity = forms.MultipleChoiceField(choices=select_choices, required=False, widget=forms.CheckboxSelectMultiple, label='4. Does your health limit you in any activities?')

  multiple_options = MultipleSelect.objects.filter(option=MultipleSelect.OPTION_CHOICES[3][0])
  select_choices = [(s.id, s.name) for s in multiple_options]
  snack = forms.MultipleChoiceField(choices=select_choices, required=False, widget=forms.CheckboxSelectMultiple, label='10. If you snack between meals, generally which of the following are your snacks? Choose all that apply')

  class Meta:
    model = Onboarding2

  def __init__(self, *args, **kwargs):
    super(Onboarding_2_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields['regular_exercise'].widget = forms.RadioSelect(choices=Onboarding2.YESNO_CHOICES)
    self.fields['many_exercise'].widget = forms.RadioSelect(choices=Onboarding2.MANY_EXERCISE_CHOICES)
    self.fields['leisure'].widget = forms.RadioSelect(choices=Onboarding2.LEISURE_CHOICES)
    self.fields['restrict_food'].widget = forms.RadioSelect(choices=Onboarding2.LEISURE_CHOICES)
    self.fields['many_meat'].widget = forms.RadioSelect(choices=Onboarding2.MANY_MEAT_CHOICES)
    self.fields['how_bbq'].widget = forms.RadioSelect(choices=Onboarding2.HOW_BBQ_CHOICES) 
    self.fields['many_dairy'].widget = forms.RadioSelect(choices=Onboarding2.DAIRY_CHOICES) 
    self.fields['calcium'].widget = forms.RadioSelect(choices=Onboarding2.YESNO_CHOICES) 
    self.fields['red_meat'].widget = forms.RadioSelect(choices=Onboarding2.REDMEAT_CHOICES) 
    self.fields['sweet'].widget = forms.RadioSelect(choices=Onboarding2.SWEET_CHOICES) 
    self.fields['carbohydrate'].widget = forms.RadioSelect(choices=Onboarding2.CARBO_CHOICES) 
    self.fields['having_diet'].widget = forms.RadioSelect(choices=Onboarding2.DIET_CHOICES) 
    self.fields['iron'].widget = forms.RadioSelect(choices=Onboarding2.IRON_CHOICES) 

    self.fields['limit_activity_explain'].widget.attrs['rows'] = '2'
    self.fields['restrict_food_explain'].widget.attrs['rows'] = '2'


class Onboarding_3_Questionnaire(forms.ModelForm):

  class Meta:
    model = Onboarding3

  def __init__(self, *args, **kwargs):
    super(Onboarding_3_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields['weight_change'].widget = forms.RadioSelect(choices=Onboarding3.YESNO_CHOICES)
    self.fields['weight_intent'].widget = forms.RadioSelect(choices=Onboarding3.INTENT_CHOICES)
    self.fields['diet_program'].widget = forms.RadioSelect(choices=Onboarding3.YESNO_CHOICES)

    self.fields['weight_18y'].widget.attrs['rows'] = '3'
    self.fields['weight_12m'].widget.attrs['rows'] = '3'
    self.fields['past_diet_program'].widget.attrs['rows'] = '3'
    self.fields['how_program'].widget.attrs['rows'] = '3'
    self.fields['maintain_weight'].widget.attrs['rows'] = '3'
    self.fields['family_weight'].widget.attrs['rows'] = '3'

class Onboarding_4_Questionnaire(forms.ModelForm):

  class Meta:
    model = Onboarding4

  def __init__(self, *args, **kwargs):
    super(Onboarding_4_Questionnaire, self).__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()

    self.fields['fitbit'].widget.attrs['rows'] = '3'
    self.fields['my_net_diary'].widget.attrs['rows'] = '3'
    self.fields['aria_scale'].widget.attrs['rows'] = '3'
    self.fields['diag_visit'].widget.attrs['rows'] = '3'
    self.fields['freq_meet'].widget.attrs['rows'] = '3'
    self.fields['prefer_method'].widget.attrs['rows'] = '3'



