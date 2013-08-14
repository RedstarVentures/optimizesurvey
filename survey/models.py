from django.db import models
from optme import settings

class MultipleSelect(models.Model):

  name = models.CharField(max_length=150)
  OPTION_CHOICES = (
      (0, 'Sources of stress'),
      (1, 'Disease'),
      (2, 'Cause of death'),
      (3, 'Family history')
  )
  option = models.IntegerField(choices=OPTION_CHOICES, default=OPTION_CHOICES[0][0])
  def __unicode__(self):
    return self.name

class Preliminary1(models.Model):
  """
    Preliminary questionnaire 1 of 4 : Demographic and Lifestyle
  """

  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # question 1
  first_name = models.CharField(max_length=32, verbose_name="First name")
  # question 2
  last_name = models.CharField(max_length=32, verbose_name="Last name")
  # question 3
  GENDER_CHOICES = (
      (1, 'Male'),
      (2, 'Female')
  )
  gender = models.IntegerField(choices=GENDER_CHOICES, default=0, verbose_name='Gender')

  # question 4
  date_of_birth = models.DateField(verbose_name='Date of Birth')

  # question 5
  MARITAL_CHOICES = (
      (1, 'Single'),
      (2, 'Married'),
      (3, 'Divorced')
  )
  marital_status = models.IntegerField(choices=MARITAL_CHOICES, verbose_name='Marital Status')

  YESNO_CHOICES = (
      (1, 'Yes'),
      (2, 'No')
  )

  # question 6
  in_person_contact = models.IntegerField(choices=YESNO_CHOICES, verbose_name='Do you have in-person contact with family members, or with friends who are practically like family, at least three times a week?')

  # question 7
  EDUCATION_CHOICES = (
      (1, 'Advanced Degree (Masters, Doctorate)'),
      (2, 'College Degree (Bachelors, Associates)'),
      (3, 'High School Degree or Equivalent'),
      (4, 'Some High School'),
      (5, 'Working on an advanced degree'),
      (6, 'Working on a college degree')
    )
  formal_education = models.IntegerField(choices=EDUCATION_CHOICES, verbose_name='How much formal education do you have?')

  #question 8
  NEW_RELATION_CHOICES = (
      (1, '7 or more'),
      (2, '4 - 6'),
      (3, '1 - 3'),
      (4, '0')
    )
  new_relation = models.IntegerField(choices=NEW_RELATION_CHOICES, verbose_name='How many new relationships/friendships have you developed over the last 12 months? (Relationship defined as contact with someone regularly- a minimum of once a week)?')

  #q9
  STRESS_CHOICES = (
      (1, 'Very well! It helps me to get motivated'),
      (2, 'Good! I can shed stress by using techniques that reduce stress (meditation, exercise, etc.)'),
      (3, 'I am doing all right! I am trying to find ways to protect myself from it.'),
      (4, 'Not very good! Stress eats away at me and I cannot seem to shake it off.')
    )

  cope_stress = models.IntegerField(choices=STRESS_CHOICES, verbose_name='How do you usually cope with your stress?')

  #q10 (MtoM)
  source_of_stress = models.ManyToManyField(MultipleSelect, verbose_name='Below is a list of typical sources of stress. Check all that you feel are currently stressful to you.')

  #q11
  WORKING_CHOICES = (
      (1, 'Yes (including stay-at-home parents)'),
      (2, 'No / retired')
    )

  current_work = models.IntegerField(choices=WORKING_CHOICES, verbose_name='Are you currently working?')

  #q12
  WORKHOUR_CHOICES = (
      (1, '40 hours or fewer'),
      (2, '41 - 60 hours'),
      (3, '61 - 80 hours'),
      (4, 'More than 80 hours'),
      (5, 'I am retired or I am not working')      
    )

  work_hour = models.IntegerField(choices=WORKHOUR_CHOICES, verbose_name='How many hours per week do you work, including your commute time?')

  #q13
  WORKWEEK_CHOICES = (
      (1, 'Fewer than 5 days'),
      (2, '6 days'),
      (3, '7 days'),
      (4, 'I am retired or I am not working')      
    )

  work_week = models.IntegerField(choices=WORKWEEK_CHOICES, verbose_name='How many days per week do you work?')
  
  #q14
  BRAIN_CHOICES = (
      (1, 'At least 2 times a week'),
      (2, 'Once a week'),
      (3, '7 days'),
      (4, 'Between once a week and once a month'),
      (5, 'Rarely'),
      (6, 'Not at all')
    )

  brain_activity = models.IntegerField(choices=BRAIN_CHOICES, verbose_name='Do you regularly engage in brain activities that are both new and challenging to you (e.g. learning a new subject, playing someone in a hard game such as chess or scrabble, solving crossword or Sudoku puzzles)?')



