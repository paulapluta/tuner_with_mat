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

# user specifies a tone
def getTone():
    print("Enter a tone name, please!")
    tone_name = input()

    if tone_name in tone_list:
        print ('Cool :)')
    else:
        print ('Buu :(')

getTone()


