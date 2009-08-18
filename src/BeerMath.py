#!/bin/python

def kg2oz(object):
    conv = 28.3495
    object = object * 1000
    object = object / conv
    return round(object, 3)

def kg2g(object):
    object = object * 1000
    return round(object, 3)

def g2kg(object):
    object = object / 1000
    return round(object, 3)

def g2oz(object):
    conv = 28.3495
    object = object / conv
    return round(object, 3)

def oz2kg(object):
    conv = 28.3495
    object = conv * object
    object = object / 1000
    return round(object, 3)

def oz2g(object):
    conv = 28.3495
    object = conv * object
    return round(object, 3)

def sg2ball(gravity):
    gravity = 259 / gravity
    return round(gravity, 3)

def ball2sg(gravity):
    gravity = 259 / (259 - gravity)
    return round(gravity, 1)

def gal2l(volume):
    return round(volume * 3.78541178,3)

def qt2l(volume):
    return round(volume * 3.78541178 / 4.0,3)

def calc_abv(ig, fg):
    diffgrav = ig - fg
    return round(diffgrav / .75,2)


def calc_ibu(hop, gravity_sg, volume_l, time_mins):
    aa_perc = hop.alpha / 100
    bigness = 1.65 * .000125 ** (gravity_sg - 1)
    boil = (1 - 2.718281828459045235 ** (-0.04 * time_mins)) / 4.15
    dec_aau = bigness * boil
    if hop.form == 'Pellet':
        dec_aau = dec_aau * 1.1
    dens_aa = (aa_perc * hop.amount * 1000 * 1000 )/volume_l
    return round(dec_aau * dens_aa,1)


