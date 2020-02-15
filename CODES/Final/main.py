from Functions import cleandata,fillDictionary

f3 = 'rawReviews.txt'
f4 = 'cleanReviews.txt'
cleandata(f3, f4)

dict = fillDictionary()

def rateReviews():
    tot_list = []
    with open('cleanReviews.txt') as file1:
        for line in file1:
            list1 = line.split()
            tot_list.append(list1)

    print(tot_list)

    m = 0
    for i in range(0, len(tot_list)):
        sum = 0
        avg = 0
        length = len(tot_list[i])
        for j in range(0, length):
            if (tot_list[i][j] in dict):
                sum += (dict[tot_list[i][j]][0]) / (dict[tot_list[i][j]][1])
            else:
                sum += 2

        avg = sum / len(tot_list[i])
        avg = round(avg, 2)

        if (m == 0):
            with open('ratings.txt', 'w') as file_object:
                file_object.write(str(avg))
                file_object.write("\n")
                m += 1;
        else:

            with open('ratings.txt', 'a') as file_object:
                file_object.write(str(avg))
                file_object.write("\n")




rateReviews()






