r'''
HOW I USED REGULAR EXPRESSION TO MATCH THE #PHONE NUMBER FORMAT

compile a pattern so that I can use it with .match method

pattern = "^(\w{3}-\w{3}-\w{4})$"

first import re function import re

now lets compile this pattern pattern_complied = re.compile(pattern)

strgin that we would like to use in the .match(string) is mystring = "555-666-7777"

now lets use the .match() method to match the compiled RE with MyString mystring_matching = pattern_complied.match(mystring) if mystring_matching: print (mystring_matching.groups(0)[0])
'''

# Writing a function to present the phone book menu 

def phonebook_menu():
    print('Option 1. Add a Phone Number Entry')
    print('Option 2. Delete a Phone Number Entry')
    print('Option 3. Edit a Phone Number Entry')
    print('Option 4. View all Contact Information')
    print('Option 5. Quit')
    print()

def validPhone(number):
    import re
    phone_match = re.compile("^(\d{3}-\d{3}-\d{4})$")
    match = phone_match.match(number)
    if match:
        return match.groups(0)[0]
    return None

#The phone book entries will be dictionaries. 
contact_info = {}
menu_choice = 0
phonebook_menu()


while menu_choice != 5:
    menu_choice = int(input("Select a menu Option (1-5): "))

    #When choosing option 1 it should accept a first name, last name and a phone number
    if menu_choice == 1:
        #print("Add a new Phone Book Entry:")
        
        first_name = ''
        while not first_name.isalpha():
            first_name = str(input("Enter First Name with letters ONLY: "))
            #continue
            
        last_name  = ''
        while not last_name.isalpha():
            last_name  = str(input("Enter Last Name with letters ONLY: "))
            continue
        
        phone = ''
        while not validPhone(phone):
            phone = input('Please enter a phone number in the format XXX-XXX-XXXX: ')
            continue
             
        name = first_name + " " +last_name
        if name in contact_info:
            if phone not in contact_info[name]['phone_number']:
                contact_info[name]['phone_number'].append(phone)
                print("\nInfo has been added")
            else:
                print("\nPhone number already exists")
        else:
            tempdict = {}
            tempdict['phone_number']  = []
            #tempdict['email_address'] = []
            tempdict['phone_number'].append(phone)
            #tempdict['email_address'].append(email)
            contact_info[name] = tempdict
            print("\nInfo has been added")

    elif menu_choice == 2:
        
        print("\nDeleting Contact Information")
        
        #same name and phone number validation as before
        name = input("\nEnter Full Name: ")
        
        phone = ''
        while not validPhone(phone):
            phone = input('Please enter a phone number in the format XXX-XXX-XXXX: ')
            continue
               
        if name in contact_info.keys():
            if phone in contact_info[name]['phone_number']:
                contact_info[name]['phone_number'].remove(phone)
                print(f'\nDeleting Phone Number {phone} Associated with {name}')
            elif len(contact_info[name]['phone_number']) == 0: #removing ['phone_number']
            # delete name from contact_infos
                del contact_info[name]
        else:
            print(f"\nPhone Number {phone} for {name} Not found")

    
    elif menu_choice == 3:
        print("\nEditing Contact Information")
        name = input("\nEnter Full Name: ")
        if name in contact_info:
            print(contact_info[name])
        else:
                print(name, "was not found")
    
    
    elif menu_choice == 4:
        print("\nLookup Contact Information")
        name = input("\nEnter Full Name: ")
        if name in contact_info:
            #new_tempdict = {}
            #new_tempdict['phone_number']  = []
            #tempdict['email_address'] = []
            #tempdict['phone_number'].append(phone)
            #tempdict['email_address'].append(email)
            #contact_info[name] = tempdict
            print(contact_info[name])
        else:
                print(name, "was not found")

    elif menu_choice != 5:
        phonebook_menu()

