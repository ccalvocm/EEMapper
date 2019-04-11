# ===============================================================================
# Copyright 2018 dgketchum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## UCRB is going with the pure state input data for now.
# 'UCRB_WY': ('ft:1M0GDErc0dgoYajU_HStZBkp-hBL4kUiZufFdtWHG', [1989, 1996, 2010, 2013, 2016], 0.5),  # a.k.a. 2000
# 'UCRB_UT_CO': ('ft:1Av2WlcPRBd7JZqYOU73VCLOJ-b5q6H5u6Bboebdv', [1998, 2003, 2006, 2013, 2016], 0.5),  # a.k.a. 2005
# 'UCRB_UT': ('ft:144ymxhlcv8lj1u_BYQFEC1ITmiISW52q5JvxSVyk', [1998, 2003, 2006, 2013, 2016], 0.5),  # a.k.a. 2006
# 'UCRB_NM': ('ft:1pBSJDPdFDHARbdc5vpT5FzRek-3KXLKjNBeVyGdR', [1987, 2001, 2004, 2007, 2016], 0.4),  # a.k.a. 2009
# ===============================================================================

import os
from datetime import datetime

import ee
# from pprint import pprint
from map.assets import list_assets

ROI = 'users/dgketchum/boundaries/western_states_expanded_union'
BOUNDARIES = 'users/dgketchum/boundaries'
ASSET_ROOT = 'users/dgketchum/classy_v2'
IRRIGATION_TABLE = 'users/dgketchum/irr_attrs/harney'
HUC_6 = 'users/dgketchum/usgs_wbd/huc6_semiarid_clip'
HUC_8 = 'users/dgketchum/usgs_wbd/huc8_semiarid_clip'
COUNTIES = 'users/dgketchum/boundaries/western_counties'

STATES = ['AZ', 'CA', 'CO', 'ID', 'MT', 'NM', 'NV', 'OR', 'UT', 'WA', 'WY']

EDIT_STATES = ['KS', 'ND', 'NE', 'OK', 'SD', 'TX']
TARGET_STATES = ['MT', 'CO']

POINTS_MT = 'ft:1quoEOgOl5dTQtYjyHZs9BxX8CZz1Leqv5qqFYLml'
POINTS = 'ft:11GT2ikIkgqzYLb0R9tICu8PW7-lo7d-0GFutcywX'
VALIDATION_POINTS = 'ft:1F6qGFzg1M1WRPIJ8rnNsQLCk932pGpqL2-MRcOYd'
TABLE = 'ft:1wLrSEoQie6u7wTPl1bJ7rLEq20OLvQncecM3_HeH'
TABLE_V2 = 'ft:1UYtOA4d8_WFy_wq2ahyfdokuC1q9BMPLoaa1H94Z'

