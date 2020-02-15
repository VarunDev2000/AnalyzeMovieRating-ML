import string

remove_list = []

def cleandata(f1,f2):

    with open('stopwords.txt') as file:
        for line in file:
            listt = line.rstrip()
            remove_list.append(listt)

    i=0
    exclude = set(string.punctuation)
    with open(f1) as file:
        for line in file:
            word_list = line.split()
            varia =' '.join([i for i in word_list if i not in remove_list])
            varia = ''.join(ch for ch in varia if ch not in exclude)
            ##tr = str.maketrans("!?.", 3*" ")
            ##s = varia.translate(tr)



            if(i==0):
                with open(f2, 'w') as file_object:
                    file_object.write(varia)
                    file_object.write("\n")
                    i+=1;
            else:

                with open(f2, 'a') as file_object:
                    file_object.write(varia)
                    file_object.write("\n")



def fillDictionary():
    f1 = 'rawReviewRatings.txt'
    f2 = 'cleanReviewRatings.txt'
    cleandata(f1,f2)

    num_line = 0
    with open('cleanReviewRatings.txt') as file1:
        for line in file1:
            num_line += 1

    total_list = []
    with open('cleanReviewRatings.txt') as file1:
        for line in file1:
            list1 = line.split()
            total_list.append(list1)

    rating = 0
    count = 0
    dictionary = {}

    for a in range(0, num_line):

        size = 0
        total1 = 0
        count1 = 0
        total = 0
        count = 0
        size = len(total_list[a])
        for i in range(1, size):
            w = total_list[a][i]
            if w in dictionary.keys():
                total1 = dictionary[total_list[a][i]][0]
                total1 += int(total_list[a][0])
                dictionary[total_list[a][i]][0] = total1

                count1 = dictionary[total_list[a][i]][1]
                count1 += 1
                dictionary[total_list[a][i]][1] = count1

            if w not in dictionary.keys():
                dict_list = []
                rating = total_list[a][0]
                dict_list.append(int(rating))
                dict_list.append(1)

                dictionary[total_list[a][i]] = dict_list

    if '' in dictionary.keys():
        del dictionary['']

    return dictionary

