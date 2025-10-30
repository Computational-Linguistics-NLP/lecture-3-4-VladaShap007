year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  print('да')
else:
  print('нет')
  2007
  нет


year = int(input())
if year % 400 == 0:
  print('да')
elif year % 100 == 0:
  print('нет')
elif year % 4 == 0:
  print('да')
else:
  print('нет')
  2005
  нет


year = int(input())
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
if is_leap:
  print('да')
else:
  print('нет')
  2010
  нет