IRR = {
    # 'Acequias': ('ft:1j_Z6exiBQy5NlVLZUe25AsFp-jSfCHn_HAWGT06D', [1987, 2001, 2004, 2007, 2016], 0.5),
    # 'AZ': ('ft:1ZwRYaGmMc7oJuDTrKbrZm3oL7yBYdeKjEa05n5oX', [2001, 2003, 2004, 2007, 2016], 0.5),
    # 'CO_DIV1': ('ft:1wRNUsKChMUb9rUWDbxOeGeTaNWNZUA0YHXSLXPv2', [1998, 2003, 2006, 2013, 2016], 0.5),
    # 'CO_SanLuis_test': ('ft:1mcBXyFw1PoVOoAGibDpZjCgb001jA_Mj_hyd-h92', [2016], 0.5),
    # 'CA_v2': ('ft:1LRHed3EWaa1UNKTU1e3jIHqwldMP-MGN6_xB_YjK', [2014], 0.5),
    # 'EastStates': ('ft:1AZUak3iuAtah1SHpkLfw0IRk_U5ei23VsPzBWxpD', [1987, 2001, 2004, 2007, 2016], 0.5),
    # 'OK': ('ft:1EjuYeilOTU3el9GsYZZXCi6sNC7z_jJ6mGa2wHIe', [2006, 2007, 2011, 2013, 2015], 0.5),
    # 'NE': ('ft:1789J-j1dq8_Ez6wfObJxGSJaxRkuJsZMFLeeiwPo', [2003, 2006, 2009, 2013, 2016], 0.5),
    'ID_Bonner': ('ft:1kkaQomLStq-zf8Dpg2eTIrRdn_2Aw5g6lagZrdiK', [1988, 1998, 2001, 2006, 2009, 2017], 0.5),
    # 'NM_SanJuan': ('ft:1_-haRl7-ppkBYWBN-cPzItftKQC7yWI7sfgoVx1R', [1987, 2001, 2004, 2007, 2016], 0.5),
    # 'NV': ('ft:1DUcSDaruwvXMIyBEYd2_rCYo8w6D6v4nHTs5nsTR', [x for x in range(2001, 2011)], 0.5),
    # 'MT_Turner': ('ft:1PpvhFdLDG4oCh7OsVcjJX6vg8FNB0FWUIFqRKYxO', [2008, 2009, 2010, 2011, 2012, 2013], 0.5),
    # 'OR': ('ft:1FJMi4VXUe4BrhU6u0OF2l0uFU_rGUe3rFrSSSBVD', [1994, 1997, 2011], 0.5),
    # 'NW_OR': ('ft:1kXr3oMe9Ybsd3N7tyBBDCTweAxb4c8GBz6B8_ELm', [1994, 1996, 1997, 2001, 2011, 2013], 0.5),
    # 'UT': ('ft:1oA0v3UUBQj3qn9sa_pDJ8bwsAphfRZUlwwPWpFrT', [1998, 2003, 2006, 2013, 2016], 0.5),
    # 'UT_CO': ('ft:1Av2WlcPRBd7JZqYOU73VCLOJ-b5q6H5u6Bboebdv', [1998, 2003, 2006, 2013, 2016], 0.5),
    # 'WA': ('ft:1tGN7UdKijI7gZgna19wJ-cKMumSKRwsfEQQZNQjl', [1997, 1996], 0.5),
    # 'WY': ('ft:1nB1Tg_CcmuhXtbnCE3wKVan0ERqV0jann4P2rvDh', [1998, 2003, 2006, 2013, 2016], 0.5),
}

ID_IRR = {

    'ID_1986': ('ft:1rAO90xDcSyR1GTKjAN4Z12vf2mVy8iKRr7vorhLr', [1986], 0.5),
    'ID_1996': ('ft:1Injcz-Q3HgQ_gip9ZEMqUAmihqbjTOEYHThuoGmL', [1996], 0.5),
    'ID_2002': ('ft:14pePO5Wr7Hcbz_VHuUYd_f5ReblXtvUFS3BrCpI2', [2002], 0.5),
    'ID_2006': ('ft:1NM9NsQJfdNAEwmZXyo5o78ha4PhgsErWzfttfZM1', [2006], 0.5),
    'ID_2008': ('ft:1VK5sWEgD35fz4pNNbg9sy6nlBD_lIl_t-ELyWbC9', [2008], 0.5),
    'ID_2009': ('ft:1RtW_lu3hFcpzZ_UUT_xPUsHarAZoenV4AibeFeBz', [2009], 0.5),
    'ID_2010': ('ft:1BSxEsy_oDUnWsWsQYJFRPaEvKsF-H_bDNE_gpBS7', [2010], 0.5),
    'ID_2011': ('ft:1NxN6aOViiJBklaUEEeGJJo6Kpy-QB10f_yGWOUyC', [2011], 0.5),
}

CO_IRR = {
    'CO_Div2': ('ft:1wRNCuexIGBwIH7gc6ZTx3Ia68aNYolgVfsxKeDuh', [1998, 2003, 2006, 2013, 2016], 0.5),
    'CO_Div3': ('ft:1Tv8Nei94QP1421iD-CkkZNoOXG9G8rgyh6zrW0JN', [1998, 2003, 2006, 2013, 2016], 0.5),
    'CO_Div4': ('ft:1W5zQHQR6oiiK556LuEONO2fPRKnrA9fySoWwD_fz', [1998, 2003, 2006, 2013, 2016], 0.5),
    'CO_Div5': ('ft:1Sj6gJOfwjfCV9sYyninX-fXdzzwE4yNC-Qxb3t-n', [1998, 2003, 2006, 2013, 2016], 0.5),
    'CO_Div6': ('ft:1BnJJuow6rgOOTZOimCeu4PbHaraY7fEjfvv-BzgP', [1998, 2003, 2006, 2013, 2016], 0.5),
    'CO_Div7': ('ft:1E1mD5M6gnpMMvEtUF4wtiG4EeeeAeqw9rmZTaMn4', [1998, 2003, 2006, 2013, 2016], 0.5),
    'CO_Repu': ('ft:133QsXytF1R6k3SDwGwTPcv3KBz6Eb9r-dB3EoxwI', [1998, 2003, 2006, 2013, 2016], 0.5),
}

