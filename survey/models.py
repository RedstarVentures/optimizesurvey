from django.db import models
from optme import settings

class MultipleSelect(models.Model):

  name = models.CharField(max_length=150)
  OPTION_CHOICES = (
      (0, 'Sources of stress'),
      (1, 'Disease'),
      (2, 'Limiting activity'),
      (3, 'snack')
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
  date_of_birth = models.DateField(verbose_name='Date of birth')

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


# 
class Onboarding1(models.Model):
  """
    In-person Onboarding visit 1 of 4 : Motivation for Joining OptMe
  """
  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # question 1
  choice_reason = models.TextField(verbose_name="1. Can you briefly explain why you chose to join OptMe?")
  # question 2
  health_goal = models.TextField(verbose_name="2. Do you have any specific health-related goals?")
  # question 3
  make_change = models.TextField(verbose_name='3. Are you interested in making any specific changes?')
  # question 4
  motivate_join = models.TextField(verbose_name='4. What motivated you to join OptMe?')


class Onboarding2(models.Model):
  """
    In-person Onboarding visit 2 of 4 : Live to 100 and Diet History
  """

  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # frequency choice
  YESNO_CHOICES = (
      (1, 'Yes'),
      (2, 'No')
  )
  # q1
  regular_exercise = models.IntegerField(choices=YESNO_CHOICES, verbose_name='1. Do you currently exercise regularly?')

  # question 2
  MANY_EXERCISE_CHOICES = (
      (1, '7'),
      (2, '6'),
      (3, '5'),
      (4, '4'),
      (5, '3'),
      (6, '2'),
      (7, '1'),
      (8, 'I get the equivalent of 30 or more minutes of exercise that significantly raises my heart rate through my job'),
      (9, 'I don\'t exercise')

  )
  many_exercise = models.IntegerField(choices=MANY_EXERCISE_CHOICES, verbose_name='2. How many days a week do you exercise (strength training, aerobic exercises or activities such as swimming, running, strenuous walking and biking) for at least 30 minutes a day?')

  # question 3
  LEISURE_CHOICES = (
      (1, 'Generally engaged in some physically active activity'),
      (2, 'Not at all'),
      (3, 'Something in between')
    )
  leisure = models.IntegerField(choices=LEISURE_CHOICES, verbose_name='3. Aside from exercise, during your leisure time, are you:')

  # question 4
  limit_activity = models.ManyToManyField(MultipleSelect, verbose_name='4. Does your health limit you in any activities?', related_name='limit_activity')
  limit_activity_explain = models.TextField(null=True, blank=True, verbose_name='If check to any activities in 4., please explain')
  
  # question 5
  restrict_food = models.IntegerField(choices=YESNO_CHOICES, verbose_name='5. Do you have any medical conditions, cultural/religious commitments or food allergies that restrict you from eating certain foods?')
  restrict_food_explain = models.TextField(null=True, blank=True, verbose_name='If answer Yes to 5., what are they?')
  
  #question 6
  MANY_MEAT_CHOICES = (
      (1, 'None'),
      (2, '1 - 2 servings'),
      (3, '3 - 4 servings'),
      (4, 'Over 5 servings')
    )
  many_meat = models.IntegerField(choices=MANY_MEAT_CHOICES, verbose_name='6. How many servings of processed meats of fast foods, excluding hamburgers (like hotdogs, chicken nuggets, bologna) do you eat per week?')

  #q7
  HOW_BBQ_CHOICES = (
      (1, 'I am a vegetarian'),
      (2, 'I never barbecue'),
      (3, 'I put aluminum foil on the grill'),
      (4, 'Lightly grilled'),
      (5, 'Almost charred or charred')
    )
  how_bbq = models.IntegerField(choices=HOW_BBQ_CHOICES, verbose_name='7. How do you barbecue fish, poultry, or meat?')

  #q8
  DAIRY_CHOICES = (
      (1, '0 - 1 servings'),
      (2, '2 - 3 servings'),
      (3, 'More than 3 servings')
    )
  many_dairy = models.IntegerField(choices=DAIRY_CHOICES, verbose_name='8. How many servings of dairy products (milk, cheese, yogurt, etc.) do you eat per day?  (Example for 1 serving: 1 cup of milk, 1 cup of yogurt, or 1/2 oz. cheese).')

  #q9
  calcium = models.IntegerField(choices=YESNO_CHOICES, verbose_name='9. Do you take supplemental calcium?')
  
  #q10
  snack = models.ManyToManyField(MultipleSelect, verbose_name='10. If you snack between meals, generally which of the following are your snacks? Choose all that apply', related_name = 'snack')

  #q11
  REDMEAT_CHOICES = (
      (1, 'I don\'t eat red meat'),
      (2, 'I eat red meat 1-2 days per week'),
      (3, 'I eat red meat 3-5 days per week'),
      (4, 'I eat red meat 6-7 days per week')
    )
  red_meat = models.IntegerField(choices=REDMEAT_CHOICES, verbose_name='11. How often per week do you have red meat as your main course?')
  
  #q12
  SWEET_CHOICES = (
      (1, 'I avoid sweets'),
      (2, '1-2 days per week'),
      (3, '3-5 days per week'),
      (4, 'Once a day'),
      (5, 'More than once a day')
    )
  sweet = models.IntegerField(choices=SWEET_CHOICES, verbose_name='12. How often do you eat sweets such as ice cream, cake, pie, pastry, or candy bars?')
  
  #q13
  CARBO_CHOICES = (
      (1, '3+ servings/day'),
      (2, '1-2 servings/day'),
      (3, '1 serving every other day'),
      (4, '1 serving 2x/week'),
      (5, '1 or fewer servings a week')
    )
  carbohydrate = models.IntegerField(choices=CARBO_CHOICES, verbose_name='13. What about carbohydrates like white bread or rolls, potatoes, French fries, pasta, white rice (basically anything white)? If one meal\'s worth of each one of these counted as 1 serving of simple carbohydrate, how many servings of these do you have?')
  
  #q14
  DIET_CHOICES = (
      (1, 'I eat too much everyday, making it easy for me to stay overweight or to gain more weight'),
      (2, 'I eat such that I am losing weight with a target of reaching a healthy weight'),
      (3, 'I am maintaining a healthy weight with the way I currently eat')
    )
  having_diet = models.IntegerField(choices=DIET_CHOICES, verbose_name='14. Do you have a diet that leads to weight gain, or do you have a diet that maintains a healthy weight or is conducive to healthy weight loss?')
  
  #q15
  IRON_CHOICES = (
      (1, 'Yes'),
      (2, 'No'),
      (3, 'Yes, but it relieves symptoms related to my anemia (low blood count) or I am taking it temporarily after surgery')
    )
  iron = models.IntegerField(choices=IRON_CHOICES, verbose_name='15.  Do you take iron either as a supplement or part of a multivitamin?')
  

class Onboarding3(models.Model):
  """
    Preliminary questionnaire 3 of 4 : Physical Measurements
  """

  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # frequency choice
  YESNO_CHOICES = (
      (1, 'Yes'),
      (2, 'No')
  )

  # question 1
  weight_18y = models.TextField(verbose_name='1. How much did you weight when you were 18 years old?')

  # question 2
  weight_12m = models.TextField(verbose_name='2. How much did you weight 12 months ago?')

  # q3
  weight_change = models.IntegerField(choices=YESNO_CHOICES, verbose_name='3. Have you experienced any weight gain or loss over the last 12 months?')
  
  # q4
  INTENT_CHOICES = (
      (1, 'Yes'),
      (2, 'No'),
      (3, 'Client Answered \'No\' to 3.')
  )
  weight_intent = models.IntegerField(choices=INTENT_CHOICES, verbose_name='4. If YES, was it intentional?')
  
  # q5
  diet_program = models.IntegerField(choices=YESNO_CHOICES, verbose_name='5. Have you ever put yourself on a diet program to lose weight?')
  
  # a
  past_diet_program = models.TextField(null=True, blank=True, verbose_name='       a. If YES, what diet programs have you tried in the past?')

  how_program = models.TextField(null=True, blank=True, verbose_name='       b. Did you lose weight on these programs? How much?')

  maintain_weight = models.TextField(null=True, blank=True, verbose_name='       c. Did you maintain your weight loss? If not, for how long did you keep the weight off?')

  # q6
  family_weight = models.TextField(verbose_name='6. What is your family history surrounding weight - are your parents overweight?')
  
  height = models.CharField(max_length=20, verbose_name='Self-Reported Height (in inches, 12in per ft)')
  weight = models.CharField(max_length=20, verbose_name='Weight')
  percent_fat = models.CharField(max_length=20, verbose_name='Percent body fat')
  heart_rate = models.CharField(max_length=20, verbose_name='Resting Heart Rate (Beats per Minute)')
  blood_pressure = models.CharField(max_length=20, verbose_name='Resting Blood Pressure (Systolic/Diastolic)')


class Onboarding4(models.Model):
  """
    Onboarding questionnaire 4 of 4 : Others
  """

  #setting custom user model
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

  # question 1
  fitbit = models.TextField(null=True, blank=True, verbose_name="FitBit")
  my_net_diary = models.TextField(null=True, blank=True, verbose_name="My Net Diary")
  aria_scale = models.TextField(null=True, blank=True, verbose_name='Aria Scale')

  # question 2
  diag_visit = models.TextField(verbose_name='Scheduled Diagnostic Visit')
  # question 3
  freq_meet = models.TextField(verbose_name='Frequency of Meetings')
  # question 4
  prefer_method = models.TextField(verbose_name='Preferred Communication Methods')
  





