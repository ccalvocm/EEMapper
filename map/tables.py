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
# ===============================================================================

import json
import os
from datetime import datetime

from geopandas import GeoDataFrame, read_file
from numpy import where, sum, nan, std, array, min, max, mean
from pandas import read_csv, concat, errors, Series, DataFrame
from pandas import to_datetime
from pandas.io.json import json_normalize
from shapely.geometry import Polygon
from sklearn.metrics import confusion_matrix
from map.models import producer, consumer

INT_COLS = ['POINT_TYPE', 'YEAR']

KML_DROP = ['system:index', 'altitudeMo', 'descriptio',
            'extrude', 'gnis_id', 'icon', 'loaddate',
            'metasource', 'name_1', 'shape_area', 'shape_leng', 'sourcedata',
            'sourcefeat', 'sourceorig', 'system_ind', 'tessellate',
            'tnmid', 'visibility', ]

DUPLICATE_HUC8_NAMES = ['Beaver', 'Big Sandy', 'Blackfoot', 'Carrizo', 'Cedar', 'Clear', 'Colorado Headwaters', 'Crow',
                        'Frenchman', 'Horse', 'Jordan', 'Lower Beaver', 'Lower White', 'Medicine', 'Muddy', 'Palo Duro',
                        'Pawnee', 'Redwater', 'Rock', 'Salt', 'San Francisco', 'Santa Maria', 'Silver', 'Smith',
                        'Stillwater', 'Teton', 'Upper Bear', 'Upper White', 'White', 'Willow']

COLS = ['SCENE_ID',
        'PRODUCT_ID',
        'SPACECRAFT_ID',
        'SENSOR_ID',
        'DATE_ACQUIRED',
        'COLLECTION_NUMBER',
        'COLLECTION_CATEGORY',
        'SENSING_TIME',
        'DATA_TYPE',
        'WRS_PATH',
        'WRS_ROW',
        'CLOUD_COVER',
        'NORTH_LAT',
        'SOUTH_LAT',
        'WEST_LON',
        'EAST_LON',
        'TOTAL_SIZE',
        'BASE_URL']


def concatenate_county_data(folder, glob='counties'):
    df = None
    base_names = [x for x in os.listdir(folder)]
    _files = [os.path.join(folder, x) for x in base_names if x.startswith(glob) and not 'total_area' in x]
    totals_file = [os.path.join(folder, x) for x in base_names if 'total_area' in x][0]
    first = True

    for csv in _files:

        print(csv)
        if first:
            df = read_csv(totals_file).sort_values('COUNTYNS')
            df['total_area'] = df['sum']
            df.drop(columns=['sum'], inplace=True)
            first = False

        comps = os.path.basename(csv).split('_')
        for c in comps:
            try:
                year = int(c)
            except ValueError:
                pass

        c = read_csv(csv).sort_values('COUNTYNS')['sum']
        c.name = '{}_{}'.format(comps[1], year)
        df = concat([df, c], sort=False, axis=1)
        print(c.shape, csv)

    out_file = os.path.join(folder, 'irr_merged.csv'.format(glob))

    print('size: {}'.format(df.shape))
    df.to_csv(out_file, index=False)


def concatenate_band_extract(root, out_dir, glob='None', sample=None):
    l = [os.path.join(root, x) for x in os.listdir(root) if glob in x]
    l.sort()
    first = True
    for csv in l:
        try:
            if first:
                df = read_csv(csv)
                cols = list(df.columns)
                names = [x for x in list(df.columns) if 'nd_max' in x]
                idx = [list(df.columns).index(x) for x in names]
                new_names = ['nd_max_{}'.format(x) for x in ['m2', 'm1', 'cy', 'p1', 'p2']]
                cols[idx[0]: idx[-1] + 1] = new_names
                df.columns = cols
                print(df.shape, csv)
                first = False
            else:
                c = read_csv(csv)
                cols = list(c.columns)
                names = [x for x in list(c.columns) if 'nd_max' in x]
                idx = [list(c.columns).index(x) for x in names]
                new_names = ['nd_max_{}'.format(x) for x in ['m2', 'm1', 'cy', 'p1', 'p2']]
                cols[idx[0]: idx[-1] + 1] = new_names
                c.columns = cols
                df = concat([df, c], sort=False)
                print(c.shape, csv)
        except errors.EmptyDataError:
            print('{} is empty'.format(csv))
            pass

    df.drop(columns=['system:index', '.geo'], inplace=True)

    if sample:
        _len = int(df.shape[0]/1e3 * sample)
        out_file = os.path.join(out_dir, '{}_{}.csv'.format(glob, _len))
    else:
        out_file = os.path.join(out_dir, '{}.csv'.format(glob))

    for c in df.columns:
        if c in INT_COLS:
            df[c] = df[c].astype(int, copy=True)
        else:
            df[c] = df[c].astype(float, copy=True)
    if sample:
        df = df.sample(frac=sample).reset_index(drop=True)

    print('size: {}'.format(df.shape))
    df.to_csv(out_file, index=False)