YEARS = [1986, 1987, 1988, 1989, 1993, 1994, 1995, 1996, 1997,
         1998, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
         2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

TEST_YEARS = [2014, 2015, 2016]
ALL_YEARS = [x for x in range(1986, 2017)]


def reduce_regions(tables, years=None, description=None, cdl_mask=False, min_years=0):
    sum_mask = None
    image_list = list_assets('users/dgketchum/classy')
    fc = ee.FeatureCollection(tables)

    if min_years > 0:
        coll = ee.ImageCollection(image_list)
        sum = ee.ImageCollection(coll.mosaic().select('classification').remap([0, 1, 2, 3], [1, 0, 0, 0])).sum()
        sum_mask = sum.lt(min_years)

    first = True
    for yr in years:
        yr_img = [x for x in image_list if x.endswith(str(yr))]
        coll = ee.ImageCollection(yr_img)
        tot = coll.mosaic().select('classification').remap([0, 1, 2, 3], [1, 0, 0, 0])

        if cdl_mask and min_years > 0:
            # cultivated/uncultivated band only available 2013 to 2017
            cdl = ee.Image('USDA/NASS/CDL/2013')
            cultivated = cdl.select('cultivated')
            cdl_crop_mask = cultivated.eq(2)
            tot = tot.mask(cdl_crop_mask).mask(sum_mask)

        elif min_years > 0:
            tot = tot.mask(sum_mask)

        elif cdl_mask:
            cdl = ee.Image('USDA/NASS/CDL/2013')
            cultivated = cdl.select('cultivated')
            cdl_crop_mask = cultivated.eq(2)
            tot = tot.mask(cdl_crop_mask)

        tot = tot.multiply(ee.Image.pixelArea())
        reduce = tot.reduceRegions(collection=fc,
                                   reducer=ee.Reducer.sum(),
                                   scale=30)
        task = ee.batch.Export.table.toCloudStorage(
            reduce,
            description='{}_area_{}_'.format(description, yr),
            bucket='wudr',
            fileNamePrefix='{}_area_{}_'.format(description, yr),
            fileFormat='CSV')
        task.start()

        if first:
            tot = coll.mosaic().select('classification').remap([0, 1, 2, 3], [1, 1, 1, 1])
            tot = tot.multiply(ee.Image.pixelArea())
            reduce = tot.reduceRegions(collection=fc,
                                       reducer=ee.Reducer.sum(),
                                       scale=30)
            task = ee.batch.Export.table.toCloudStorage(
                reduce,
                description='{}_total_area_'.format(description),
                bucket='wudr',
                fileNamePrefix='{}_total_area_'.format(description),
                fileFormat='CSV')
            task.start()
            first = False

        print(yr)


def attribute_irrigation():

    fc = ee.FeatureCollection(IRRIGATION_TABLE)
    for state in TARGET_STATES:
        for yr in range(1986, 2017):
            images = os.path.join(ASSET_ROOT, '{}_{}'.format(state, yr))
            coll = ee.Image(images)
            tot = coll.select('classification').remap([0, 1, 2, 3], [1, 0, 0, 0])
            means = tot.reduceRegions(collection=fc,
                                      reducer=ee.Reducer.mean(),
                                      scale=30)

            task = ee.batch.Export.table.toCloudStorage(
                means,
                description='{}_{}'.format(state, yr),
                bucket='wudr',
                fileNamePrefix='attr_{}_{}'.format(state, yr),
                fileFormat='CSV')

            print(state, yr)
            task.start()


def export_classification(out_name, asset, export='asset'):
    fc = ee.FeatureCollection(TABLE_V2)
    roi = ee.FeatureCollection(asset)
    mask = roi.geometry().bounds().getInfo()['coordinates']

    classifier = ee.Classifier.randomForest(
        outOfBagMode=False).setOutputMode('CLASSIFICATION')

    input_props = fc.first().propertyNames().remove('YEAR').remove('POINT_TYPE').remove('system:index')
    feature_bands = sorted([b for b in fc.first().getInfo()['properties']])
    feature_bands.remove('POINT_TYPE')
    feature_bands.remove('YEAR')

    trained_model = classifier.train(fc, 'POINT_TYPE', input_props)

    for yr in TEST_YEARS:

        input_bands = stack_bands(yr, roi)
        annual_stack = input_bands.select(input_props)
        classified_img = annual_stack.classify(trained_model).int()

        if export == 'asset':
            task = ee.batch.Export.image.toAsset(
                image=classified_img,
                description='{}_{}'.format(out_name, yr),
                assetId=os.path.join(ASSET_ROOT, '{}_{}'.format(out_name, yr)),
                fileNamePrefix='{}_{}'.format(yr, out_name),
                region=mask,
                scale=30,
                maxPixels=1e10)
        elif export == 'cloud':
            task = ee.batch.Export.image.toCloudStorage(
                image=classified_img,
                description='{}_{}'.format(out_name, yr),
                bucket='wudr',
                fileNamePrefix='{}_{}'.format(yr, out_name),
                region=mask,
                scale=30,
                maxPixels=1e10)
        else:
            raise NotImplementedError('choose asset or cloud for export')

        task.start()
        print(yr)


def filter_irrigated():
    for k, v in IRR.items():
        plots = ee.FeatureCollection(v[0])

        for year in v[1]:
            # pprint(plots.first().getInfo())
            start = '{}-01-01'.format(year)

            early_summer_s = ee.Date(start).advance(5, 'month')
            early_summer_e = ee.Date(start).advance(7, 'month')
            late_summer_s = ee.Date(start).advance(7, 'month')
            late_summer_e = ee.Date(start).advance(10, 'month')

            if year <= 2011:
                collection = ndvi5()
            elif year == 2012:
                collection = ndvi7()
            else:
                collection = ndvi8()

            early_collection = period_stat(collection, early_summer_s, early_summer_e)
            late_collection = period_stat(collection, late_summer_s, late_summer_e)

            early_nd_max = early_collection.select('nd_mean').reduce(ee.Reducer.intervalMean(0.0, 15.0))
            early_int_mean = early_nd_max.reduceRegions(collection=plots,
                                                        reducer=ee.Reducer.mean(),
                                                        scale=30.0)

            s_nd_max = late_collection.select('nd_mean').reduce(ee.Reducer.intervalMean(0.0, 15.0))
            combo_mean = s_nd_max.reduceRegions(collection=early_int_mean,
                                                reducer=ee.Reducer.mean(),
                                                scale=30.0)

            filt_fc = combo_mean.filter(ee.Filter.Or(ee.Filter.gt('mean', v[2]), ee.Filter.gt('mean', v[2])))

            task = ee.batch.Export.table.toCloudStorage(filt_fc,
                                                        folder='Irrigation',
                                                        description='{}_{}'.format(k, year),
                                                        bucket='wudr',
                                                        fileNamePrefix='{}_{}'.format(k, year),
                                                        fileFormat='KML')

            task.start()


def request_validation_extract(file_prefix='validation'):

    roi = ee.FeatureCollection(ROI)
    plots = ee.FeatureCollection(VALIDATION_POINTS).filterBounds(roi)
    image_list = list_assets('users/dgketchum/classy')

    for yr in YEARS:
        yr_img = [x for x in image_list if x.endswith(str(yr))]
        coll = ee.ImageCollection(yr_img)
        classified = coll.mosaic().select('classification')

        start = '{}-01-01'.format(yr)
        d = datetime.strptime(start, '%Y-%m-%d')
        epoch = datetime.utcfromtimestamp(0)
        start_millisec = (d - epoch).total_seconds() * 1000
        filtered = plots.filter(ee.Filter.eq('YEAR', ee.Number(start_millisec)))

        plot_sample_regions = classified.sampleRegions(
            collection=filtered,
            properties=['POINT_TYPE', 'YEAR'],
            scale=30,
            tileScale=16)

        task = ee.batch.Export.table.toCloudStorage(
            plot_sample_regions,
            description='{}_{}'.format(file_prefix, yr),
            bucket='wudr',
            fileNamePrefix='{}_{}'.format(file_prefix, yr),
            fileFormat='CSV')

        task.start()
        print(yr)


def request_band_extract(file_prefix, filter_bounds=False):
    roi = ee.FeatureCollection(ROI)
    plots = ee.FeatureCollection(POINTS)
    for yr in TEST_YEARS:
        stack = stack_bands(yr, roi)
        start = '{}-01-01'.format(yr)
        d = datetime.strptime(start, '%Y-%m-%d')
        epoch = datetime.utcfromtimestamp(0)
        start_millisec = (d - epoch).total_seconds() * 1000

        if filter_bounds:
            plots = plots.filterBounds(roi)

        filtered = plots.filter(ee.Filter.eq('YEAR', ee.Number(start_millisec)))

        proj = stack.select('B2').projection().getInfo()['crs']

        plot_sample_regions = stack.sampleRegions(
            collection=filtered,
            properties=['POINT_TYPE', 'YEAR'],
            scale=30,
            tileScale=2)

        task = ee.batch.Export.table.toCloudStorage(
            plot_sample_regions,
            description='{}_{}'.format(file_prefix, yr),
            bucket='wudr',
            fileNamePrefix='{}_{}'.format(file_prefix, yr),
            fileFormat='CSV')

        task.start()
        print(yr)


def get_ndvi_series(years, roi):

    ndvi_l5, ndvi_l7, ndvi_l8 = ndvi5(), ndvi7(), ndvi8()
    ndvi = ee.ImageCollection(ndvi_l5.merge(ndvi_l7).merge(ndvi_l8)).filterBounds(roi)

    def ndvi_means(date):
        etc = ndvi.filterDate(ee.Date(date).advance(4, 'month'),
                              ee.Date(date).advance(9, 'month')).toBands()
        stats = ee.Image(etc.reduce(ee.Reducer.mean()).rename('nd_mean_{}'.format(date[:4])))
        return stats

    bands_list = []
    for yr, s in zip(years, [1, 2, 3, 4, 5]):
        d = '{}-01-01'.format(yr)
        bands = ndvi_means(d)
        bands_list.append(bands.rename('nd_mean_{}'.format(s)))

    i = ee.Image(bands_list)
    return i


def add_doy(image):
    mask = ee.Date(image.get('system:time_start'))
    day = ee.Image.constant(image.date().getRelative('day', 'year')).clip(image.geometry())
    i = image.addBands(day.rename('DOY')).int().updateMask(mask)
    return i


def stack_bands(yr, roi):

    start = '{}-01-01'.format(yr)
    end_date = '{}-01-01'.format(yr + 1)
    water_year_start = '{}-10-01'.format(yr - 1)

    spring_s, spring_e = '{}-03-01'.format(yr), '{}-05-01'.format(yr),
    late_spring_s, late_spring_e = '{}-05-01'.format(yr), '{}-07-01'.format(yr)
    summer_s, summer_e = '{}-07-01'.format(yr), '{}-09-01'.format(yr)
    fall_s, fall_e = '{}-09-01'.format(yr), '{}-11-01'.format(yr)

    l5_coll = ee.ImageCollection('LANDSAT/LT05/C01/T1_SR').filterBounds(
        roi).filterDate(start, end_date).map(ls5_edge_removal).map(ls57mask)
    l7_coll = ee.ImageCollection('LANDSAT/LE07/C01/T1_SR').filterBounds(
        roi).filterDate(start, end_date).map(ls57mask)
    l8_coll = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR').filterBounds(
        roi).filterDate(start, end_date).map(ls8mask)

    lsSR_masked = ee.ImageCollection(l7_coll.merge(l8_coll).merge(l5_coll))
    lsSR_spr_mn = ee.Image(lsSR_masked.filterDate(spring_s, summer_s).mean())
    lsSR_lspr_mn = ee.Image(lsSR_masked.filterDate(late_spring_s, late_spring_e).mean())
    lsSR_sum_mn = ee.Image(lsSR_masked.filterDate(summer_s, fall_s).mean())
    lsSR_fal_mn = ee.Image(lsSR_masked.filterDate(fall_s, end_date).mean())

    proj = lsSR_sum_mn.select('B2').projection().getInfo()
    input_bands = lsSR_spr_mn.addBands([lsSR_lspr_mn, lsSR_sum_mn, lsSR_fal_mn])

    nd_list_ = []
    for pos, year in zip(['m2', 'm1', 'cy', 'p1', 'p2'], range(yr - 2, yr + 3)):
        if year <= 2011:
            collection = ndvi5()
        elif year == 2012:
            collection = ndvi7()
        else:
            collection = ndvi8()

        nd_collection = period_stat(collection, spring_s.replace('{}'.format(yr), '{}'.format(year)),
                                    fall_e.replace('{}'.format(yr), '{}'.format(year)))
        s_nd_max = nd_collection.select('nd_max').rename('nd_max_{}'.format(pos))
        nd_list_.append(s_nd_max)

    input_bands = input_bands.addBands(nd_list_)

    for s, e, n in [(spring_s, spring_e, 'espr'),
                    (late_spring_s, late_spring_e, 'lspr'),
                    (summer_s, summer_e, 'smr'),
                    (fall_s, fall_e, 'fl'),
                    (water_year_start, spring_e, 'wy_espr'),
                    (water_year_start, late_spring_e, 'wy_espr'),
                    (water_year_start, summer_e, 'wy_smr'),
                    (water_year_start, fall_e, 'wy')]:
        gridmet = ee.ImageCollection("IDAHO_EPSCOR/GRIDMET").filterBounds(
            roi).filterDate(s, e).select('pr', 'eto', 'tmmn', 'tmmx')
        temp_reducer = ee.Reducer.mean()
        t_names = ['tmax'.format(n), 'tmin'.format(n)]
        temp_perc = gridmet.select('tmmn', 'tmmx').reduce(temp_reducer).rename(t_names).resample(
            'bilinear').reproject(crs=proj['crs'], scale=30)

        precip_reducer = ee.Reducer.sum()
        precip_sum = gridmet.select('pr', 'eto').reduce(precip_reducer).rename(
            'precip_total_{}'.format(n), 'pet_total_{}'.format(n)).resample('bilinear').reproject(crs=proj['crs'],
                                                                                                  scale=30)
        wd_estimate = precip_sum.select('precip_total_{}'.format(n)).subtract(precip_sum.select(
            'pet_total_{}'.format(n))).rename('wd_est_{}'.format(n))
        input_bands = input_bands.addBands([temp_perc, precip_sum, wd_estimate])

    coords = ee.Image.pixelLonLat().rename(['Lon_GCS', 'LAT_GCS']).resample('bilinear').reproject(crs=proj['crs'],
                                                                                                  scale=30)
    ned = ee.Image('USGS/NED')
    terrain = ee.Terrain.products(ned).select('elevation', 'slope', 'aspect').reduceResolution(
        ee.Reducer.mean()).reproject(crs=proj['crs'], scale=30)

    world_climate = get_world_climate(proj=proj)
    elev = terrain.select('elevation')
    tpi_1250 = elev.subtract(elev.focal_mean(1250, 'circle', 'meters')).add(0.5).rename('tpi_1250')
    tpi_250 = elev.subtract(elev.focal_mean(250, 'circle', 'meters')).add(0.5).rename('tpi_250')
    tpi_150 = elev.subtract(elev.focal_mean(150, 'circle', 'meters')).add(0.5).rename('tpi_150')
    static_input_bands = coords.addBands([terrain, tpi_1250, tpi_250, tpi_150, world_climate])

    nlcd = ee.Image('USGS/NLCD/NLCD2011').select('landcover').reproject(crs=proj['crs'], scale=30).rename('nlcd')
    cdl = ee.Image('USDA/NASS/CDL/2017').select('cultivated').remap([1, 2], [0, 1]).reproject(crs=proj['crs'],
                                                                                              scale=30).rename('cdl')
    static_input_bands = static_input_bands.addBands([nlcd, cdl])

    input_bands = input_bands.addBands(static_input_bands).clip(roi)

    # standardize names to match EE javascript output
    standard_names = []
    temp_ct = 1
    prec_ct = 1
    names = input_bands.bandNames().getInfo()
    for name in names:
        if 'B' in name and '_1_1' in name:
            replace_ = name.replace('_1_1', '_2')
            standard_names.append(replace_)
        elif 'B' in name and '_2' in name:
            replace_ = name.replace('_2', '_3')
            standard_names.append(replace_)
        elif 'tavg' in name and 'tavg' in standard_names:
            standard_names.append('tavg_{}'.format(temp_ct))
            temp_ct += 1
        elif 'prec' in name and 'prec' in standard_names:
            standard_names.append('prec_{}'.format(prec_ct))
            prec_ct += 1
        else:
            standard_names.append(name)

    input_bands = input_bands.rename(standard_names)
    return input_bands


