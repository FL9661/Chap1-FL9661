#Chap 2-6 using input functions

# 2.6.1.9 Lab
a = float(input("Please insert the value for \"a\": "))
b = float(input("Please insert the value for \"b\": "))
print("a+b=", a + b)
print("a-b=", a - b)
print("a*b=", a * b)
print("a/b=", a + b, "\n")

# 2.6.1.10 Lab
x = float(input("Enter value for x: "))
y = float(1/(x+1/(x+1/(x+1/(x))))) #start from bottom of formula, bracket and then work backwards
print("y =", y, "\n")

#2.6.1.11 Lab
hour = int(input("Starting time (hours): ")) #User input for hours
mins = int(input("Starting time (minutes): ")) #User input for mins
dura = int(input("Event duration (minutes): ")) #User input for duration in mins

HH = int((hour * 60 + mins + dura)//60) #Converts time inputs in minutes and outputs hours to zero decimal places
MM = int((hour * 60 + mins + dura)%60) #Converts time inputs in minutes, outputs remainder to zero decimal places for mins
print (HH % 24, ":", MM, sep="") # %24 outputs the remainder of HH when devided by 24 clock times