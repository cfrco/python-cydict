#!/usr/bin/env python 

import yahdict
import sys
from optparse import OptionParser

def easy_print(l,name):
    if l :
        print "# "+name+" :"
        for e in l :
            print "    "+e["content"] #+"("+e["href"]+")"
        print '' 

def parser_init():
    parser = OptionParser()
    parser.add_option("-v","--verbose",dest="verbose",
                      help="view all information",
                      action="store_true",default=False)
    return parser

def print_word(dic,verbose):

    if verbose :
        #summary-description
        print word+ " : "+dic.summary_desc
        print '' 

        #pronunciation
        if dic.summary_pron:
            print "# Pronunciation :"
            print "    KK : "+dic.summary_pron["kk"]
            print "    DJ : "+dic.summary_pron["dj"]
            print '' 
    else :
        print word+ " : "+dic.summary_desc
        print "KK : "+dic.summary_pron["kk"]+" | DJ : "+dic.summary_pron["dj"]
        print '' 
    
    if verbose:
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

                if verbose : 
                    for exam in inte[1]:
                        print "      >> "+exam[0]
                        print "         "+exam[1]
                    print ''

            print ''

if __name__ == "__main__":

    parser = parser_init()
    (options,args) = parser.parse_args()
    
    for word in args :
        dic = yahdict.YahooDictAPI(word)
        
        if not dic.found():
            print "[!] No found."
        
        else :
            print_word(dic,options.verbose)
        
        
