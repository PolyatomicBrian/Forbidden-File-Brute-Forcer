#Simple Dictionary Brute Forcer
# ~~ By Brian Jopling, 2016 ~~
# ---------------------------------------------------------------------------------
#Purpose: To append words from a dictionary to the end of a URL in an attempt at
#         brute forcing to obtain forbidden files from a website.
# ---------------------------------------------------------------------------------
#Why was this created?
#I threw this together during the Steam Summer Sale of 2016 to help the community
#figure out whether or not Valve was hosting an ARG during the event.
# ---------------------------------------------------------------------------------

import urllib2
from urllib2 import URLError

def func():

    #URL up to (and including) the parent directory you want to check.
    url = "http://www.brianjopling.com/img/"
    #Extensions for the file types you want to find. (The more extensions, the longer the program will take to run.)
    extensions = ['.png', '.jpg']

    #Get the file containing all the words you want to try.
    dic = open('dictionary.txt')

    #Store words from dictionary to list.
    with dic as f:
        global wordsList
        wordsList = f.readlines()

    #Create new file called "foundWords.txt" that will be used to store the names of files that were found on the server.
    foundWords = open('foundWords.txt', 'w')

    #For every word in our list of words...
    for word in wordsList:
        #For this example, I'm having the below chunk of code iterate twice, once with the raw data from
        #the dictionary, and a second time with the first letter of each word capitalized.
        for i in range(0,2):
            #On the second iteration, capitalize first letter of current word.
            if i == 1:
                word = word.title()
            #For every extension in our list of extensions...
            for extension in extensions:
                try:
                    #Removes any line breaks, tabs, and spaces (respectively) from the current word.
                    word = word.replace('\n', '')
                    word = word.replace('\t', '')
                    word = word.replace(' ', '')
                    #Appends word and extension to URL.
                    global currentURL
                    currentURL = url + word + extension
                    #Gets raw data of website with file name appended.
                    raw = urllib2.urlopen(currentURL).read()
                    print "--------------------------------------------------------\n" + currentURL + ": Found." + "\n--------------------------------------------------------"
                    #Write the word and extension to the foundWords.txt file created earlier.
                    foundWords.write(word + extension + '\n')
                #If nothing is found, an exception will be thrown.
                except URLError, error:
                    print currentURL + ": Not found."

#Call the above function.
func()

#Input to prevent premature termination.
k = input("\nType anything to quit: ")

#Close foundWords.txt file to prevent possible issues.
foundWords.close()
