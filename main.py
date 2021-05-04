from fx import get_attributes
from random import choice
from var import n_class,n_slot,get_kind_wp

i = 0
while True:
    class_tf = choice(n_class)
    slot_tf = choice(n_slot)
    kind_wp = get_kind_wp(class_tf,slot_tf)
    
    weapon = get_attributes(class_tf,slot_tf,kind_wp)
    print('=======================================')
    print('A {} for the {}\n'.format(kind_wp,class_tf))
    print('+')
    for pos_atr in weapon[0]:
        print(pos_atr)
    print('\n-')
    for neg_atr in weapon[1]:
        print(neg_atr)
    print('=======================================')
    i += 1
    print(i)
    input('')
