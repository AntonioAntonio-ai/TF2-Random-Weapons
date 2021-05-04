from random import choice
from random import randint
import var
import fx_list

def get_attributes(class_tf,slot_tf,kind_wp):
    pos = randint(1,4)
    neg = randint(1,4)

    pos_fx = []
    neg_fx = []

    exceptions = []
    for p in range(0, pos):
        atr = Attribute('+',exceptions, class_tf, slot_tf, kind_wp)
        exceptions += atr.get_num(True)
        pos_fx += [atr.get_msg()]
    for n in range(0, neg):
        atr = Attribute('-',exceptions, class_tf, slot_tf, kind_wp)
        exceptions += atr.get_num(True)
        neg_fx += [atr.get_msg()]

    return(pos_fx,neg_fx)

class Attribute():
    def __init__(self, polarity, exception, class_tf='Scout', slot_tf='Primary', kind_wp='Scattergun'):
        self.poss = [] + fx_list.types_wp['General']

        # determine the sets of fx to pull from
        if kind_wp in fx_list.kinds_wp:
            self.poss += fx_list.kinds_wp[kind_wp]
        if slot_tf in fx_list.types_wp:
            self.poss += fx_list.types_wp[slot_tf]
        
        # take out given exceptions
        for x in exception:
            if x in self.poss:
                if x not in fx_list.multiple:
                    self.poss.pop(self.poss.index(x))
        # and also take out bad fx
        if polarity == '+':
            for n in fx_list.neg_only:
                if n in self.poss:
                    self.poss.pop(self.poss.index(n))
        elif polarity == '-':
            for p in fx_list.pos_only:
                if p in self.poss:
                    self.poss.pop(self.poss.index(p))

        self.num = choice(self.poss)
        exec('fx_list.__init_{}__(self,polarity)'.format(self.num))

        # special qualities go first
        if self.num in fx_list.reverse_polarity:
            if polarity == '+':
                polarity = '-'
            elif polarity == '-':
                polarity = '+'

        # now format self.msg
        if self.num in fx_list.pol_perc:
            if polarity == '+':
                used = var.p5_double
            elif polarity == '-':
                used = var.p5_halve
            self.val = choice(used)
            
            self.msg = self.msg.format(polarity,self.val)
        elif self.num in fx_list.perc_res_src:
            if polarity == '+':
                used = var.p5_halve
                polarity = 'resistance'
            elif polarity == '-':
                used = var.p5_double
                polarity = 'vulnerability'
            self.val = choice(used)

            self.msg = self.msg.format(self.val,polarity,choice(var.resvul))
        elif self.num in fx_list.src_crit:
            if polarity == '+':
                used = choice(['converted to critical damage', 'converted to mini-crit damage'])
            elif polarity == '-':
                used = 'nullified'

            self.msg = self.msg.format(choice(var.hitcrit),used)
        elif self.num in fx_list.on_hit_sec:
            if polarity == '+':
                used = choice(var.on_hit_pos)
            elif polarity == '-':
                used = choice(var.on_hit_neg)

            self.msg = self.msg.format(used,choice(var.sec))
        elif self.num in fx_list.pol_one:
            self.msg = self.msg.format(polarity,choice(var.one))
        elif self.num in fx_list.plus_one:
            self.msg = self.msg.format('+',choice(var.one))
        
    def get_msg(self):
        return(self.msg)
    def get_num(self, excepted=False):
        if not excepted:
            return([self.num])
        else:
            exceptions = []
            # jump stuff
            if self.num in [16,17,25,26]:
                exceptions = [29]
            elif self.num in [29]:
                exceptions = [16,17,25,26]
            return(exceptions)
    def get_value(self):
        return(self.val)
