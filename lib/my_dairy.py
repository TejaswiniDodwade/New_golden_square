def make_snippet(paramstring):
    my_list = paramstring.split()
    if len(my_list) > 5:
       my_string = my_list[0] + " " + my_list[1] + " " + my_list[2] + " " + my_list[3] + " " + my_list[4] +   "..."
       return my_string
    else:
        return paramstring
    # elif len(my_list) == 5:
    #     return paramstring
        
#print(make_snippet("This is my python test dairy"))





# def make_snippet(paramstring):
#     counter = 0
#     counter2 = 0
#     for char in paramstring:
#         counter2 += 1
#         if char == " ":
#            counter += 1
#     if counter > 5:
#        return
#     else:
#        return paramstring
    
