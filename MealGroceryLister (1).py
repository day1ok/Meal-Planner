#For all google spreadsheets functions
import gspread
#For hidding the password while running
import getpass
#For reading and writing to CSV files
import csv

#Keeps a list of quantity for the user to select
qty = [0,1,2,3,4,5,6]
count_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
meal_selection = []

#Prompts the user to enter a password and it will hide the password when it is typed in (import getpass)
pswd = getpass.getpass('Password:')

#makes a gap so password is not visible (does not work in shell)
for item in range(100):
    print ('\n')

#prompt this while loading the worksheets from google docs
print ('Loading....')

try:
# Login with your Google account
    gc = gspread.login('day1ok@gmail.com', pswd)  # getpass.getpass()

#not sure what this does
except gspread.AuthenticationError or gspread.NameError:
        print ("Incorrect Username or Password")
        
# Open a worksheet from spreadsheet with one shot
wks = gc.open("Dinner Ratings")

#Open Shopping List spread sheet to save the list to
wks1 = gc.open("Shopping List").sheet1


# Get all values from the first row
wksList = wks.worksheets()

#Get how many meals the user wants
meal_quantity = input('How many meals would you like this week? ')

i = 1

#Grabs each worksheet in the document starting with the 2nd worksheet [1:] and prints a list of the items
for sh in wksList[1:]:
    print("      " + str(i) + ". " + sh.title)
    i += 1
    
#Goes through the ammount of meals the user inputed and tells the user to select what meals they want one at a time
for item in range(meal_quantity):
    thing = input("Enter " + count_list[item] + " choice: " )
    meal_selection.append(thing)

#Set dictionary inventory to store 
inventory = {}

#Loops through the user selected meals and add them to the inventory. Adds new items and adds quantity. 
for meal in meal_selection:

    #Gets the names from all of the worksheets in your spreadsheet
    rows = wksList[meal].get_all_values()

    #Loops through the worksheets and lists them starting at the 2nd worksheet. It then adds the names of the ingrediant and the quantity to the inventory dictionary. 
    for rowNumber in range(1,len(rows)):
        ingredient = rows[rowNumber][0]
        qty = float(rows[rowNumber][1])
        inventory.setdefault(ingredient,0)
        inventory[ingredient] += qty

print ("Generating Shopping List, please wait for finished to appear and then exit")

y = 1

#Write the inventory to a CSV file
for key in inventory:
    wks1.update_cell(y, 1, key) # For updating the ingredient
    wks1.update_cell(y, 2, inventory[key]) # For updateing the quantity 
    y += 1


print inventory
#Indicates to the user that the shopping list has updated 
print ("finished")







"""
THIS WAS SLOW FOR UNKNOWN REASAONS, PROBABLY WRITING TO GOOGLE SHEETS
#Update the google docs shopping list with the items in the inventory
for key in inventory:
    wks1.update_cell(y, 1, key) # For updating the ingredient
    wks1.update_cell(y, 2, inventory[key]) # For updateing the quantity 
    y += 1
"""
