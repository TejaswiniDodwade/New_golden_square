#### Exercise 1 ####
# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, 
# assuming that I can read 200 words a minute.

# The name of the function = estimate_reading_time
# What parameters it takes, their names and data types = One parameter = paramtext, type = string
# What it returns and the data type of that value = estimate reading time for text, data type int
# Any other side effects it might have = NA

def estimate_reading_time(paramtext):
    count_words = len(paramtext.split())
    return (count_words * 1 ) / 200
    
