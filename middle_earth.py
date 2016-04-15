def goodVsEvil(good, evil):
    #point values for each race
    good_values = {'Hobbits': 1, 'Men': 2, 'Elves': 3, 'Dwarves': 3, 'Eagles': 4, 'Wizards': 10}
    evil_values = {'Orcs': 1, 'Men': 2, 'Wargs': 2, 'Goblins': 2, 'Uruk Hai': 3, 'Trolls': 5, 'Wizards': 10}
    #list of good and evil races
    good_army_races = ['Hobbits', 'Men', 'Elves', 'Dwarves', 'Eagles', 'Wizards']
    evil_army_races = ['Orcs', 'Men', 'Wargs', 'Goblins', 'Uruk Hai', 'Trolls', 'Wizards']
    #list of good and evil values
    good_list = good.split()
    evil_list = evil.split()
    #create dictionary of army numbers
    good_army = dict(zip(good_army_races, good_list))
    evil_army = dict(zip(evil_army_races, evil_list))
    #calculate good army's totals
    good_total = 0
    for k,v in good_army.iteritems():
        good_total += int(v) * good_values[k]
    #calculate evil army's totals 
    evil_total = 0
    for k,v in evil_army.iteritems():
        evil_total += int(v) * evil_values[k]
    #determine the winner
    if good_total > evil_total:
        return "Battle Result: Good triumphs over Evil"
    elif evil_total > good_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else: 
        return "Battle Result: No victor on this battle field"


