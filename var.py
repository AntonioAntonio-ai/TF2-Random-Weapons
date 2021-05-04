n_class = ['Scout','Soldier','Pyro','Demoman','Heavy','Engineer','Medic','Sniper','Spy']
n_slot = ['Primary','Secondary','Melee']

w_all = [['Scattergun','Pistol','Bat'],
        ['Rocket','Shotgun','Shovel'],
        ['Flamethrower','Shotgun','Axe'],
        ['Pipe','Sticky','Bottle'],
        ['Minigun','Shotgun','Fists'],
        ['Shotgun','Pistol','Wrench','Construction PDA','Destruction PDA'],
        ['Needle','Medigun','Bonesaw'],
        ['Rifle','SMG','Kukri'],
        ['Revolver','Sapper','Knife','Watch','Disguise Kit']]

def get_kind_wp(class_tf,slot_tf):
    return(w_all[n_class.index(class_tf)][n_slot.index(slot_tf)])
def get_type_wp(kind_wp,class_tf):
    all_types = ['Primary','Secondary','Melee']
    return(all_types[w_all[n_class.index(class_tf)].index(kind_wp)])
#print(get_type_wp('Shotgun','Soldier'))
#print(get_kind_wp('Spy','Quaternary'))
'''
{} Maximum health bonus/penalty, 5%-100%
{} Health regen bonus/penalty, 1-5
Wearer starts life with {} extra/less health, 10-100
{} Health gain/loss on... 5%-100%
        switch-to
        switch-to without kill (Honorbound)
        switch-from
        switch-from without kill (Honorbound)
        fire
        hit
        kill
        health gain
        health loss
        jump
        walk
{} Bonus/Penalty healing from..., 5%-100%
        all sources
        dispensers
        medi-guns
        healthpacks
        dispensers and medi-guns
{} Overheal bonus/penalty from medi-guns, 5%-100%
Shots heal teammates for {} damage, 5-100
{} Damage resistance/vulnerability on wearer/deployed for... 5%-100%
        all sources
        bullet damage
        explosive damage
        fire damage
        melee damage
        falling damage
        environmental damage
        sentries
        bleed damage
        critical damage
        mini-crit damage
[for Soldier, Demoman, Engineer] the above for self-inflicted damage
Critical damage against the wearer/deployed is converted to mini-crit damage/vice versa
{} damage taken/dealt by the wearer/deployed has a bonus/penalty or deals mini-crits/crits/no damage vs... 5%-100% or N/A
        Class-specific
        Burning targets
        Wet targets
        Jarated targets
        Mad Milked targets
        Gasolined targets
        Taunting targets
        Airborne targets
        Launched targets (rocket jumping, etc.)
        Disguised/cloaked targets
        Overhealed targets
        Uber-ready targets
        Targets above/below 50% health
        Targets with full health
On hit:
        Target ignites
        Target is marked for death
        Target is Jarated
        Target is Mad Milk'd
        Target is covered in gasoline
        Target is crit boosted
        Target is mini-crit boosted
        Target is slowed
        Target is stunned
        Target is inflicted with bleed
        Target gains a speed boost
        Target is disguised
        Target is cloaked
        Target is colorblind
        
{} firing rate bonus/penalty, 5%-100%
{} reload rate bonus/penalty, 5%-100%
{} maximum ammo bonus/penalty, 5%-100%
'''

# things for attributes
p5_halve  = range(5,50,5)
p5_double = range(5,100,5)

sec = ['for 1 second', 'for 2 seconds', 'for 3 seconds', 'for 4 seconds', 'for 5 seconds', 'for 6 seconds', 'for 7 seconds', 'for 8 seconds', 'for 9 seconds', 'for 10 seconds', 'for 11 seconds', 'for 12 seconds', 'until death']
one = [1,2,3,4,5]

resvul = ['all sources of damage',
          'bullet damage',
          'explosive damage',
          'fire damage',
          'melee damage',
          'falling damage',
          'sentry damage',
          'critical damage',
          'short-range damage',
          'medium-range damage',
          'long-range damage']
hitcrit = ['enemy Scouts',
          'enemy Soldiers',
          'enemy Pyros',
          'enemy Demomen',
          'enemy Heavies',
          'enemy Engineers',
          'enemy Medics',
          'enemy Snipers',
          'enemy Spies',
          'disguised targets',
          'cloaked targets',
          'burning targets',
          'wet targets',
          'airborne targets',
          'launched targets',
          'targets with more than 50% health',
          'targets with less than 50% health',
          'targets with 100% health',
          'targets with less than 100% health',
          'overhealed targets',
          'Uber-ready targets']
on_hit_pos = ['ignites',
              'is doused in Jarate',
              "is doused in Mad Milk",
              'is doused in gasoline',
              'is slowed',
              'is stunned',
              'is inflicted with bleed',]
on_hit_neg = ['is crit boosted',
              'is mini-crit boosted',
              'gains a speed boost',
              'becomes disguised',
              'is cloaked',
              'becomes invulnerable']
effect_on = ['switch-to',
        'switch-to without kill',
        'switch-from',
        'switch-from without kill',
        'fire',
        'hit',
        'kill',
        'health gain',
        'health loss',
        'jump',
        'walk']
uber_type = ['Invulnerability',
             'Crit Boost',
             'Mini-Crit Boost',
             'Megaheal',
             'Triple Overheal',
             'Vaccinator',
             'Double Speed',
             'Invisibility',
             'Quintuple Jump',
             'Triple Fire Speed',
             'Grow',
             'Shield',
             'Counter']
