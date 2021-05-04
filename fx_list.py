# available: 70 onwards

# + or - 5% of a quality
def __init_0__(self,polarity):
    self.msg = "{}{}% Maximum health on wearer"
def __init_1__(self,polarity):
    self.msg = "{}{}% Maximum overheal on wearer"
def __init_2__(self,polarity):
    self.msg = "{}{}% Damage dealt"
def __init_3__(self,polarity):
    self.msg = "{}{}% Firing rate"
def __init_4__(self,polarity):
    self.msg = "{}{}% Reload rate"
def __init_5__(self,polarity):
    self.msg = "{}{}% Clip size"
def __init_6__(self,polarity):
    self.msg = "{}{}% Maximum ammo"
def __init_7__(self,polarity):
    self.msg = "{}{}% Random bullet spread"
def __init_8__(self,polarity):
    self.msg = "{}{}% Accuracy"
def __init_9__(self,polarity):
    self.msg = "{}{}% Speed on wearer"
def __init_10__(self,polarity):
    self.msg = "{}{}% Speed while deployed"
def __init_11__(self,polarity):
    self.msg = "{}{}% Switch-to speed"
def __init_12__(self,polarity):
    self.msg = "{}{}% Switch-from speed"
def __init_13__(self,polarity):
    self.msg = "{}{}% Knockback dealt"
def __init_14__(self,polarity):
    self.msg = "{}{}% Knockback taken on wearer"
def __init_15__(self,polarity):
    self.msg = "{}{}% Knockback taken while deployed"
def __init_16__(self,polarity):
    self.msg = "{}{}% Jump height on wearer"
def __init_17__(self,polarity):
    self.msg = "{}{}% Jump height while deployed"
def __init_31__(self,polarity):
    self.msg = "{}{}% Pellets per shot"
def __init_40__(self,polarity):
    self.msg = "{}{}% Explosion radius"
def __init_41__(self,polarity):
    self.msg = "{}{}% Projectile speed"
def __init_42__(self,polarity):
    self.msg = "{}{}% Damage dealt against buildings"
def __init_43__(self,polarity):
    self.msg = "{}{}% Health gained from all sources on wearer"
def __init_44__(self,polarity):
    self.msg = "{}{}% Air turn control on wearer"
def __init_45__(self,polarity):
    self.msg = "{}{}% Fall damage taken on wearer"
def __init_46__(self,polarity):
    self.msg = "{}{}% Maximum primary ammo on wearer"
def __init_47__(self,polarity):
    self.msg = "{}{}% Maximum secondary ammo on wearer"
def __init_48__(self,polarity):
    self.msg = "{}{}% Flame size"
def __init_49__(self,polarity):
    self.msg = "{}{}% Airblast cost"
def __init_50__(self,polarity):
    self.msg = "{}{}% Afterburn damage dealt"
def __init_51__(self,polarity):
    self.msg = "{}{}% Melee range"
def __init_52__(self,polarity):
    self.msg = "{}{}% Melee bounds"
def __init_53__(self,polarity):
    self.msg = "{}{}% Air movement control"
def __init_54__(self,polarity):
    self.msg = "{}{}% Damage dealt on crit"
def __init_55__(self,polarity):
    self.msg = "{}{}% Damage dealt on mini-crit"
def __init_56__(self,polarity):
    self.msg = "{}{}% Spacing between pellets"
def __init_58__(self,polarity):
    self.msg = "{}{}% Spin-up speed"
def __init_59__(self,polarity):
    self.msg = "{}{}% Speed while spun-up"
def __init_60__(self,polarity):
    self.msg = "{}{}% Damage taken while spun-up"
def __init_61__(self,polarity):
    self.msg = "{}{}% Heal rate"
def __init_62__(self,polarity):
    self.msg = "{}{}% Overheal"
def __init_63__(self,polarity):
    self.msg = "{}{}% Uber build rate"
def __init_64__(self,polarity):
    self.msg = "{}{}% Uber drain rate"
def __init_66__(self,polarity):
    self.msg = "{}{}% Sap damage"
def __init_70__(self,polarity):
    self.msg = "{}{}% Sapper health"
def __init_71__(self,polarity):
    self.msg = "{}{}% Damage dealt on backstab"

# assorted fill-in-the-blank kinds of fx
def __init_18__(self,polarity):
    self.msg = "+{}% Damage {} against {} on wearer"
def __init_19__(self,polarity):
    self.msg = "+{}% Damage {} against {} while deployed"
def __init_20__(self,polarity):
    self.msg = "Damage dealt with this weapon against {} is {}"
def __init_21__(self,polarity):
    self.msg = "On hit: Target {} {}"

