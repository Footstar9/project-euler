days_to_number = {"Monday": 0, "Tuesday" : 1 , "Wednesday" : 2, "Thursday": 3, "Friday" : 4, "Saturday": 5, "Sunday":6}
month_length = {0 : 31, 1 : 28, 2: 31, 3: 30, 4: 31, 5 : 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
month_length_leap = {0 : 31, 1 : 29, 2: 31, 3: 30, 4: 31, 5 : 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
first= [days_to_number["Tuesday"]]
year = 1901
count = 0
while year <= 2000:
    if year % 4 != 0:
        for i in range(12):
            first.append((first[len(first)-1]+ ((month_length[i % 12])% 7))%7)
    if year % 4 == 0:
        for i in range(12):
            first.append((first[len(first)-1]+ ((month_length_leap[i % 12])% 7))%7)        
    year +=1
print(first)
print(len(first))
for x in first:
    if x == 6:
        count+=1

print(count)