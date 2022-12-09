from textblob import TextBlob

#Create a list with wrong word
string = input("Enter elements (Space-Separated): ")
  
# split the strings and store it to a list
word = string.split()  
print('The list is:', word) 
correct_word = []   #will store correct word
for i in word:
    #storing correct word into correctZ_word
    correct_word.append(TextBlob(i))
    
print("Given wrong words: ",word);
print('Correct words are: ')
for i in correct_word:
    print(i.correct(),end=' ')
    