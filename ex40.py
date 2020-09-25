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

but_not_for_me = Song(["They're writing songs of love",
                       "But not for me",
                       "A lucky star's above",
                       "But not for me"])

just_friends = Song(["Just friends",
                     "Lovers no more",
                     "Just friends",
                     "But not like before"])

but_not_for_me.sing_me_a_song()
just_friends.sing_me_a_song()

print("-" * 20)

class Sang(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    alive = ["I'm thankful for every breath I take",
             "I won't take you for granted"]

python_sing = Sang("LOVE")

python_sing.sing_me_a_song()

print(python_sing.alive)
