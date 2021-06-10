def witch_hunt(suspect_sets, innocent_sets):
    f = set()
    g = set()
    for i in suspect_sets:
        if len(f) == 0:
            f = i.difference(f)
        else:
            f = f.intersection(i)
    for i in innocent_sets:
        if len(g) == 0:
            g = i.difference(g)
        else:
            g = g.union(i)
    return f.difference(g)

# from Sprints.Sprint02.Sprint02_02_Witch_hunt import witch_hunt
#
# def run_test(suspect_sets, innocent_sets):
#     witches = witch_hunt(suspect_sets, innocent_sets)
#     assert isinstance(witches, set)
#     print(f'Witches found: {sorted(list(witches))}')
#
# if __name__ == '__main__':
#     can_read = {'Keeva', 'Daegal', 'Adam', 'Bellatrix', 'Ulrich', 'Keene',
#                 'Evanora', 'Earthan', 'Paxton', 'Alice', 'Candice', 'Cedonia',
#                 'Zelig', 'Lydia', 'Mortimer'}
#     talk_to_self = {'Candice', 'Lydia', 'Chilton', 'Alice', 'Cedonia',
#                     'Minerva', 'Adam', 'Daegal', 'Camilla', 'Keene',
#                     'Chalmers', 'Keeva', 'Paxton'}
#     healers = {'Bellatrix', 'Cullen', 'Adam', 'Alice', 'Lydia', 'Ulrich',
#                'Zelig', 'Cedonia', 'Paris', 'Chalmers', 'Chilton',
#                'Minerva', 'Paxton', 'Mortimer', 'Earthan', 'Daegal'}
#     wealthy = {'Chalmers', 'Keeva', 'Alice', 'Cullen', 'Minerva'}
#     men = {'Keene', 'Zelig', 'Mortimer', 'Adam', 'Ulrich', 'Chalmers',
#            'Paxton', 'Cullen', 'Chilton', 'Earthan', 'Daegal'}
#
#     run_test([can_read, talk_to_self, healers], [wealthy, men])
#     run_test([], [wealthy, men])
#     run_test([can_read, talk_to_self, healers], [])