class Preliminary2(models.Model):
  """
    Preliminary questionnaire 2 of 4 : Environmental Risk Assessment
  """

  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # frequency choice
  YESNO_CHOICES = (
      (1, 'Yes'),
      (2, 'No')
  )

  # question 1
  AIR_CHOICES = (
      (1, 'Very bad! (Industrial area/lots of smog)'),
      (2, 'Average (Urban area/medium smog)'),
      (3, 'Okay (Suburbs/low smog)'),
      (4, 'Very good! (Country side/no smog)')
  )
  air_pollution = models.IntegerField(choices=AIR_CHOICES, default=0, verbose_name='How is the air quality (air pollution) where you live?')

  # question 2
  SEATBELT_CHOICES = (
      (1, 'Always'),
      (2, 'About 80% of the time'),
      (3, 'Half of the time'),
      (4, 'Less than half of the time')
  )
  seatbelt = models.IntegerField(choices=SEATBELT_CHOICES, verbose_name='How often do you wear a seatbelt when you are driving in a car (either as driver or passenger)?')

  # question 3
  COFFEE_CHOICES = (
      (1, 'None'),
      (2, '1 to 2 cups'),
      (3, '3 or more cups')
    )
  coffee = models.IntegerField(choices=COFFEE_CHOICES, verbose_name='How many cups of caffeinated coffee do you drink per day?')

  # question 4
  second_smoke = models.IntegerField(choices=YESNO_CHOICES, verbose_name='Do you smoke or are you exposed to second-hand smoke?')

  #question 5
  OFTEN_SMOKE_CHOICES = (
      (1, 'Daily'),
      (2, 'Not daily, but often'),
      (3, 'Sometimes'),
      (4, 'Rarely or never')
    )
  often_smoke = models.IntegerField(choices=OFTEN_SMOKE_CHOICES, verbose_name='How often do you smoke or chew tobacco?')

  #q6
  MANY_SMOKE_CHOICES = (
      (1, 'None'),
      (2, '1 cigarette to half a pack'),
      (3, '1 pack'),
      (4, '1 and a half packs'),
      (5, '2 packs'),
      (6, '3 or more packs')
    )
  many_smoke = models.IntegerField(choices=MANY_SMOKE_CHOICES, verbose_name='How many cigarettes do you smoke per day?')

  #q7
  EXPOSURE_CHOICES = (
      (1, 'Daily and prolonged'),
      (2, 'Not daily, but often and prolonged'),
      (3, 'At least once a week and prolonged'),
      (4, 'Rarely or never')
    )
  exposure_smoke = models.IntegerField(choices=EXPOSURE_CHOICES, verbose_name='What is your exposure to close-proximity second-hand smoke? Answer even if you also smoke')

  #q8
  LUNG_CHOICES = (
      (1, 'I did not smoke in the past'),
      (2, 'As a result of smoking, I have been diagnosed with emphysema or chronic obstructive lung disease (COPD)'),
      (3, 'I still smoke or have quit and seem to have minimal or no lung problems')
    )
  lung_disease = models.IntegerField(choices=LUNG_CHOICES, verbose_name='Do you have any lung disease as a result of smoking in the past?')

  #q9
  DAY_ALCOHOL_CHOICES = (
      (1, 'I don\'t drink alcohol'),
      (2, '1 or 2 days per week'),
      (3, '3 or 5 days per week'),
      (4, '6 or 7 days per week')
    )
  day_alcohol = models.IntegerField(choices=DAY_ALCOHOL_CHOICES, verbose_name='How many days per week do you usually consume alcohol?')
  
  #q10
  GLASS_ALCOHOL_CHOICES = (
      (1, 'I don\'t drink'),
      (2, '1 to 2'),
      (3, '3'),
      (4, 'Over 3')
    )
  glass_alcohol = models.IntegerField(choices=GLASS_ALCOHOL_CHOICES, verbose_name='On the days when you drink alcoholic beverages (beer, wine, liquor and mixed drinks) how many glasses do you usually drink?')

  #q11
  ASPIRIN_CHOICES = (
      (1, 'Never'),
      (2, 'Occasionally'),
      (3, 'Frequently'),
      (4, 'Every day')
    )
  aspirin = models.IntegerField(choices=ASPIRIN_CHOICES, verbose_name='How often do you take aspirin (eg. 81-325 mg)?')
  
  #q12
  floss_teeth = models.IntegerField(choices=YESNO_CHOICES, verbose_name='Do you floss your teeth every day?')
  
  #q13
  SUNSCREEN_CHOICES = (
      (1, 'Rarely or never'),
      (2, 'Sometimes'),
      (3, 'Most of the time'),
      (4, 'Always')
    )
  sunscreen = models.IntegerField(choices=SUNSCREEN_CHOICES, verbose_name='Do you wear sunscreen (at least SPF 30) or protective clothing when you spend time in the sun?')
  
  #q14
  body_mass_index = models.IntegerField(choices=YESNO_CHOICES, verbose_name='Do you body build or strength train to the degree that your body mass index is high because of muscle, not because of fat?')


