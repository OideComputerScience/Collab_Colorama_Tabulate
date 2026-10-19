#Declare 3 name string variables and 3 age integer variables. 
name1 = "Alice"
age1 = 20

name2 = "Bob"
age2 = 22

name3 = "Charlie"
age3 = 19
'''
Create a table using string formatting.
%s and %d represent strings and integers respectively.
-15 represents left align the string field 15 characters wide.
5 represents right aling the integer firld 5 characters wide.
% tells Python to substitute the values into the string. '''
print("%-15s %5s" % ("Name", "Age"))
print("%-15s %5s" % ("---------------", "-----"))
print("%-15s %5d" % (name1, age1))
print("%-15s %5d" % (name2, age2))
print("%-15s %5d" % (name3, age3))

#Or we could create a list and use loops as so
students = [
    ("Jack", 20),
    ("James", 22),
    ("Jill", 19)
]

print("%-15s %5s" % ("Name", "Age"))
print("%-15s %5s" % ("---------------", "-----"))

for name, age in students:
    print("%-15s %5d" % (name, age))
    
#Add a vertical border between columns by using the | character in your format string.
    students = [
    ("Tom", 20),
    ("Marge", 22),
    ("Bill", 19)
]

print("+-----------------+------+")
print("| %-15s | %4s |" % ("Name", "Age"))
print("+-----------------+------+")
for name, age in students:
    print("| %-15s | %4d |" % (name, age))
print("+-----------------+------+")
    