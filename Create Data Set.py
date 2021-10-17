import pandas as pd
import datetime

x = open(r'**','r', encoding = 'utf-8') #Replace ** with WhatsApp Text File Path and name. should be some thing like: C:\Desktop\chat.txt
y = x.read()
z=["[","]","\u200e","\u200f","\u200d♂️","\xa0","\U0001f972","\U0001f90d"]
for i in z:
    y= y.replace(i,"")
chat = y.splitlines()
del chat[0:2]


for i in range(len(chat)):
  try:
    datetime.datetime.strptime(chat[i].split(',')[0], '%d/%m/%Y')
  except ValueError:
    chat[i-1] = chat[i-1] + ' ' + chat[i]
    chat[i] = "NA"
    
    
for i in range(len(chat)):
  if chat[i].split(' ')[0] == 'NA':
    chat[i] = 'NA'


while True:
    try:
        chat.remove("NA")
    except ValueError:
        break

        
date = [chat[i].split(',')[0] for i in range(len(chat))]
time = [chat[i].split(',')[1] for i in range(len(chat))]  
time = [s.strip(' ') for s in time] # Remove spacing
time = [s[0:11] for s in time]
x = [chat[i].split(':')[2].split(' ')[2:] for i in range(len(chat))]
name=[]
for i in range(len(x)):
    name.append(' '.join(x[i]))

    
content = []
for i in range(len(chat)):
  try:
    content.append(chat[i].split(':')[3:])
  except IndexError:
    content.append('No Text')

message=[]
for i in range(len(content)):
    message.append(' '.join(content[i]))

df = pd.DataFrame(list(zip(date, time, name, message)), columns = ['Date', 'Time', 'Name', 'message'])
df.to_csv(r'**', encoding='UTF-8-sig', index=False) #Replace ** with where you want the CSV File to be saved and its name. should be some thing like: C:\Desktop\data.csv