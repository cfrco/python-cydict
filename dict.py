#!/usr/bin/env python 

import yahdict
import sys

def easy_print(l,name):
    if l :
        print "# "+name+" :"
        for e in l :
            print "    "+e["content"] #+"("+e["href"]+")"
        print '' 

if __name__ == "__main__":
    dic = yahdict.YahooDictAPI(sys.argv[1])
    
    if not dic.found():
        print "[!] No found."
        exit(0)
    
    #summary-description
    print sys.argv[1]+ " : "+dic.summary_desc
    print '' 

    #pronunciation
    if dic.summary_pron:
        print "# Pronunciation :"
        print "    KK : "+dic.summary_pron["kk"]
        print "    DJ : "+dic.summary_pron["dj"]
        print '' 

    #related
    easy_print(dic.summary_related,"Related")

    #Synonyms
    easy_print(dic.summary_synonym,"Synonyms")
    
    #antonyms
    easy_print(dic.summary_antonym,"Antonyms")

    #Variation
    easy_print(dic.summary_variation,"Variation")

    #defition
    for e in dic.defition :
        if "caption" in e :
            print "$ "+e["caption"]
        
        if "interpret" in e :
            for inte in e["interpret"]:
                print "   * "+inte[0]
                
                for exam in inte[1]:
                    print "      >> "+exam[0]
                    print "         "+exam[1]
                print ''
        print ''


        for data in res.find_all("a"):
            print "    "+data.contents[0]
        print '' 