def concatenate_irrigation_attrs(_dir, out_filename):
    _files = [os.path.join(_dir, x) for x in os.listdir(_dir) if x.endswith('.csv')]
    _files.sort()
    first_year = True
    for year in range(1986, 2017):
        yr_files = [f for f in _files if str(year) in f]
        first_state = True
        for f in yr_files:
            if first_state:
                df = read_csv(f, index_col=0)
                df.dropna(subset=['mean'], inplace=True)
                df.rename(columns={'mean': 'IPct_{}'.format(year)}, inplace=True)
                df.drop_duplicates(subset=['.geo'], keep='first', inplace=True)
                df['Irr_{}'.format(year)] = where(df['IPct_{}'.format(year)].values > 0.5, 1, 0)
                first_state = False
            else:
                c = read_csv(f, index_col=0)
                c.dropna(subset=['mean'], inplace=True)
                c.rename(columns={'mean': 'IPct_{}'.format(year)}, inplace=True)
                c['Irr_{}'.format(year)] = where(c['IPct_{}'.format(year)].values > 0.5, 1, 0)
                df = concat([df, c], sort=False)
                df.drop_duplicates(subset=['.geo'], keep='first', inplace=True)

        print(year, df.shape)
        if first_year:
            master = df
            first_year = False
        else:
            master['IPct_{}'.format(year)] = df['IPct_{}'.format(year)]
            master['Irr_{}'.format(year)] = df['Irr_{}'.format(year)]

    bool_cols = array([master[x].values for x in master.columns if 'Irr_' in x])
    bool_sum = sum(bool_cols, axis=0)
    master['IYears'] = bool_sum
    master.dropna(subset=['.geo'], inplace=True)
    coords = Series(json_normalize(master['.geo'].apply(json.loads))['coordinates'].values,
                    index=master.index)
    master['geometry'] = coords.apply(to_polygon)
    master.dropna(subset=['geometry'], inplace=True)
    gpd = GeoDataFrame(master.drop(['.geo'], axis=1),
                       crs={'init': 'epsg:4326'})
    gpd.to_file(out_filename)


def concatenate_attrs(_dir, out_csv_filename, out_shp_filename, template_geometry):

    _files = [os.path.join(_dir, x) for x in os.listdir(_dir) if x.endswith('.csv')]
    _files.sort()
    first = True
    df_geo = []
    template_names = []
    count_arr = None
    names = None

    for year in range(1986, 2017):
        print(year)
        yr_files = [f for f in _files if str(year) in f]
        _mean = [f for f in yr_files if 'mean' in f][0]

        if first:
            df = read_csv(_mean, index_col=['huc8']).sort_values('huc8', axis=0)
            names = df['Name']
            units = df.index
            template_gpd = read_file(template_geometry).sort_values('huc8', axis=0)
            for i, r in template_gpd.iterrows():

                if r['Name'] in DUPLICATE_HUC8_NAMES:
                    df_geo.append(r['geometry'])
                    template_names.append('{}_{}'.format(r['Name'], str(r['states']).replace(',', '_')))
                elif r['Name'] in names.values and r['Name'] not in template_names:
                    df_geo.append(r['geometry'])
                    template_names.append(r['Name'])
                else:
                    print('{} is in the list'.format(r['Name']))

            mean_arr = df['mean']
            df.drop(columns=KML_DROP, inplace=True)
            df.drop(columns=['.geo', 'mean'], inplace=True)
            _count_csv = [f for f in yr_files if 'count' in f][0]
            count_arr = read_csv(_count_csv, index_col=0)['count'].values
            df['TotalPix'.format(year)] = count_arr
            df['Ct_{}'.format(year)] = mean_arr * count_arr
            first = False

        else:
            mean_arr = read_csv(_mean, index_col=['huc8']).sort_values('huc8', axis=0)['mean'].values
            df['Ct_{}'.format(year)] = mean_arr * count_arr

    year_cts = [x for x in df.columns if 'Ct_' in x]
    cts = df.drop(columns=[x for x in df.columns if x not in year_cts])

    arr = cts.values
    max_pct = (max(arr, axis=1) / df['TotalPix'].values).reshape(arr.shape[0], 1)
    df['max_pct'] = max_pct

    min_pct = (min(arr, axis=1) / df['TotalPix'].values).reshape(arr.shape[0], 1)
    df['min_pct'] = min_pct

    mean_pct = (mean(arr, axis=1) / df['TotalPix'].values).reshape(arr.shape[0], 1)
    df['mean_pct'] = mean_pct

    diff = (max_pct - min_pct) / mean_pct
    df['diff_pct'] = diff

    std_ = std(arr, axis=1).reshape(arr.shape[0], 1)
    df['std_dev'] = std_

    df.drop(columns=['Name'], inplace=True)
    df['Name'] = names
    df['geometry'] = df_geo
    df['huc8'] = units
    df.to_csv(out_csv_filename)
    gpd = GeoDataFrame(df, crs={'init': 'epsg:4326'}, geometry=df_geo)
    gpd.to_file(out_shp_filename)