class Preliminary3(models.Model):
  """
    Preliminary questionnaire 3 of 4 : Personal Medical History
  """

  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # frequency choice
  YESNO_CHOICES = (
      (1, 'Yes'),
      (2, 'No')
  )

  # question 1
  bowel_movement = models.IntegerField(choices=YESNO_CHOICES, default=0, verbose_name='Do you have a bowel movement at least once every two days?')

  # question 2
  skin_cancer = models.IntegerField(choices=YESNO_CHOICES, default=0, verbose_name='Do you regularly screen for skin cancer by doing self-examinations and have regular screenings by your health care provider for breast or testicular cancer?')

  # q3
  HEARTATTACK_CHOICES = (
      (1, 'No heart attack'),
      (2, 'Yes, I had a heart attack more than 2 years ago'),
      (3, 'Yes, I had a heart attack within the past 2 years, and I took action to reduce my risk factors for another one (regular exercise, stop smoking, lose weight, changed diet)'),
      (4, 'Yes, I had a heart attack within the past 2 years, and I HAVE NOT taken action to reduce my risk factors for another one')
  )
  heart_attack = models.IntegerField(choices=HEARTATTACK_CHOICES, verbose_name='Have you had a heart attack?')

  # question 4
  DOCTOR_CHOICES = (
      (1, 'Over 3 years ago'),
      (2, 'Between 1-3 years ago'),
      (3, 'Within the past year')
    )
  doctor_appointment = models.IntegerField(choices=DOCTOR_CHOICES, verbose_name='When did you have your last doctor\'s appointment for your regular medical check-up (which includes blood pressure check, age- and gender-appropriate screenings, immunizations, review of medical history, and analysis about your risk factors)?')

  #q5 (MtoM)
  have_disease = models.ManyToManyField(MultipleSelect, verbose_name='Below is a list of typical sources of stress. Check all that you feel are currently stressful to you.', related_name='survey_multiple_2')


