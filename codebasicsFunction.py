"""
poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance
"""
list_of_words =[]
file_open  = open("/content/poem.txt", "r")
for line in file_open:
  lines = line.split()
  #print(lines)
  for word in lines :
    new_word = ''.join (letter for letter in word if letter.isalnum()).lower()
    #print(new_word)
    list_of_words.append(new_word)
    #print(list_of_words)



list1 =[]
list2= []
for word in list_of_words:
  if  not word  in list1:
    list1.append(word)
    list2.append(1)
  else :
    indx = list1.index(word)
    list2[indx]+=1
  #print(list2)
max_list2 = max(list2)
#print(max_list2)

a = list2.index(max_list2)
maxword = list1[a]
#print(a)
print(maxword)
