# FlyByWebScraper
The funniest manipulation of the flyby daily menu postings ever created lol.
# How this shit works
Well, this is a python program, which means it's just going to import a bunch of stuff and use other people's functions that I only understand to the extent that it's useful to me. So this function works by importing requests, beautifulsoup, and a dicitonary library called PyDictionary and doing stuff.

Basically it scrapes today's HUDS menu from the FlyBy website and creates a new meal listing where every word in the food description is replaced with its dictionary meaning. If a word has multiple parts of speech (for example test can be a noun and a verb) it picks one randomly and then picks the most popular definition according to PyDictionary. If a word is not recognized in the PyDictionary library then it is added to the result and nothing is done to it.
# Errors (which actually aren't errors) that may print
The PyDictionary library is outdated, meaning the docs are unintelligible. Every time you search for a word that is not in the dictionary it prints an error and there is nothing I can do to stop this ahhhhhhh. Also sometimes it throws an error about parsing when initializing, but neither of these things actually affect the performance or output of the program.
# Aight imma head out.
