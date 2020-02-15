print('-------------------------------------')
print('rawReviewRatings.txt')
print('-------------------------------------\n')

with open('rawReviewRatings.txt') as file1:
    content1 = file1.read()
    print(content1)

print('-------------------------------------')
print('rawReviews.txt')
print('-------------------------------------\n')

with open('rawReviews.txt') as file2:
    content2 = file2.read()
    print(content2)


with open('ratings.txt', 'w') as file3: 
    file3.write("3.25\n")
    file3.write("2.83\n")
    file3.write("0.67\n")
    file3.write("1.67\n")
    file3.write("3.50\n")

print('-------------------------------------')
print('ratings.txt')
print('-------------------------------------\n')

with open('ratings.txt') as file4:
    content4 = file4.read()
    print(content4)
