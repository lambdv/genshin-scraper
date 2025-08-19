import wikiscrapper  as wiki
import tclscrapper   as tcl
import os
import time as timer
import json
import manager as m
import utils

weapons = [
    "Flame-Forged Insight",
    "Fractured Halo"
]

for weapon in weapons:
    imgs = wiki.scrapeWeaponAssets(weapon)
    utils.saveIMGS(weapon, imgs, "./genshindata/public/assets/weapons", override=True)







