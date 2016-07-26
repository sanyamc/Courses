
# lets create a list of names with new python methods.

"""a_list=['john','smith','alex']

upper = [val.upper() for val in a_list]

print(upper)

b_list=[('test','testing'),('abc','def')]

upper_b = [val.upper() for val,val2 in b_list if val=='test']

print([val.find('testing') for val,val2 in b_list])


ta_data = [['Peter', 'USA', 'CS262'],
           ['Andy', 'USA', 'CS212'],
           ['Sarah', 'England', 'CS101'],
           ['Gundega', 'Latvia', 'CS373'],
           ['Job', 'USA', 'CS387'],
           ['Sean', 'USA', 'CS253']]

ta_300 = [name+' is the TA for '+ course for name,country,course in ta_data if course.find("3")>=0]

print ta_300"""

############################################################
######## star args

## star args could be part of definition of a function or function argument
## def fn(something,*args) means that this function takes multiple args and they are available in args tuple.count
## in fu(*args) they are passed as a type which spreads or unpacks the argument

## fn(x,1,2,3) will be args=(1,2,3)
## fu(*args) will be fu(1,2,3)

################################################################
""" this is a multi line comment
    continuing the multi line comment """

""""  
a_list=[2,3]
b_list=[6,7]
"""
""""
print([val*b 
               for val in a_list
               for b in b_list])

# using generator expressions

print( next(val*b)
       for val in a_list
       for b in b_list
       
       )


#print(list(a+b for a in range(100,1000) if a%2!=0 for b in range(100,1000) if (a+b)%2==0 and b%2!=0))

"""

a=[1]
print(a.index(4))