def get_world_climate(proj):
    n = list(range(4, 10))
    months = [str(x).zfill(2) for x in n]
    parameters = ['tavg', 'prec']
    combinations = [(m, p) for m in months for p in parameters]
    l = [ee.Image('WORLDCLIM/V1/MONTHLY/{}'.format(m)).select(p).resample('bilinear').reproject(crs=proj['crs'],
                                                                                                scale=30) for m, p in
         combinations]
    i = ee.Image(l)
    return i


def get_qa_bits(image, start, end, qa_mask):
    pattern = 0
    for i in range(start, end - 1):
        pattern += 2 ** i
    return image.select([0], [qa_mask]).bitwiseAnd(pattern).rightShift(start)


def mask_quality(image):
    QA = image.select('pixel_qa')
    shadow = get_qa_bits(QA, 3, 3, 'cloud_shadow')
    cloud = get_qa_bits(QA, 5, 5, 'cloud')
    cirrus_detected = get_qa_bits(QA, 9, 9, 'cirrus_detected')
    return image.updateMask(shadow.eq(0)).updateMask(cloud.eq(0).updateMask(cirrus_detected.eq(0)))


def ls57mask(img):
    sr_bands = img.select('B1', 'B2', 'B3', 'B4', 'B5', 'B7')
    mask_sat = sr_bands.neq(20000)
    img_nsat = sr_bands.updateMask(mask_sat)
    mask1 = img.select('pixel_qa').bitwiseAnd(8).eq(0)
    mask2 = img.select('pixel_qa').bitwiseAnd(32).eq(0)
    mask_p = mask1.And(mask2)
    img_masked = img_nsat.updateMask(mask_p)
    mask_sel = img_masked.select(['B1', 'B2', 'B3', 'B4', 'B5', 'B7'], ['B2', 'B3', 'B4', 'B5', 'B6', 'B7'])
    mask_mult = mask_sel.multiply(0.0001).copyProperties(img, ['system:time_start'])
    return mask_mult


