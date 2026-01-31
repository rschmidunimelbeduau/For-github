# Test your vocabulary from the German wordlist

import random as ra


FILENAME = 'German_wordlist_short.csv'

fileObject = open(FILENAME,encoding="utf8")

list1 = fileObject.readlines()  
# list1 is a  list of the lines in FILENAME.txt
# remember to close the  file promptly!
fileObject.close()

#remove \n and split list  on +
wordlist = []
for item in list1:
    newitem1 = item.strip('\n')
    newitem2 = newitem1.split('+')
    wordlist.append(newitem2)

#print(wordlist)   

wlen = len(wordlist)

str1 = input('How would you like to test your German? Type: '\
             '\n1 for German to English translation, '\
             '\n2 for English to German translation, '\
             '\n3 for articles of German nouns and ' \
             '\nq to Quit. ')

while str1 in {'1','2','3'}:
    
    while str1 == '1': # German to English
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
        while  str2 not in '123456':
                str2 = input('Please Enter a number from 1 to 6: ')        
                
        num2 = int(str2)

        if anslist[num2-1] == testword[1]:
                    print('Correct!\n')
        else:
            print('Sorry, it is:', testword[1])
        str1 = input('Type 2 to continue, ' \
                     '\nType 1 for German to English translation, ' \
                     '\nType 3 for articles of German nouns, ' \
                     '\nor q to quit.\n')
         

    while str1 == '2': # English to German
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

        print('Translate the English word: ')
        cprint(testword[1], 'red' )
        print('Here is a list of possible German translations:'\
                '\n1:', anslist[0],'\n2:',anslist[1],'\n3:', anslist[2],'\n4:',anslist[3],'\n5:', anslist[4],'\n6:',anslist[5] )
        str2 = input('Which one is the correct translation? Enter a number from 1 to 6: ')
        while  str2 not in '123456':
            str2 = input('Please Enter a number from 1 to 6: ')        
        
        num2 = int(str2)

        if anslist[num2-1] == testword[0]:
            print('Correct!\n')
        else:
            print('Sorry, it is: ', testword[0])    
 

        str1 = input('Type 2 to continue, ' \
                     '\nType 1 for German  to English translation, ' \
                     '\nType 3 for articles of German nouns, ' \
                     '\nor q to quit.\n')

    while str1  == '3': #Test articles for nouns
        testword = []
        while len(testword) == 0:
            x =  ra.randint(0,wlen-1)
            tempword1 = wordlist[x][0]
            if tempword1[0:4]  in {'der ', 'die ', 'das '}:
                testword.append([tempword1[0:3], tempword1[4:] ])
        anslist = ['der' , 'die', 'das']   
    
        print('What is the article of the German noun: ', testword[0][1])
        print( '\n1:', anslist[0],'\n2:',anslist[1],'\n3:', anslist[2] )
        
        str2 = input('Enter a number from 1 to 3: ')
        while  str2 not in '123':
            str2 = input('Please Enter a number from 1 to 3: ')
                
        num2 = int(str2)

        if anslist[num2-1] == testword[0][0]:
            print(testword[0][0], testword[0][1], ' is Correct! \n')
        else:
            print('Sorry, it is: ', testword[0][0], testword[0][1])
        
        str1 = input('Type 2 to continue, ' \
                      '\nType 1 for German to English translation, ' \
                     '\nType 3 for articles of German nouns, or' \
                     '\nor Type q to quit.\n')

                   
    
    

    