def add_stats_to_shapefile(shp, out_shp):
    gdf = read_file(shp).sort_values('huc8', axis=0)
    geometry = gdf['geometry']
    gdf.drop(columns=['geometry'], inplace=True)
    df = DataFrame(gdf)
    new_cols = [x.replace('Ct_', '') if 'Ct_' in x else x for x in df.columns]
    df.columns = new_cols
    e, l = [str(x) for x in range(1986, 1991)], [str(x) for x in range(2012, 2017)]
    early = df[e].mean(axis=1)
    late = df[l].mean(axis=1)
    tot_pix = df['TotalPix']
    df['delta'] = (early - late) / tot_pix.values
    gpd = GeoDataFrame(df, crs={'init': 'epsg:4326'}, geometry=geometry)
    gpd.to_file(out_shp)


def to_polygon(j):
    if not isinstance(j, list):
        return nan
    try:
        return Polygon(j[0])
    except ValueError:
        return nan
    except TypeError:
        return nan
    except AssertionError:
        return nan


def count_landsat_scenes(index, shp):
    pr_list = [str(x) for x in read_file(shp)['PR'].values]
    first = True
    l8, l7, l5 = 0, 0, 0
    with open(index) as f:
        for line in f:
            if first:
                # skip header line
                first = False
            else:
                l = line.split(',')
                sat = l[2]
                pr = l[9].zfill(2) + l[10].zfill(3)
                dt = to_datetime(l[7]).to_pydatetime()
                doy = int(dt.strftime('%j'))
                start, end = datetime(1986, 1, 1), datetime(2016, 12, 31)
                if pr in pr_list and start < dt < end and 59 < doy < 365:
                    if sat == 'LANDSAT_8':
                        l8 += 1
                    elif sat == 'LANDSAT_7':
                        l7 += 1
                    elif sat == 'LANDSAT_5':
                        l5 += 1
        print('{} l8, {} l7, {} l5'.format(l8, l7, l5))


def get_confusion(_dir):
    _list = [os.path.join(_dir, x) for x in os.listdir(_dir)]
    _list.sort()
    first = True
    for csv in _list:
        try:
            if first:
                df = read_csv(csv)
                first = False
            else:
                c = read_csv(csv)
                df = concat([df, c], sort=False)
        except errors.EmptyDataError:
            print('{} is empty'.format(csv))
            pass

    df.drop(columns=['system:index', '.geo'], inplace=True)

    y_true, y_pred = df['POINT_TYPE'].values, df['classification'].values
    cf = confusion_matrix(y_true, y_pred)
    print(cf)
    consumer(cf)
    producer(cf)


if __name__ == '__main__':
    home = os.path.expanduser('~')
    huc_lev = 8
    # attrs = os.path.join(home, 'IrrigationGIS', 'attr_irr')
    # or_csv = os.path.join(attrs, 'csv', 'harney')
    # out = os.path.join(attrs, 'shp', 'Harney_IrrAttrs.shp')
    # concatenate_irrigation_attrs(or_csv, out)

    # val = os.path.join(home, 'IrrigationGIS', 'validation_tables')
    # get_confusion(val)

    extracts = os.path.join(home, 'IrrigationGIS', 'time_series', 'exports_huc{}'.format(huc_lev))
    tables = os.path.join(home, 'IrrigationGIS', 'time_series', 'tables')
    shapes = os.path.join(home, 'IrrigationGIS', 'time_series', 'shapefiles')

    out_table = os.path.join(tables, 'concatenated_huc{}.csv'.format(huc_lev))
    out_shape = os.path.join(shapes, 'time_series_15MAR19.shp')
    template = os.path.join(home, 'IrrigationGIS', 'hydrography', 'huc{}_semiarid_clip.shp'.format(huc_lev))
    #
    # concatenate_attrs(extracts, out_table, out_shape, template_geometry=template)
    # in_shape = os.path.join(shapes, 'time_series_15MAR19.shp')
    # out_shp = in_shape.replace('time_series_', 'add_stats_')
    # add_stats_to_shapefile(in_shape, out_shp)
    tables = os.path.join(home, 'IrrigationGIS', 'time_series', 'exports_county')
    concatenate_county_data(tables, glob='counties_')

    # d = os.path.join(home, 'IrrigationGIS', 'EE_extracts', 'to_concatenate')
    # r = os.path.join(home, 'IrrigationGIS', 'EE_extracts', 'concatenated')

    # concatenate_band_extract(d, r, glob='bands_26MAR_')
# ========================= EOF ====================================================================
