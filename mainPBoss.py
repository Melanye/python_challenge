
# coding: utf-8

# In[ ]:


#MTAYLOR
#import modules

import os
import csv
import datetime


# In[ ]:


# Ask user which file to open and transform
user_input = input("Which employee data file would you like to open? 1 or 2 ? " )# Set the paths for the two csv files
csvpath1 = os.path.join("raw_data","employee_data1.csv")
csvpath2 = os.path.join("raw_data","employee_data2.csv")


# In[ ]:


# Tie the user's choice to the file to be opened.
if user_input=="1":
    file_choice = csvpath1
    print("You've selected employee_data1")
elif user_input=="2":
    file_choice = csvpath2
    print("You've selected employee_data2")


# In[ ]:


else:
    file_choice = csvpath2
    print("You've not selected a valid choice. Opening employee_data2")


# In[ ]:


# Open the csv file
with open(file_choice, newline ='') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=",")


# In[ ]:


# Skip the header row
   next(csvreader1)


# In[ ]:


# specify the file which will be written to
outputfile = os.path.join("output","bossfinal.csv")

# open the output file and set variable to hold contents
with open(outputfile, 'w', newline='') as datafile:


# In[ ]:


# Initialize csvwriter
writer = csv.writer(datafile, delimiter=',')
# Write the header row
writer.writerow(["Emp Id", "First Name", "Last Name", "DOB", "SSN", "State"])
# transform the data in the rows as specified
 for row in csvreader1:


# In[ ]:


# Pop the full name and replace it with new entries for first and last names
            full_name = row.pop(1)
            first, last = full_name.split()
            row.insert(1,first)
            row.insert(2,last)


# In[ ]:


# Pop the date-of-birth, reformat it, then re-insert it
            old_dob=row.pop(3)
            datetimeobject = datetime.datetime.strptime(old_dob,'%Y-%m-%d')
            new_dob = datetimeobject.strftime('%m/%d/%Y')
            row.insert(3,new_dob)


# In[ ]:


# Pop the ssn, then concatenate the obscured first 5 digits with the last 4
            old_ssn=row.pop(4)
            new_ssn="***-**-" + old_ssn[-4:]
            row.insert(4,new_ssn)


# In[ ]:


# Add dictionary that provides state codes for state names
            us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',

            }


# In[ ]:


# pop the state name
state_name=row.pop(5)
# look up the state code in the dictionary based on the state name
state_code = us_state_abbrev[state_name]
# append the state code to the end of the row
row.append(state_code)
#Write the zipped rows
writer.writerow(row)

