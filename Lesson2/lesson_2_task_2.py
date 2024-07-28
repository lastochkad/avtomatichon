#Високосный год
#year = 2024
# 1 вариант
#year = int((input))
#def is_year_leap (year):
 #   if year % 4 == 0:
 #      return True  
 #  else:
 #       return False
#result = is_year_leap (year)
#print (f'Год {year}:{result}')

# 2 варант
def is_year_leap (year):
    return f'Год {year} высокосный? : {year % 4 == 0}'
print (is_year_leap (2024))
print (is_year_leap (2023))
print (is_year_leap (2022))