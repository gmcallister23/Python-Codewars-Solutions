#Solution to Even or Odd
def even_or_odd(number):
        if number % 2 == 0:
                return "Even"
        else:
                return "Odd"

#Solution to Convert a Number to a String
def number_to_string(num):
        return str(num)

#Remove String Spaces
def no_space(x):
        
        return x.replace(' ', '')

#Vowel Count
def get_count(sentence):
        return sum(sentence.count(v) for v in "aeiou")

