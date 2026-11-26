#homework = input('Did you do your homework? (yes/no)')
#day = input('What is the day?')
#if not (homework == 'yes'):
 #   print('Homework: no done yet. Finifh it.')
#if day != 'Saturday':
  #  print('It is a school week day.')

print('=== Smart School Day Planner ===')
print('Awnser 3 quick questions and i will plan your day!\n')

day = input('What day is it? (Monday - Sunday):').strip().capitalize()
weather = input('What is the weather? (sunny / rainy / cloudy)').strip().lower()
homework = input('Is your homework done? (yes / no)').strip().lower()

print()
print(f'=== Your plan for {day} ===')
print('-' * 35)

if day in ('Saturday', 'Sunday'):
    print('Day type  : Weekend - enjoy your free time!')
elif day == 'Monday':
    print('Day type  : First day of the week. Pack your weekly planner')
elif day == 'Friday':
    print('Day type  : Last school day. return library books today.')
elif day in ('Tuesday', 'Wednesday', 'Thursday'):
    print('Day type  : Regular school day. Stay focused!')
else:
    print('Day type  : Day not recognised. Please check your spelling.')

if weather == 'sunny' and homework == 'yes':
    print('After school: Head to the park - great weather and homework is done!')

if weather == 'rainy' or weather == 'cloudy':
    print('Weather tip: Pack your umbrella - It may get wet outside.')


if not (homework == 'yes'):
    print('Homework  : not done yet. Finish it before going out.')

if weather == 'rainy' and not (homework == 'yes'):
    print('Best plan  : Stay in, funish homework, then watch your favourite show!')
elif weather == 'sunny' and homework == 'yes' and not(day in('Saturday', 'Sunday')):
    print('Best plan  : Go for a walk in the park!')
else:
    print('Best plan  : Take it one step at a time - you have got this!')