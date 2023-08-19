# This program extracts URLs from a text file saved on my computer.
# The text file has the list of all urls given in assignment spreadsheet
# Each function in this code performs a specific analytic operation and returns the appropriate value


import requests
from bs4 import BeautifulSoup
import re

with open(r"C:\Users\ROSHIT\Desktop\URLS.txt") as file:
    d = []
    for line in file:
        url = line.strip()  # Remove any whitespace or newline characters
        u = url.split()

        for i in u:  # going through every link for textual analysis
            response = requests.get(i)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                target_element = soup.find("div", {"class": "td-post-content tagdiv-type"})
                target_text = target_element.get_text()
                # target_text is the name of text we need


            else:
                print("Error accessing URL:", response.status_code)


            def PosiScore(text):
                score = 0
                file = open(r'C:\Users\ROSHIT\PycharmProjects\pythonProject4\positive-words.txt')
                get = file.read()
                posi = get.split()
                temptext = text.split()

                for i in temptext:
                    for j in posi:
                        if i == j:
                            score += 1

                return (score)


            def NegScore(text):
                score = 0
                file = open(r'C:\Users\ROSHIT\PycharmProjects\pythonProject4\negative-words.txt')
                get = file.read()
                posi = get.split()
                temptext = text.split()

                for i in temptext:
                    for j in posi:
                        if i == j:
                            score += 1

                return (score)


            def PolScore(ps, ns):
                a = (ps - ns) / (ps + ns + 0.000001)

                return a


            def SubScore(ps, ns, text):
                temptext = text.split()
                s = (ps + ns) / ((len(temptext)) + 0.000001)
                return s


            def AvgSentLength(text):
                delimiters = [".", "!", "?"]
                sentences = [sentence.strip() for sentence in re.split(f"[{''.join(delimiters)}]", text)]
                sencount = len(sentences)

                word_count = wordcount(target_text)
                x = word_count / sencount
                return x


            def wordcount(text):
                temptext = text.split()
                return len(temptext)


            def ComplexCount(text):
                complexcount = 0

                vow = ['a', 'e', 'i', 'o', 'u']
                exp = ['es', 'ed']
                temptext = text.split()
                for i in temptext:

                    cnt = 0
                    for x in i:
                        if x in vow:
                            if i[len(i) - 2:len(i)] not in exp:
                                cnt += 1
                            else:
                                pass

                    if cnt > 2:
                        complexcount += 1

                return complexcount


            def ComplexPerc(text):
                # count percentage of complex words in
                complexcount = ComplexCount(text)
                wordcnt = wordcount(target_text)
                return (complexcount / wordcnt)


            def FogLength(text):
                a = AvgSentLength(text) + ComplexPerc(text)
                return (0.4 * a)


            def AvgWordperSent(text):
                delimiters = [".", "!", "?"]
                sentences = [sentence.strip() for sentence in re.split(f"[{''.join(delimiters)}]", text)]
                sencount = len(sentences)
                word_count = wordcount(target_text)
                x = word_count / sencount
                return x


            def syllper(text):
                temptext = text.split()
                vow = ['a', 'e', 'i', 'o', 'u']
                exp = ['es', 'ed']
                scount = 0
                for i in temptext:

                    cnt = 0
                    for x in i:
                        if x in vow:
                            if i[len(i) - 2:len(i)] not in exp:
                                cnt += 1
                            else:
                                pass
                    scount += cnt

                return scount / wordcount(target_text)


            def prnouns(text):
                pronounRegex = re.compile(r'(I|we|my|ours|(?-i:us))', re.I)
                pronouns = pronounRegex.findall(text)
                return len(pronouns)


            def avgwordlen(text):
                temptext = text.split()
                wcount = len(temptext)
                ccount = 1
                for i in temptext:
                    for j in i:
                        ccount += 1

                return ccount / wcount

            # assigning a variable to every function
            positive_score = PosiScore(target_text)
            negative_score = NegScore(target_text)
            polarity_score = PolScore(positive_score, negative_score)
            subjectivity_score = SubScore(positive_score, negative_score, target_text)
            avgs = AvgSentLength(target_text)
            wps = AvgSentLength(target_text)
            comp = ComplexPerc(target_text)
            flen = FogLength(target_text)
            cc = ComplexCount(target_text)
            wc = wordcount(target_text)
            syll = syllper(target_text)
            pr = prnouns(target_text)
            avwl = avgwordlen(target_text)

            v = [positive_score, negative_score, polarity_score, subjectivity_score, avgs, comp, flen, wps, cc, wc,
                 syll, pr, avwl]
            d.append(v)
            # list d is made up of list of values for every URL
    import csv

    with open('C:/Users/ROSHIT/Desktop/BlackCofferProj.csv', 'w', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        writer.writerows(d) # List d gets added to an Excel file I created on my computer
