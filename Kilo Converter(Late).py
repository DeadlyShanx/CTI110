# Kilometer Converter
# Date
# CTI-110 P5T1_KilometerConverter 
# Johnson Jordan
#This program converts kilometers to miles.
#This is the Factor to Multiply with against miles
CONVERSION_FACTOR = 0.6214
# Program to Convert Kilometers to Miles.
km=int(input('Enter the number of km:'))
miles=km*CONVERSION_FACTOR
print('\n',miles,'miles')

