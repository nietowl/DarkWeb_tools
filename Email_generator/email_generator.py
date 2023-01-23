#!usr/bin/python3
import pandas as pd
import os
import random
import string

# Create a list of sheet names
sheet_names = ["Vespera","Calantha","Cygnus","Lysander","Nimue","Seraphina","Titan","Zephyr","Anora","Azura","Calliope","Eirlys","Galen","Helix","Iliana","Jagger","Kaida","Lysander","Orion","Phoenixia","Quill","Seraphine","Thorne","Vesperia","Zinnober"]
# Create an ExcelWriter object
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

# Set the password length
password_length = 12

# Generate a random password
password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

for sheet_name in sheet_names:
    # Set the email address for the account
    email = sheet_name.lower().replace(" ", ".") + "@onionmail.org"
    # Create a dataframe and write it to the first sheet
    df1 = pd.DataFrame({'first name': [""], 'last name': [""],'userName': [sheet_name], 'Email': [email],'Password': [password], 'Site name': ["onionmail"], 'Site Url': ["http://pflujznptk5lmuf6xwadfqy6nffykdvahfbljh7liljailjbxrgvhfid.onion/account/login"]})
    # Write the dataframe to the current sheet
    df1.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the Excel file
writer.save()