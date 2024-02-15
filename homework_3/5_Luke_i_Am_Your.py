# 5.	Luke Skywalker has family and friends. Help him remind them who is who. 
# Given a string with a name, return the relation of that person to Luke.
# Person  Relation
# Darth Vader father
# Leia    sister
# Han brother in law
# R2D2    droid
# Examples
# 'Darth Vader' ➞ 'Luke, I am your father.'
# 'Leia' ➞ 'Luke, I am your sister.'
# 'Han' ➞ 'Luke, I am your brother in law.'
name =input('Insert name ')
match name:
    case "Darth Vader":
        print('Luke, I am your father.')
    case "Leia":
        print('Luke, I am your sister.')
    case "Han":
        print('Luke, I am your brother in law.')
        
