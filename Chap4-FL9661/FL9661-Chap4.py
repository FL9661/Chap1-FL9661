# Lab 4.3.1.6 A leap year: writing your own functions

def is_year_leap(year):
    if (year) < 1582:
        print ('Not within the Gregorian calendar period.')
        return False
    elif (year % 4 ) != 0: # if output is not equal to 0 = common year
        print ("common year")
        return False
    elif (year % 100 ) != 0: # if output is not equal to 0 = leap year
        print ("leap year")
        return True
    elif (year % 400 ) != 0: # if output is not equal to 0 = common year
        print ("common year")
        return False
    else:
        print ("leap year") # everything else is a leap year
        return True
    
test_data = [1581, 1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Lab 4.3.1.7 How many days: writing and using your own functions
def is_year_leap(year):# From Lab 4.3.1.6 deleted additional print outputs
    if (year % 4 ) != 0: # if output is not equal to 0 = common year
        return False
    elif (year % 100 ) != 0: # if output is not equal to 0 = leap year
        return True
    elif (year % 400 ) != 0: # if output is not equal to 0 = common year
        return False
    else:
        return True
### I had to light blub this part as I was completely lost, I do not understand how the res value works
def days_in_month(year,month):
	# if statement
		# ...
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res
### Test data
test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr,mo,"-> ",end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Lab 4.3.1.10 : Converting fuel consumption

def liters_100km_to_miles_gallon(litres):
    km_per_litres = 100 / litres  #100/litres = km per litre 25.64
    miles_per_litre = km_per_litres / 1.609344 # miles per litre
    gallon = 3.785411784 #litres
    miles_per_gallon = miles_per_litre * gallon
    return miles_per_gallon
    
def miles_gallon_to_liters_100km(miles):
    mile2km = 1 * 1.609344 # 1.62137119223733396961743418436332
    gallon = 3.785411784 #litres
    total_Km_Per_Gallon = miles * mile2km #= 97.0434432
    Km_Per_litre = total_Km_Per_Gallon / gallon # 25.636165558045401805089324464363 km per litre
    litres_to_100km = 100 / Km_Per_litre
    return 'litres to 100Km: ', litres_to_100km # not sure why this now prints an additional () with brackets and is brackets used it returns an additional none line
   
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

###Expected Output
# 0.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
#10.009131205673757

def intro(a=input('first name: '), b=input('last name :')):
    print("My name is", a , b)

intro()