class Preliminary4(models.Model):
  """
    Preliminary questionnaire 4 of 4 : Family Medical History
  """

  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # frequency choice
  YESNO_CHOICES = (
      (1, 'Yes'),
      (2, 'No')
  )

  # question 1
  MANY_CHOICES = (
      (1, 'None'),
      (2, 'One'),
      (3, 'Two'),
      (4, 'Three or more'),
      (5, 'I don\'t know')
  )
  immediate_family = models.IntegerField(choices=MANY_CHOICES, verbose_name='How many members of your immediate family (parents and brothers and sisters) have diabetes or have had a heart attack?')

  # question 2
  cancer_family = models.IntegerField(choices=MANY_CHOICES, verbose_name='How many non-smoking members of your family (grandparents, parents, brothers and sisters) were diagnosed with cancer (other than benign skin cancers)?')

  # question 3
  MOTHER_CHOICES = (
      (1, 'Yes'),
      (2, 'No'),
      (3, 'I don\'t know (I am adopted or I have losted touch with my mother)')
    )
  mother_alive = models.IntegerField(choices=MOTHER_CHOICES, verbose_name='Is your mother alive?')

  # question 4
  OLD_CHOICES = (
      (0, 'N/A'),
      (1, 'Under 80'),
      (2, '80 - 89'),
      (3, '90 - 94'),
      (4, '95 - 99'),
      (5, 'Above 100')
    )
  mother_old = models.IntegerField(choices=OLD_CHOICES, verbose_name='How old is your mother?')

  #question 5
  mother_depend = models.IntegerField(choices=YESNO_CHOICES, verbose_name='Does your mother depend on others?')

  #q6
  mother_passed_old = models.IntegerField(choices=OLD_CHOICES, verbose_name='How old was your mother when she passed away?')

  CAUSE_CHOICES = (
      (1, "Smoking related illness (cancer, heart attack, emphysema)"),
      (2, 'Trauma prior to age 80'),
      (3, 'Trauma after age 80'),
      (4, 'Natural cause'),
      (5, 'Other cause')
    )
  #q7
  mother_cause = models.IntegerField(choices=CAUSE_CHOICES, verbose_name='What was your mother\'s cause of death?')
  
  # question 8
  FATHER_CHOICES = (
      (1, 'Yes'),
      (2, 'No'),
      (3, 'I don\'t know (I am adopted or I have losted touch with my father)')
    )
  father_alive = models.IntegerField(choices=FATHER_CHOICES, verbose_name='Is your father alive?')

  # question 9
  father_old = models.IntegerField(choices=OLD_CHOICES,  verbose_name='How old is your father?')

  #question 10
  father_depend = models.IntegerField(choices=YESNO_CHOICES, verbose_name='Does your father depend on others?')

  #q11
  father_passed_old = models.IntegerField(choices=OLD_CHOICES,  verbose_name='How old was your father when he passed away? ')

  #q12
  father_cause = models.IntegerField(choices=CAUSE_CHOICES, verbose_name='What was your father\'s cause of death?')
  
  HISTORY_CHOICES = (
      (1, "Generally, my relatives passed away in their 60s and 70s (or earlier)"),
      (2, "Generally, my relatives passed away in their 80s"),
      (3, 'I have at least one relative who lived into their 90s'),
      (4, 'I have at least one relative who lived to age 100 or older'),
      (5, 'I do not know my family history')
    )
  #q13
  family_history = models.IntegerField(choices=HISTORY_CHOICES, verbose_name='Concerning the longevity in your family, including your grandparents, parents, aunts and uncles, and your brothers and sisters, which one of the following fits you best?')

  #q14
  long_live = models.IntegerField(choices=YESNO_CHOICES, verbose_name='Did any of your grandparents or great-grandparents live to age 98 years or older?')
  
  #q15
  CHILD_CHOICES = (
      (1, 'I have not had nay children'),
      (2, 'Younger than 34'),
      (3, '35 - 39'),
      (4, '40 - 44'),
      (5, 'Older than 45')
    )
  child_old = models.IntegerField(choices=CHILD_CHOICES, verbose_name='How old were you when you last had a child without fertility technology assistance?')










