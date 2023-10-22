# URL-Extractor
Project Objective: Analyze given urls in the .csv file and save all statistics. 
There are about 150 URLs in the sheet
This code analyzes each url and automatically updates the datasheet as required

The following values are calculated:

NOTE: POSITIVE & NEGATIVE Dictionaries are nothing but text files which contain words to determine if a given paragraph has more of positive or negative words. 

POSITIVE SCORE : This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.

NEGATIVE SCORE : This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.

POLARITY SCORE : (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1

SUBJECTIVITY SCORE : This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: 
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
Range is from 0 to +1

AVG SENTENCE LENGTH : the number of words / the number of sentences

PERCENTAGE OF COMPLEX WORDS : the number of complex words / the number of words 

FOG INDEX : 0.4 * (Average Sentence Length + Percentage of Complex words)

AVG NUMBER OF WORDS PER SENTENCE : the total number of words / the total number of sentences

COMPLEX WORD COUNT : Complex words are words in the text that contain more than two syllables.

WORD COUNT : We count the total cleaned words present in the text by 
removing the stop words (using stopwords class of nltk package).
removing any punctuations like ? ! , . from the word before counting.

SYLLABLE PER WORD : 
We count the number of Syllables in each word of the text by counting the vowels present in each word. We also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.


PERSONAL PRONOUNS : To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US is not included in the list.


AVG WORD LENGTH : Sum of the total number of characters in each word/Total number of words
