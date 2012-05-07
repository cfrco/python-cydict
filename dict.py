#!/usr/bin/env python 

import urllib2
import sys
import bs4

if __name__ == "__main__":
    url = 'http://tw.dictionary.yahoo.com/dictionary?p='+sys.argv[1].replace(" ","+")

    html = urllib2.urlopen(url)
    
    html_out = ""

    for line in html:
        html_out += line

        if "type=text/javascript" in line:
            break

    soup = bs4.BeautifulSoup(html_out)
    msg = soup.find(attrs={"class":"msg"})

    if msg != None:
        if "zrpmsg" in str(msg):
            print "No found."
            exit(0)
            
    summary = soup.find(attrs={"id":"summary-card"})
    #print summary.prettify()
   
    #summary-description
    print sys.argv[1]+ " : "+summary.find("div","description").p.contents[0]
    print '' 

    #pronunciation
    res = summary.find("div","pronunciation")
    if res :
        pron = str(res.div)
        if "KK" in pron:
            print "# Pronunciation :"
            print "    KK : "+pron[pron.find("</span>")+8:pron.rfind("<span>")]
            print "    DJ : "+pron[pron.rfind("</span>")+8:pron.rfind("</div>")]
            print '' 

    #related
    res = summary.find(attrs={"class":"related"})
    if res :
        print "# Related :"
        for data in res.find_all("li"):
            print "    "+data.a.contents[0]
        print '' 

    #Synonyms
    res = summary.find(attrs={"class":"synonyms"})
    if res :
        print "# Synonyms :"
        for data in res.find_all("a"):
            print "    "+data.contents[0]
        print '' 
    
    #antonyms
    res = summary.find(attrs={"class":"antonym"})
    if res :
        print "# Antonyms :"
        for data in res.find_all("a"):
            print "    "+data.contents[0]
        print ''

    #Variation
    res = summary.find(attrs={"class":"variation"})
    if res :
        print "# Variation :"
        for data in res.find_all("a"):
            print "    "+data.contents[0]
        print '' 


    defition = soup.find_all(attrs={"class":"def clr nobr"})
    
    for d in defition:
        if d.find(attrs={"class":"caption"}).contents :
            print "$ "+d.find(attrs={"class":"caption"}).contents[0]

        for li in d.find_all("li"):
            print "   * "+li.find("p","interpret").contents[0]

            example =  li.find_all("p","example")
            
            for ex in example :
                out = ""
                for e in  ex.contents:
                    out += unicode(e)
                out = out.replace("<b>","").replace("</b>","")
                outs = out.split("\n")
                print "      >> "+outs[0]
                print "         "+outs[1]
            print ''
        print ''

