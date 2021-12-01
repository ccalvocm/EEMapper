import ee


def cdl_key():
    """Four-class system (grain, forage, vegetable, orchard. Plus 5: non-ag/undefined"""
    key = {1: ('Corn', 1),
           2: ('Cotton', 1),
           3: ('Rice', 1),
           4: ('Sorghum', 1),
           5: ('Soybeans', 1),
           6: ('Sunflower', 1),
           7: ('', 5),
           8: ('', 5),
           9: ('', 5),
           10: ('Peanuts', 1),
           11: ('Tobacco', 2),
           12: ('Sweet Corn', 1),
           13: ('Pop or Orn Corn', 1),
           14: ('Mint', 2),
           15: ('', 5),
           16: ('', 5),
           17: ('', 5),
           18: ('', 5),
           19: ('', 5),
           20: ('', 5),
           21: ('Barley', 1),
           22: ('Durum Wheat', 1),
           23: ('Spring Wheat', 1),
           24: ('Winter Wheat', 1),
           25: ('Other Small Grains', 1),
           26: ('Dbl Crop WinWht/Soybeans', 1),
           27: ('Rye', 1),
           28: ('Oats', 1),
           29: ('Millet', 1),
           30: ('Speltz', 1),
           31: ('Canola', 1),
           32: ('Flaxseed', 1),
           33: ('Safflower', 1),
           34: ('Rape Seed', 1),
           35: ('Mustard', 1),
           36: ('Alfalfa', 3),
           37: ('Other Hay/Non Alfalfa', 3),
           38: ('Camelina', 1),
           39: ('Buckwheat', 1),
           40: ('', 5),
           41: ('Sugarbeets', 2),
           42: ('Dry Beans', 2),
           43: ('Potatoes', 2),
           44: ('Other Crops', 2),
           45: ('Sugarcane', 2),
           46: ('Sweet Potatoes', 2),
           47: ('Misc Vegs & Fruits', 2),
           48: ('Watermelons', 2),
           49: ('Onions', 2),
           50: ('Cucumbers', 2),
           51: ('Chick Peas', 2),
           52: ('Lentils', 2),
           53: ('Peas', 2),
           54: ('Tomatoes', 2),
           55: ('Caneberries', 2),
           56: ('Hops', 2),
           57: ('Herbs', 2),
           58: ('Clover/Wildflowers', 3),
           59: ('Sod/Grass Seed', 3),
           60: ('Switchgrass', 3),
           61: ('Fallow/Idle Cropland', 3),
           62: ('Pasture/Grass', 3),
           63: ('Forest', 5),
           64: ('Shrubland', 5),
           65: ('Barren', 5),
           66: ('Cherries', 4),
           67: ('Peaches', 4),
           68: ('Apples', 4),
           69: ('Grapes', 4),
           70: ('Christmas Trees', 4),
           71: ('Other Tree Crops', 4),
           72: ('Citrus', 4),
           73: ('', 5),
           74: ('Pecans', 4),
           75: ('Almonds', 4),
           76: ('Walnuts', 4),
           77: ('Pears', 4),
           78: ('', 5),
           79: ('', 5),
           80: ('', 5),
           81: ('Clouds/No Data', 5),
           82: ('Developed', 5),
           83: ('Water', 5),
           84: ('', 5),
           85: ('', 5),
           86: ('', 5),
           87: ('Wetlands', 5),
           88: ('Nonag/Undefined', 5),
           89: ('', 5),
           90: ('', 5),
           91: ('', 5),
           92: ('Aquaculture', 5),
           93: ('', 5),
           94: ('', 5),
           95: ('', 5),
           96: ('', 5),
           97: ('', 5),
           98: ('', 5),
           99: ('', 5),
           100: ('', 5),
           101: ('', 5),
           102: ('', 5),
           103: ('', 5),
           104: ('', 5),
           105: ('', 5),
           106: ('', 5),
           107: ('', 5),
           108: ('', 5),
           109: ('', 5),
           110: ('', 5),
           111: ('Open Water', 5),
           112: ('Perennial Ice/Snow', 5),
           113: ('', 5),
           114: ('', 5),
           115: ('', 5),
           116: ('', 5),
           117: ('', 5),
           118: ('', 5),
           119: ('', 5),
           120: ('', 5),
           121: ('Developed/Open Space', 5),
           122: ('Developed/Low Intensity', 5),
           123: ('Developed/Med Intensity', 5),
           124: ('Developed/High Intensity', 5),
           125: ('', 5),
           126: ('', 5),
           127: ('', 5),
           128: ('', 5),
           129: ('', 5),
           130: ('', 5),
           131: ('Barren', 5),
           132: ('', 5),
           133: ('', 5),
           134: ('', 5),
           135: ('', 5),
           136: ('', 5),
           137: ('', 5),
           138: ('', 5),
           139: ('', 5),
           140: ('', 5),
           141: ('Deciduous Forest', 5),
           142: ('Evergreen Forest', 5),
           143: ('Mixed Forest', 5),
           144: ('', 5),
           145: ('', 5),
           146: ('', 5),
           147: ('', 5),
           148: ('', 5),
           149: ('', 5),
           150: ('', 5),
           151: ('', 5),
           152: ('Shrubland', 5),
           153: ('', 5),
           154: ('', 5),
           155: ('', 5),
           156: ('', 5),
           157: ('', 5),
           158: ('', 5),
           159: ('', 5),
           160: ('', 5),
           161: ('', 5),
           162: ('', 5),
           163: ('', 5),
           164: ('', 5),
           165: ('', 5),
           166: ('', 5),
           167: ('', 5),
           168: ('', 5),
           169: ('', 5),
           170: ('', 5),
           171: ('', 5),
           172: ('', 5),
           173: ('', 5),
           174: ('', 5),
           175: ('', 5),
           176: ('Grassland/Pasture', 5),
           177: ('', 5),
           178: ('', 5),
           179: ('', 5),
           180: ('', 5),
           181: ('', 5),
           182: ('', 5),
           183: ('', 5),
           184: ('', 5),
           185: ('', 5),
           186: ('', 5),
           187: ('', 5),
           188: ('', 5),
           189: ('', 5),
           190: ('Woody Wetlands', 5),
           191: ('', 5),
           192: ('', 5),
           193: ('', 5),
           194: ('', 5),
           195: ('Herbaceous Wetlands', 5),
           196: ('', 5),
           197: ('', 5),
           198: ('', 5),
           199: ('', 5),
           200: ('', 5),
           201: ('', 5),
           202: ('', 5),
           203: ('', 5),
           204: ('Pistachios', 4),
           205: ('Triticale', 1),
           206: ('Carrots', 2),
           207: ('Asparagus', 2),
           208: ('Garlic', 2),
           209: ('Cantaloupes', 2),
           210: ('Prunes', 2),
           211: ('Olives', 2),
           212: ('Oranges', 3),
           213: ('Honeydew Melons', 2),
           214: ('Broccoli', 2),
           215: ('Avocados', 2),
           216: ('Peppers', 2),
           217: ('Pomegranates', 4),
           218: ('Nectarines', 4),
           219: ('Greens', 2),
           220: ('Plums', 4),
           221: ('Strawberries', 2),
           222: ('Squash', 2),
           223: ('Apricots', 4),
           224: ('Vetch', 3),
           225: ('Dbl Crop WinWht/Corn', 1),
           226: ('Dbl Crop Oats/Corn', 1),
           227: ('Lettuce', 2),
           228: ('', 1),
           229: ('Pumpkins', 2),
           230: ('Dbl Crop Lettuce/Durum Wht', 2),
           231: ('Dbl Crop Lettuce/Cantaloupe', 2),
           232: ('Dbl Crop Lettuce/Cotton', 2),
           233: ('Dbl Crop Lettuce/Barley', 2),
           234: ('Dbl Crop Durum Wht/Sorghum', 1),
           235: ('Dbl Crop Barley/Sorghum', 1),
           236: ('Dbl Crop WinWht/Sorghum', 1),
           237: ('Dbl Crop Barley/Corn', 1),
           238: ('Dbl Crop WinWht/Cotton', 1),
           239: ('Dbl Crop Soybeans/Cotton', 1),
           240: ('Dbl Crop Soybeans/Oats', 1),
           241: ('Dbl Crop Corn/Soybeans', 1),
           242: ('Blueberries', 2),
           243: ('Cabbage', 2),
           244: ('Cauliflower', 2),
           245: ('Celery', 2),
           246: ('Radishes', 2),
           247: ('Turnips', 2),
           248: ('Eggplants', 2),
           249: ('Gourds', 2),
           250: ('Cranberries', 2),
           251: ('', 5),
           252: ('', 5),
           253: ('', 5),
           254: ('Dbl Crop Barley/Soybeans', 1),
           255: ('', 5)}
    return key


