class InteractingWithUser:
    def say_hi(self):
        print('Enter a tone name, please :)')

    def tone_name(self):
        self.tone_list = ['c', 'd,' 'e', 'f', 'g', 'a', 'h', 'cis', 'dis', 'eis', 'fis', 'gis', 'ais', 'his', 'ces', 'des',
                     'es', 'fes', 'ges', 'as', 'b',
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

        tone_name = input()

        if tone_name not in tone_list:
            print('Your choice, ' + tone_name + ', is not a tone name.')

        else:
            print('Super!')

    def another_tone(self):
        print ('Would you like to try another tone?')

        #if yes > def tone_name
        #if no > print('Thanks, see you again!')

a = InteractingWithUser()
a.say_hi()