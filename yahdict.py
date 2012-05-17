#!/usr/bin/env python

import urllib2
import sys
import bs4

class YahooDictAPI:
    
    def __init__(self,word,space2add=True,url_prefix='http://tw.dictionary.yahoo.com/dictionary?p='):
        """
            @word : a word want to search.
            @space2add : replace ` ` with `+` for URL.
            @url_prefix : [default] i think you needn't change it.
        """
        self.request_url = url_prefix

        if space2add :
            self.request_url += word.replace(" ","+")
        else :
            self.request_url += word

        html = urllib2.urlopen(self.request_url)
        html_out = ""

        for line in html:
            html_out += line
            
            #find ending line
            if "type=text/javascript" in line:
                break

        self.soup = bs4.BeautifulSoup(html_out)
        self.msg = self.soup.find(attrs={"class":"msg"})
        
        if self.found() :
            self.summary = self.soup.find(attrs={"id":"summary-card"})
            self.defition = self.soup.find_all(attrs={"class":"def clr nobr"})
            
            self.summary_word = self.summary.find("div","theme clr").h3.a.contents[0]
            self.summary_desc = self.summary.find("div","description").p.contents[0]
            self.summary_pron = self.get_pron()
            self.summary_related = self.get_related()
            self.summary_synonym = self.get_synonym()
            self.summary_antonym = self.get_antonym()
            self.summary_variation = self.get_variation()
            self.defition = self.get_defition()

    def found(self):
        """
            return False,if no word be found.
        """
        return not "zrpmsg" in str(self.msg)
    
    def autocorrect(self):
        """
            return True,if word be correct autoly.
        """
        if self.msg == None :
            return False
        return "dym" in str(self.msg)

    def get_pron(self):
        res = self.summary.find("div","pronunciation")
        if res :
            d = dict()
            pron = str(res.div)
            if "KK" in pron:
                d["kk"] = pron[pron.find("</span>")+8:pron.rfind("<span>")].strip()
                d["dj"] = pron[pron.rfind("</span>")+8:pron.rfind("</div>")].strip()
            return d
        return None

    def get_related(self):
        return self.easy_fetch_li("related")

    def get_synonym(self):
        return self.easy_fetch_a("synonyms")

    def get_antonym(self): 
        return self.easy_fetch_a("antonym")

    def get_variation(self):
        return self.easy_fetch_a("variation")

    def get_defition(self):
        """  
            [
                {
                    "caption":caption,
                    "interpret":interpret,
                    "example":[(english,chinese),...]
                },...
            ]
        """
        defition = self.soup.find_all(attrs={"class":"def clr nobr"})
        
        out_list = list()
        for d in defition:
            dd = dict()

            if d.find(attrs={"class":"caption"}).contents :
                dd["caption"] = d.find(attrs={"class":"caption"}).contents[0]
                dd["interpret"] = list()

            for li in d.find_all("li"):
                inte = (li.find("p","interpret").contents[0],list())

                example =  li.find_all("p","example")
                for ex in example :
                    out = ""
                    for e in  ex.contents:
                        out += unicode(e)
                    out = out.replace("<b>","").replace("</b>","")    # clean <b> </b> tag
                    outs = out.split("\n")                            # seperate : english,chinese
                    inte[1].append((outs[0],outs[1]))

                dd["interpret"].append(inte)

            out_list.append(dd)
        return out_list

    def easy_fetch_li(self,class_name):
        res = self.summary.find(attrs={"class":class_name})
        if res :
            li = list()
            for data in res.find_all("li"):
                li.append({"href":data.a["href"],"content":data.a.contents[0]})
            return li
        return None

    def easy_fetch_a(self,class_name):
        res = self.summary.find(attrs={"class":class_name})
        if res :
            li = list()
            for data in res.find_all("a"):
                li.append({"href":data["href"],"content":data.contents[0]})
            return li
        return None

"""
    This is for testing.
"""
if __name__ == "__main__":
    d = YahooDictAPI('attend')
    print d.summary_word
    print d.summary_desc
    print d.summary_pron
    print d.summary_related
    print d.summary_synonym
    print d.summary_antonym
    print d.summary_variation
    print d.get_defition()