# things that can be either + or -
def __init_22__(self,polarity):
    if polarity == '+':
        self.msg = "This weapon has random crits"
    elif polarity == '-':
        self.msg = "No random crits"
def __init_23__(self,polarity):
    if polarity == '+':
        self.msg = "Crits against the user are converted to mini-crits"
    elif polarity == '-':
        self.msg = "Mini-crits against the user are converted to crits"
def __init_24__(self,polarity):
    if polarity == '+':
        self.msg = "This weapon deals critical damage when it would normally deal mini-crits"
    elif polarity == '-':
        self.msg = "This weapon deals mini-crit damage when it would normally deal crits"

# positive-only effects
def __init_25__(self,polarity):
    self.msg = "Wearer cannot be backstabbed"
def __init_26__(self,polarity):
    self.msg = "Wearer cannot be headshot"
def __init_27__(self,polarity):
    self.msg = "Wearer has 1 extra mid-air jump"
def __init_28__(self,polarity):
    self.msg = "Wearer has 1 extra mid-air jump while this weapon is deployed"
def __init_65__(self,polarity):
    self.msg = "This weapon has random crits"
def __init_67__(self,polarity):
    self.msg = "This sapper rapidly downgrades buildings"
def __init_68__(self,polarity):
    self.msg = "This sapper drains health from buildings"
        
# negative-only effects
def __init_29__(self,polarity):
    self.msg = "Wearer cannot jump"
def __init_30__(self,polarity):
    self.msg = "If one shot is in the clip when reloading, it is lost"
def __init_69__(self,polarity):
    self.msg = "This sapper rapidly upgrades buildings"
def __init_72__(self,polarity):
    self.msg = "Backstabs with this weapon only deal mini-crit damage"
def __init_73__(self,polarity):
    self.msg = "This weapon cannot backstab"

# plus/minus 1-5
def __init_32__(self,polarity):
    self.msg = "{}{} Health regen per sec"

# plus-only 1-5 (with a few exceptions)
def __init_33__(self,polarity):
    self.msg = "{}{} Degrees of random deviation in accuracy"
def __init_34__(self,polarity):
    self.msg = "{}{} Bullets per shot"
def __init_35__(self,polarity):
    self.msg = "{}{} Rockets per shot"
def __init_36__(self,polarity):
    self.msg = "{}{} Pipes per shot"
def __init_37__(self,polarity):
    self.msg = "{}{} Stickybombs per shot"
def __init_38__(self,polarity):
    self.msg = "{}{} Needles per shot"
def __init_39__(self,polarity):
    self.msg = "{}{} Arrows per shot"
def __init_57__(self,polarity):
    self.msg = ""

# fx for this file's use only
inW = [2,3,8,11,12,13,18,19,20,21,22,24,33,42,54,55]

# the following are collectives of fx that belong to certain qualities
pol_perc = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,31,40,41,42,43,44,45,46,
            47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,66,70,71] # polarity percent fx

multiple = [18,19,20,21]
perc_res_src = [18,19]
src_crit = [20]
on_hit_sec = [21]

pol_one = [32]
plus_one = [33,34,35,36,37,38,39]
pos_or_neg = [22,23,24]

zero = [22,23,24,25,26,27,28,29,30,65,67,68,69,72,73]

# fx for types of weapons
types_wp = {
            'Primary':[47],
            'Secondary':[46],
            'Melee':[51,52,46,47] + inW,
            'General':[0,1,9,10,14,15,16,17,18,23,43,44,45,32,53,25,26,27,28,29]
            } # can be put to all weapons, whether gun or wearable

# fx for kinds of weapons
kinds_wp = {'Scattergun':[4,5,6,7,30,31,56] + inW,
            'Pistol':[4,5,6,7,30,34] + inW,
            'Rocket':[4,5,6,7,30,40,41,35] + inW,
            'Shotgun':[4,5,6,7,30,34] + inW,
            'Flamethrower':[6,7,48,49,50] + inW,
            'Pipe':[4,5,6,7,30,40,41,36] + inW,
            'Sticky':[4,5,6,7,30,40,41,37] + inW,
            'Minigun':[6,7,34,58,59,60] + inW,
            'Wrench':[],
            'Needle':[4,5,6,7,30,38] + inW,
            'Medigun':[11,12,61,62,63,64],
            'Rifle':[4,5,6,7,30,34,65] + inW,
            'SMG':[4,5,6,7,30,34] + inW,
            'Revolver':[4,5,6,7,30,34] + inW,
            'Sapper':[11,12,66,67,68,69,70],
            'Knife':[71,72,73]}

# special qualities that fx possess
reverse_polarity = [14,15,45,56,64]
pos_only = [25,26,27,28,34,35,36,37,38,39,65,67,68]
neg_only = [29,30,33,69,72,73]
