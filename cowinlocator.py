from cowin_api import CoWinAPI

cowin = CoWinAPI()

'''states = cowin.get_states()
print(states)'''

'''state_id = '21'
districts = cowin.get_districts(state_id)
print(districts)'''

pin_code = input("Enter the pincode of the area:")
date = input("Enter the current date(dd-mm-yyyy):")  # Optional. Default value is today's date
min_age_limit = int(input("Enter the age limit(18/45):"))  # Optional. By default returns centers without filtering by min_age_limit
available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
print(available_centers)

