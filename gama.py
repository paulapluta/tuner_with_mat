# Q: Po co na początku skryptów dodaje się coś takiego i czy/kiedy to jest potrzebne: "#! /usr/bin/..."?
# A: Żeby można było to uruchomić poleceniem w linii komend. Dojdziemy do tego.

# getting started, interacting with a user
print ("Enter a tone name, please :)")
# Q: Jak od wpisania "z palca" dojdziemy do zagrania na ukulele przed komputerem? Black magic & rocket science it is for me ;D
# A: Nasz długi proces ;)...

# defining a list of tone names in the chromatic scale
tone_list = ['c', 'd,' 'e', 'f', 'g', 'a', 'h', 'cis', 'dis', 'eis', 'fis', 'gis', 'ais', 'his', 'ces', 'des', 'es', 'fes', 'ges', 'as', 'b',
             'C', 'D', 'E', 'F', 'G', 'A', 'H',
             'CIS', 'CiS', 'CIs', 'Cis', 'cIS', 'ciS', 'cIs',
             'DIS', 'DiS', 'DIs', 'Dis', 'dIS', 'diS', 'dIs',
             'EIS', 'EiS', 'EIs', 'Eis', 'eIS', 'eiS', 'eIs',
             'FIS', 'FiS', 'FIs', 'Fis', 'fIS', 'fiS', 'fIs',
             'GIS', 'GiS', 'GIs', 'Gis', 'gIS', 'giS', 'gIs',
             'AIS', 'AiS', 'AIs', 'Ais', 'aIS', 'aiS', 'aIs',
             'HIS', 'HiS', 'HIs', 'His', 'hIS', 'hiS', 'hIs',
             'CES', 'CeS', 'CEs', 'Ces', 'cES', 'ceS', 'cEs',
             'DES', 'DeS', 'DEs', 'Des', 'dES', 'deS', 'dEs',
             'ES', 'eS', 'Es',
             'FES', 'FeS', 'FEs', 'Fes', 'fES', 'feS', 'fEs',
             'GES', 'GeS', 'GEs', 'Ges', 'gES', 'geS', 'gEs',
             'AS', 'aS', 'As',
             'B']
# Q: Czy w Pythonie stawia się gdzieś średniki?
# Q: Czy nasza lista dźwięków gamy jest "case sensitive"? A: yes.
# Q: Czy spacje na liście nają znaczenia? A: Tylko po to, żeby było czytelniej.
# Q: Kiedy/jak zdefiniujemy gamy wielokreślne itd.? A: Dojdziemy do tego.
# Q: Kiedy/jak zdefiniujemy częstotliwość każdego dźwięku? Sami czy użyjemy jakiejś biblioteki?
# Q: Kiedy zdefiniujemy jakie (G, C, E, A?) powinny być i jak powinny brzmieć dźwięki ukulele?

tone_name = input()

if tone_name not in tone_list:
    print ('Your choice, ' + tone_name + ', is not a tone name.', 'Lets try again!', sep='\n')
else:
    print ('Super! Enter another tone name if you wish :)')

# Nie wiem jak sprawić, żeby program kontynuował przyjmowanie zmiennych :/... A: Check 'while'...