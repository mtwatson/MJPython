'''
Created on Feb 6, 2016

@author: Jesse
'''
class Song(object):
    #it's not a constructor, but it serves a similar purpose
    def __init__(self, lyrics):
        self.lyrics = lyrics
    #'self' is the Python equivalent of 'this'. It is used for 
    # any instantiations, and allows objects to be passed to a module
    # or that modules class
    
    def sing_me_a_song(songLyrics):
    #the object passed into this module can be called anything
        for line in songLyrics.lyrics:
            #call the passed object with reference to the __init__ property
            print (line) 

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()