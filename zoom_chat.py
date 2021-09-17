import datetime
import os
import csv

file_lst = []
updated_lst = []
attendance_lst = []
attendance = []

attendance_set = {}

def create_attendace(chlst):
    for each in chlst:
        ind = each.rfind("From")
        if ind != -1:
            ind1 = ind + len("From")
            each = each[ind1+1:]
            updated_lst.append(each)
            #print(each)

    return updated_lst
    #print(chat_lst)


files = os.walk("/Users/shourjadeepdatta/Documents/Zoom/2021-07-20 11.01.09 Shourjadeep Datta's Zoom Meeting 88351896599")
lst = list(files)
file_lst.append(lst[0][-1][-1])
file_name = file_lst[-1]

chatbook = open(f"/Users/shourjadeepdatta/Documents/Zoom/2021-07-20 11.01.09 Shourjadeep Datta's Zoom Meeting 88351896599/{file_name}","r")

chats = chatbook.read()


chat_lst = chats.split(" to Everyone")

attendance_set = set(create_attendace(chat_lst))
attendance_tup = tuple(attendance_set)
attendance_lst.append(attendance_tup)
filename = f"{file_name}.xls"
with open(filename,"w") as att:
    writer = csv.writer(att)
    writer.writerows(attendance_lst)

print(attendance_lst)