from tabulate import tabulate #use the tabulate library

#tabulate works best with collections of data such as lists
#rather than indivudal variables like strings or integers.

names = ["Alice", "Bob", "Charlie"] #create a list of names

#Basic Table
print(tabulate(names))
''' Or use
table = tabulate(names)
print(table)'''
print()

#let's create another basic table with 2 columns
#tabulate works best with lists of lists
data = [ ["Apple", 5],
    ["Banana", 3],
    ["Orange", 10],
    ["Grapes", 1],
    ["Mango", 7]
]

print(tabulate(data))
print()

#Give headings to the table
headers = ["Country", "Capital", "Population (M)"]
countries = [
    ["Ireland", "Dublin",5.5],
    ["France", "Paris", 68],
    ["Germany", "Berlin", 83]
]

print(tabulate(countries, headers=headers))
#print(tabulate(countries, headers = ["Country", "Capital", "Population (M)"])) #same as above
print()

#What if we modify our countries table to have column headers in the first row
countries = [
    ["Country", "Capital", "Population (M)"],
    ["Ireland", "Dublin",5.5],
    ["France", "Paris", 68],
    ["Germany", "Berlin", 83]
]
#We can use the tabulate library to use the first row as headers
print(tabulate(countries, headers="firstrow"))
print()

#Alternatively, we could construct our tables in the format below:
countries = {
    "Country": ["France", "Japan", "Canada"],
    "Capital": ["Paris", "Tokyo", "Ottawa"],
    "Population (M)": [67, 126, 38]
}

print(tabulate(countries, headers="keys"))
print()
#We can generate an index for our table with an index for each row
# using showindex
headers = ["Book Title", "Author"]

books = [
    ["Da Vinci Code", "Dan Brown"],
    ["Python Crash Course", "Eric Matthes"]
]

print(tabulate(books, headers=headers, showindex="always"))
#print(tabulate(books, headers=headers, showindex=True))
#print(tabulate(books, headers=headers, showindex=False))
#print(tabulate(books, headers=headers, showindex="never"))
print()

#Or we can create our own index
rowIndex = ["A", "B"]
print(tabulate(books, headers=headers, showindex=rowIndex))
print()

#To align numeric content use numalign
#Left alignment
headers = ["Food Item", "Quantity", "Price"]

menu = [
    ["Pizza", 2, 8.50],
    ["Burger", 1, 5.00],
    ["Sushi", 3, 12.00],
    ["Pasta", 2, 7.25],
    ["Salad", 1, 4.50]
]

print(tabulate(menu, headers=headers, numalign="left"))
print()
#Right alignment
print(tabulate(menu, headers=headers, numalign="right"))
print()
#Center alignment
print(tabulate(menu, headers=headers, numalign="center"))
print()
#Decimal Alignment (alighted by Decimal Point)
print(tabulate(menu, headers=headers, numalign="decimal"))
print()

#Text Alignment
#stralign is used to control text alignment with left, center and right alignments.
headers = ["Movie", "Genre"]

movies = [
    ["Inception", "Sci-Fi"],
    ["The Dark Knight", "Action"],
    ["Interstellar", "Adventure"],
]
print(tabulate(movies, headers=headers, stralign="left"))
print()
print(tabulate(movies, headers=headers, stralign="center"))
print()
print(tabulate(movies, headers=headers, stralign="right"))
print()
#We can also align individual columns using colalign
print(tabulate(movies, headers=headers, colalign=("right", "center")));
print()
#The table structure itself can be formatted using tablefmt.
#The table can have format plain, simple, grid, outline, simple_grid, simple_outline
# rounded_grid, rounded_outline and many more.
print(tabulate(movies, headers=headers, stralign="left", tablefmt="simple"))
print()
print(tabulate(movies, headers=headers, stralign="left", tablefmt="outline"))
print()
print(tabulate(movies, headers=headers, stralign="left", tablefmt="heavy_grid"))
print()
