import string
num_line = 0
with open('rawReviewRatings.txt') as file1:
    for line in file1:
        num_line += 1

total_list = []
with open('rawReviewRatings.txt') as file1:
    for line in file1:
        list1 = line.split()
        for word in list1:
            word.strip(string.punctuation)

        total_list.append(list1)

rating = 0
count = 1
dictionary = {}

for a in range(0, num_line):
    size = 0
    dict_list = []
    rating = total_list[a][0]
    dict_list.append(int(rating))
    dict_list.append(count)

    size = len(total_list[a])
    for i in range(1, size):
        dictionary[total_list[a][i]] = dict_list


print(dictionary)








