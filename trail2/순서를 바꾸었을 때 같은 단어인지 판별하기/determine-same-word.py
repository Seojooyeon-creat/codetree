word1 = input()
word2 = input()

# Please write your code here.
lst1 = list(word1)
lst2 = list(word2)

lst1.sort()
lst2.sort()

if lst1 == lst2:
    print("Yes")
else:
    print("No")