"""

If you find yourself in a situation where you want to wrap
some complex behavior around a dict (or worse, dict of dicts),
see if you can instead refactor it into a collection of small,
easily understood classes.

"""

# Not too bad so far, but what it we want to include
# a player position preference?
foos = {'joe':
            {'wins': 5, 'losses': 5},
        'eric':
            {'wins': 7, 'losses': 5},
        'ryan':
            {'wins': 9, 'losses': 3},
        }

# Adding pos preference...
foos = {'joe':
        {'wins': 5, 'losses': 5, 'pos': 'goalie'},
        'eric':
        {'wins': 7, 'losses': 5, 'pos': 'goalie'},
        'ryan':
        {'wins': 9, 'losses': 3, 'pos': 'striker'},
        }

# Now what if we were to include add'l prefs?
foos = {'joe':
        {'wins': 5, 'losses': 5, 'prefs': {'pos': 'goalie'}},
        'eric':
        {'wins': 7, 'losses': 5, 'prefs': {'pos': 'goalie'}},
        'ryan':
        {'wins': 9, 'losses': 3, 'prefs': {'pos': 'striker'}},
        }
# Getting ugly now...

# Instead, implement nested dicts as helper classes
class WinLossRecord:
    def __init__(self, wins, losses):
        self.wins = wins
        self.losses = losses

    def total_games_played(self):
        return self.wins + self.losses

def FoosEntry:
    def __init__(self, name, win_loss_record, prefs):
        self.name = name
        self.win_loss_record = win_loss_record
        self.prefs = prefs

foosbook = []
foosbook.append(FoosEntry('joe', WinLossRecord(5,5), prefs=None))
foosbook.append(FoosEntry('eric', WinLossRecord(7,5), prefs=None))
foosbook.append(FoosEntry('ryan', WinLossRecord(9,3), prefs=None))

