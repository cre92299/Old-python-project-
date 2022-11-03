from time import sleep
from datetime import date
from collections import Counter

actions = {
    'action1':'It was terrible                                       1',
    'action2':'It was pretty bad                                     2',                                     
    'action3':'It was alright                                        3',
    'action4':'It was pretty good, nothing special about it though   4',
    'action5':'It was amazing!!!!!!!!!                               5',
}   
print('Hey. . ')
sleep(0.7)

print('Soooooooo. . ..  . How was your day?')
sleep(0.25)
print(
    "-----------------------------------------",
    "\n",
    actions["action1"],
    "\n",
    actions["action2"],
    "\n",
    actions["action3"],
    "\n",
    actions["action4"],
    "\n",
    actions["action5"],
    "\n",
    "-----------------------------------------",
)
actionask = input('Which of these sounds right?  : ')

correctnumbs = ['1','2','3','4','5']

if actionask not in correctnumbs:
    print('Wrong number')
    sleep(2)
    exit()

ensureity = str(input("Do you want to report this to 'report.txt' (Y - Yes, N - No) :"))


if ensureity == 'Y':
    with open('report.txt', 'a') as cass2:
     cass2.write(f"\n {actionask} | {date.today()}")

else:
    pass
with open('report.txt') as file:
    reportfile = file.read()

abcd = ''.join(reportfile).split()

jj = abcd[0::3]

aba = Counter(jj)

mean123 = aba.get

if actionask == '1':
    print(
        "Do something you like, have fun, don't make one day bad turn into many"
    )
    sleep(1)
    print('The action 1 was reported', aba.get('1'), 'times')
    sleep(3)
elif actionask == '2':
    print(
        "Do something you like, make days like this uncommon go outside, make friends whatever the shit"
        )
    sleep(1)
    print(" Do something you like, watch a movie, watch a tv show, learn more code, enjoy yourself" )
    print('The action 2 was reported', aba.get('2'), 'times')
    sleep(3)
elif actionask == '3':
    print(
        "Not so bad, lets start making alright days, uncommon"
    )
    sleep(1)
    print('The action 3 was reported', aba.get('3'), 'times')

elif actionask == '4':
    print(
        "Progess, hope he didnt do anything too bad, but atleast nothing that bad happened today :)"
    )
    sleep(1)
    print('The action 4 was reported', aba.get('4'), 'times')
    sleep(3)
elif actionask == '5':
    print("Congrats, hope you did lots of fun stuff in your day :DDD")
    sleep(1)
    print('The action 5 was reported', aba.get('5'), 'times')
    sleep(3)





