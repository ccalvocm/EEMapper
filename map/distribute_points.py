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

import os

import fiona
from numpy import linspace, max, ceil
from numpy.random import shuffle
from pandas import DataFrame
from pyproj import Proj
from shapely.geometry import shape, Point, mapping

training = os.path.join(os.path.expanduser('~'), 'IrrigationGIS', 'training_raw')
WETLAND = os.path.join(training, 'wetlands', 'wetlands_sample_wgs84.shp')
UNCULTIVATED = os.path.join(training, 'uncultivated', 'uncultivated.shp')
IRRIGATED = os.path.join(training, 'irrigated', 'merged_attributed', 'irr_merge.shp')
UNIRRIGATED = os.path.join(training, 'unirrigated', 'unirrigated.shp')

YEARS = [
    1986,
    1988,
    1996,
    1998,
    1999,
    2000,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
]


class PointsRunspec(object):

    def __init__(self, root, **kwargs):
        self.root = root
        self.features = []
        self.object_id = 0
        self.year = None
        self.aea = Proj(
            '+proj=aea +lat_1=20 +lat_2=60 +lat_0=40 +lon_0=-96'
            ' +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs')
        self.wgs = Proj('+init=EPSG:4326')
        self.meta = None
        self.extracted_points = DataFrame(columns=['FID', 'X', 'Y', 'POINT_TYPE', 'YEAR'])

        self.irr_path = IRRIGATED
        self.unirr_path = UNIRRIGATED
        self.uncult_path = UNCULTIVATED
        self.wetland_path = WETLAND

        if 'irrigated' in kwargs.keys():
            self.irrigated(kwargs['irrigated'])
        if 'unirrigated' in kwargs.keys():
            self.unirrigated(kwargs['unirrigated'])
        if 'wetlands' in kwargs.keys():
            self.wetlands(kwargs['wetlands'])
        if 'uncultivated' in kwargs.keys():
            self.uncultivated(kwargs['uncultivated'])

    def wetlands(self, n):
        print('wetlands: {}'.format(n))
        n /= len(YEARS)
        n = int(n)
        for yr in YEARS:
            self.year = yr
            self.create_sample_points(n, self.wetland_path, code=3)

    def uncultivated(self, n):
        print('uncultivated: {}'.format(n))
        n /= len(YEARS)
        for yr in YEARS:
            self.year = yr
            self.create_sample_points(n, self.uncult_path, code=2)

    def unirrigated(self, n):
        print('unirrigated: {}'.format(n))
        n /= len(YEARS)
        for yr in YEARS:
            self.year = yr
            self.create_sample_points(n, self.unirr_path, code=1)

    def irrigated(self, n):
        print('irrigated: {}'.format(n))
        self.create_sample_points(n, self.irr_path, code=0, attribute='YEAR')

    def shapefile_area_count(self, shapes):
        a = 0
        totals = []
        for shp in shapes:
            ct = 0
            with fiona.open(shp, 'r') as src:
                if not self.meta:
                    self.meta = src.meta
                for feat in src:
                    l = feat['geometry']['coordinates'][0]
                    if any(isinstance(i, list) for i in l):
                        l = l[0]
                    lon, lat = zip(*l)
                    x, y = self.aea(lon, lat)
                    cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
                    a += shape(cop).area
                    ct += 1
            totals.append((shp, a, ct))

        return totals

    def create_sample_points(self, n, shp, code, attribute=None):

        instance_ct = 0
        polygons = self._get_polygons(shp, attr=attribute)
        shuffle(polygons)
        if attribute:
            years, polygons = [x[1] for x in polygons], [x[0] for x in polygons]
        positive_area = sum([x.area for x in polygons])
        for i, poly in enumerate(polygons):
            if attribute:
                self.year = years[i]
            fractional_area = poly.area / positive_area
            required_points = max([1, fractional_area * n])
            x_range, y_range = self._random_points(poly.bounds, n)
            poly_pt_ct = 0
            for coord in zip(x_range, y_range):
                if Point(coord[0], coord[1]).within(poly):
                    self._add_entry(coord, val=code)
                    poly_pt_ct += 1
                    instance_ct += 1
                if poly_pt_ct >= required_points:
                    break
            if instance_ct > n:
                break

        print(self.extracted_points.shape, shp)

    def _random_points(self, coords, n):
        min_x, max_x = coords[0], coords[2]
        min_y, max_y = coords[1], coords[3]
        x_range = linspace(min_x, max_x, num=2 * n)
        y_range = linspace(min_y, max_y, num=2 * n)
        shuffle(x_range), shuffle(y_range)
        return x_range, y_range

    def _add_entry(self, coord, val=0):

        self.extracted_points = self.extracted_points.append({'FID': int(self.object_id),
                                                              'X': coord[0],
                                                              'Y': coord[1],
                                                              'POINT_TYPE': val,
                                                              'YEAR': int(self.year)},
                                                             ignore_index=True)
        self.object_id += 1

    def save_sample_points(self, path):

        points_schema = {
            'properties': dict([('FID', 'int:10'), ('POINT_TYPE', 'int:10'), ('YEAR', 'int:10')]),
            'geometry': 'Point'}
        crs = {'proj': 'longlat', 'ellps': 'WGS84', 'datum': 'WGS84'}
        meta = {'driver': 'ESRI Shapefile', 'schema': points_schema, 'crs': crs}

        with fiona.open(path, 'w', **meta) as output:
            for index, row in self.extracted_points.iterrows():
                props = dict([('FID', row['FID']),
                              ('POINT_TYPE', row['POINT_TYPE']),
                              ('YEAR', row['YEAR'])])

                pt = Point(row['X'], row['Y'])
                output.write({'properties': props,
                              'geometry': mapping(pt)})
        return None

    def _get_polygons(self, vector, attr=None):
        with fiona.open(vector, 'r') as src:
            polys = []
            bad_geo_count = 0
            for feat in src:
                try:
                    geo = shape(feat['geometry'])
                    if attr:
                        attribute = feat['properties'][attr]
                        polys.append((geo, attribute))
                    else:
                        polys.append(geo)
                except AttributeError:
                    bad_geo_count += 1

        return polys


if __name__ == '__main__':
    home = os.path.expanduser('~')
    gis = os.path.join(home, 'IrrigationGIS', 'EE_sample')
    extract = os.path.join(home, 'IrrigationGIS', 'EE_extracts', 'point_shp')

    kwargs = {
        'irrigated': 50000,
        'wetlands': 15000,
        'uncultivated': 15000,
        'unirrigated': 20000,
    }
    prs = PointsRunspec(gis, **kwargs)
    prs.save_sample_points(os.path.join(extract, 'sample_100k.shp'.format()))

# ========================= EOF ====================================================================
