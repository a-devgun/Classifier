# CLASSIFIER                                        


*****************************--------------------------------------------**********************************

This project contains 8 attachments from which  1 .py file Classifier.py , 1 folder textcat 6 .txt files.
*****************************************************************************************************************
a) Classifier.py contains the code for detecting the movie reviews weather they are positive or negative using  
   Naive based Classifier.

b) textcat - >    this folder further contains 3 folders named as "Dev" , "test" and "train"(given in the question) 
                  out of which dev and train folder further ontains 2 folders each "pos" and "neg" which has text  
                  files and in those files the movie reviews are written . so considering those reviews  
                  Naive Bayes Classifier will assigns the score to the possibility of postive or negative reviews.
 
c) Model.txt ->   Thos file will contains the data in the form of key value pairs where keys will be the doc numbers  
                  and values will be the corresponding words in the document.

d) Prediction-dev.txt ->  prediction file for the development data, which list  the scores that our model assigns to 
                          the  possibilities of positive and negative reviews.

e) Prediction-test.txt -> prediction file for the test data, which  list each filename in the test directory, 
                          and the scores our  model assigns to the possibilities of positive and negative reviews.

f) README.txt- >         This file.

g) PNRatio.txt ->        A list of the 20 terms with the highest (log) ratio of positive to negative weight. 

h) NPRatio.txt - >        A list of the 20 terms with the highest (log) ratio of  negative  to positive weight. 

************************************************************************************************************************

*******Percentage of positive and negative reviews in the development data  correctly classified is********
 
                                     = (158/200)*100 = 79 %

**********************************----------------------------**********************************************************
                                      Steps to compile :-
                                   ************************

## Setup

- Install Python  version 3.5

- Install Pycharm in your system using "https://www.jetbrains.com/pycharm/download/".
link.

## After successful installation:--
- open Pycharm  
- go to file-New-Select Python File.
- browse the file which I have submitted with the name "pgRank" or "pgrankGraph.py."and run it.
 
2nd Way to compile:-
Install * Install Python  version 2.7.10 from here - "https://www.python.org/downloads/release/python-2710/"

go to the python shell (command Line)
give the location of the .py file which you want to run . for Eg:- execfile('C:\Users\PyCharmProject\pgRank.py'\)
Press enter 

 *The program will run successfully*


 References Taken from :- www.Stackoverflow.com- for syntax , python documentation
************************************************************************************************************