def remap_cdl():
    """remap cdl to alternative class system, return tuple (original, remapped)"""
    key = cdl_key()
    map_ = list(key.keys())
    remap = [v[1] for k, v in key.items()]
    return map_, remap


def get_cdl(yr):
    cultivated, crop = None, None
    cdl_years = [x for x in range(1997, 2021)]
    cultivated_years = [x for x in range(2013, 2019)]

    mode_reduce = ee.Reducer.mode()

    first = True
    for y in cultivated_years:
        image = ee.Image('USDA/NASS/CDL/{}'.format(y))
        cultivated = image.select('cultivated')
        cultivated = cultivated.remap([1, 2], [0, 1])
        if first:
            cultivated = cultivated.rename('clt_{}'.format(y))
            first = False
        else:
            cultivated.addBands(cultivated.rename('clt_{}'.format(y)))

    cultivated = cultivated.reduce(mode_reduce).resample('bilinear').rename('cdl')

    if yr in cdl_years:
        image = ee.Image('USDA/NASS/CDL/{}'.format(yr))
        crop = image.select('cropland')
    else:
        first = True
        for y in cdl_years:
            image = ee.Image('USDA/NASS/CDL/{}'.format(y))
            crop = image.select('cropland')
            if first:
                crop = crop.rename('crop_{}'.format(y))
                first = False
            else:
                crop.addBands(crop.rename('crop_{}'.format(y)))
        crop = crop.reduce(mode_reduce).rename('cropland')

    cdl_keys, our_keys = remap_cdl()
    simple_crop = crop.remap(cdl_keys, our_keys).rename('crop5c').resample('bilinear')
    return cultivated, crop, simple_crop


if __name__ == '__main__':
    pass
# ========================= EOF ====================================================================
