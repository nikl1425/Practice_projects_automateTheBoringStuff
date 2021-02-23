import random
numberOfStreaks = 0
tails = 'T'
heads = 'H'
myList = []

for num in range(10000):
    random_number = random.randint(0, 1)

    if random_number == 0:
        myList.append(tails)
    elif random_number == 1:
        myList.append(heads)

    if len(myList) > 6:
        mynum = num-6
        my_slice = myList[mynum:num]

        try:
            if my_slice == ['T', 'T', 'T', 'T', 'T', 'T']:
                numberOfStreaks += 1
            if my_slice == ['H', 'H', 'H', 'H', 'H', 'H']:
                numberOfStreaks += 1
        except:
            print("not enought elements in list")




print('chance of streaks: %s%%' % (numberOfStreaks / 100))


