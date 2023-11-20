# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a 
# suitable sentence-ending punctuation mark.

#The name of the function -- letter_and_punct()
#What parameters it takes, their names and data types -- string = paramtext
#What it returns and the data type of that value -- boolen value to verify
#Any other side effects it might have -- NA

def letter_and_punctution(paramtext):
           if paramtext[0].isupper() and paramtext[-1] in [".","!","?"]:
              return True           
           else:
              return False
        