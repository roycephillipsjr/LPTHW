class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


##########
# 2. Put the lyrics in a separate varible, then pass that variable to the class to use instead
print()
print()
row_row_row = ['Row row row your boat',
               'Gently down the stream',
               'Merrily Merrily Merrily Merrily',
               'Life is but a dream...']

rowing_boat = Song(row_row_row)

rowing_boat.sing_me_a_song()

###########
# 3. Do more things??
print()
print()
print('-'*20)
print()
print()

class Song(object):

    def __init__(self, singer, song_name, lyrics):
        self.lyrics = lyrics
        self.singer = singer
        self.song_name = song_name

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def __str__(self):
        return f"{self.singer} will be performing {self.song_name}"


tonights_guest = Song('Frank Sinatra', 'Row Row Row Your Boat', row_row_row)

print(tonights_guest)
tonights_guest.sing_me_a_song()

####
# Classes are like blueprints or definitions for creating new mini-modules
# Instantiation is how you make one of these mini-modules and import it at the same time.
    # "Instantiate" just means to create an object from the class
# The resulting mini-module is called an object, and you then assign it to a variable to work with it