def ls8mask(img):
    sr_bands = img.select('B2', 'B3', 'B4', 'B5', 'B6', 'B7')
    mask_sat = sr_bands.neq(20000)
    img_nsat = sr_bands.updateMask(mask_sat)
    mask1 = img.select('pixel_qa').bitwiseAnd(8).eq(0)
    mask2 = img.select('pixel_qa').bitwiseAnd(32).eq(0)
    mask_p = mask1.And(mask2)
    img_masked = img_nsat.updateMask(mask_p)
    mask_mult = img_masked.multiply(0.0001).copyProperties(img, ['system:time_start'])
    return mask_mult


def ndvi5():
    l = ee.ImageCollection('LANDSAT/LT05/C01/T1_SR').map(lambda x: x.select().addBands(
        x.normalizedDifference(['B4', 'B3'])))
    return l


def ndvi7():
    l = ee.ImageCollection('LANDSAT/LE07/C01/T1_SR').map(lambda x: x.select().addBands(
        x.normalizedDifference(['B4', 'B3'])))
    return l


def ndvi8():
    l = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR').map(lambda x: x.select().addBands(
        x.normalizedDifference(['B5', 'B4'])))
    return l


def ls5_edge_removal(lsImage):
    inner_buffer = lsImage.geometry().buffer(-3000)
    buffer = lsImage.clip(inner_buffer)
    return buffer


def period_stat(collection, start, end):
    c = collection.filterDate(start, end)
    return c.reduce(
        ee.Reducer.mean().combine(reducer2=ee.Reducer.minMax(),
                                  sharedInputs=True))


def is_authorized():
    try:
        ee.Initialize()
        print('Authorized')
        return True
    except Exception as e:
        print('You are not authorized: {}'.format(e))
        return False


if __name__ == '__main__':
    is_authorized()
    # request_band_extract('bands_26MAR', filter_bounds=False)
    filter_irrigated()
    # for state in TARGET_STATES:
    #     print(state)
    #     bounds = os.path.join(BOUNDARIES, state)
    #     export_classification(out_name='{}'.format(state), asset=bounds, export='asset')
    # attribute_irrigation()
    # request_validation_extract()
# ========================= EOF ====================================================================
