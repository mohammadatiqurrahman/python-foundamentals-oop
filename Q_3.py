age = int(input())
if age<12:
    print('Child')
elif 12<=age<=22:
    print('Student')
elif 23<=age<=64:
    print('Adult')
else:
    print('Senior')