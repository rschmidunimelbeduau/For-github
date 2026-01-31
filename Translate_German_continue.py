# Test your vocabulary from the German wordlist

import random as ra
import csv

FILENAME = 'My_German_Words.csv'

fileObject1 = open(FILENAME,encoding="utf-8")

data1 = csv.reader(fileObject1)  
# list1 is a  list of the lines in FILENAME.txt
# remember to close the  file promptly!
#fileObject1.close()

wordlist  = list(data1)

wlen = len(wordlist)

str1 = input('How would you like to test your German? Type: '\
             '\n1 for German to English translation, '\
             '\n2 for English to German translation, '\
             '\nq to Quit. ')

if  str1 == '1':
    
    k = 0
    correct = 0
    while k < 100:
        testword = wordlist[ra.randint(0,wlen-1)]
        testlist = [ testword]
        while len(testlist) < 6:
            x =  ra.randint(0,wlen-1)
            if wordlist[x] not in testlist:
                testlist.append(wordlist[x])
        anslist = []
        for k in  range(6):
                anslist.append(testlist[k][1])
                anslist.sort()
        print('Translate the German word: ', testword[0]  )
        print('\n1:', anslist[0],'\n2:',anslist[1],'\n3:', anslist[2],'\n4:',anslist[3],'\n5:', anslist[4],'\n6:',anslist[5] )
        str2 = input('Which one is the correct translation? Enter a number from 1 to 6: ')
        if str2 not in '123456':
                str2 = input('Please Enter a number from 1 to 6: ')        
                
        num2 = int(str2)

        if anslist[num2-1] == testword[1]:
                    correct =  correct + 1
                    print(testword[1] , 'is Correct!\n')
        else:
            print('Sorry, it is:', testword[1])
    k = k+1
    if k == 100:
        print('You got ', correct, 'words correct out of 100 today!')
        

if str1 == '2': # English to German
    k = 0
    while k < 500:
        testword = wordlist[ra.randint(0,wlen-1)]
        testlist = [ testword]
        while len(testlist) < 6:
            x =  ra.randint(0,wlen-1)
            if wordlist[x] not in testlist:
                testlist.append(wordlist[x])        
        anslist = []
        for k in range(6):
            anslist.append(testlist[k][0])
        anslist.sort()

        print('Translate the English word: ', testword[1] )
        print('Here is a list of possible German translations:'\
                '\n1:', anslist[0],'\n2:',anslist[1],'\n3:', anslist[2],'\n4:',anslist[3],'\n5:', anslist[4],'\n6:',anslist[5] )
        str2 = input('Which one is the correct translation? Enter a number from 1 to 6: ')
        if  str2 not in '123456':
            str2 = input('Please Enter a number from 1 to 6: ')        
        
        num2 = int(str2)

        if anslist[num2-1] == testword[0]:
            print(testword[0], 'is Correct!\n')
        else:
            print('Sorry, it is: ', testword[0])    
 

    k = k+1
    if k == 100:
        print('You got ', correct, 'words correct out of 100 today!')
        

    

                   
    
    

    


