====================
Python-CatYahooDict
====================
A little tool for using yahoo dictionary in CLI. Include a easy-using CLI tool and a API.

Dependence
==========
  - `Python`_ 2.7+
  - `BeautifulSoup`_ 4.0.5+

.. _`Python`: http://www.python.org/
.. _`BeautifulSoup`: http://www.crummy.com/software/BeautifulSoup/

Usage
=====
::

    $ python dict.py {word} {word} ...
    $ ./dict.py {word} {word} ..
    
    #   @word : a word you want to search
    # 
    #   [!] please use `"` when the word contains space(` `) 
    #       like "attend to"

    $ ./dict.py -v {word} {word} ...
    #   [!] show all information.


Example
+++++++

::
    
    $ python dict.py cat
    $ python dict.py attend
    $ python dict.py "attend to"


About API (yahdict.py)
======================

Field
++++++
  - YahooDictAPI.summary
  - YahooDictAPI.summary_desc
  - YahooDictAPI.summary_pron
  - YahooDictAPI.summary_related
  - YahooDictAPI.summary_synonym
  - YahooDictAPI.summary_antonym
  - YahooDictAPI.summary_variation
  - YahooDictAPI.defition

Useful Function
+++++++++++++++
  - YahooDictAPI(word,[space2add=True,url_prefix=[default]])
  - YahooDictAPI.found()
others please read code or help(yahdict)
