# ===============================================================================
# Copyright 2020 dgketchum
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


def variable_importance():
    
    return [('CDL', 0.0634524752804307),
            ('NLCD', 0.05690229985097357),
            ('Near Infrared Late Spring', 0.04846799523587754),
            ('NDVI Max, Current Year', 0.045404237850643424),
            ('Near Infrared Summer', 0.04015844163951064),
            ('NDVI Max, Previous Year', 0.03563385257746881),
            ('Slope', 0.02745370484079356),
            ('NDVI Max, Two Years Previous', 0.027120492992345962),
            ('Latitude', 0.02708653896853951),
            ('Red Late Spring', 0.02537686479728658),
            ('Shortwave Infrared 2 Late Spring', 0.021513328748268033),
            ('Shortwave Infrared 2 Summer', 0.01904087261906528),
            ('Blue Late Spring', 0.016482011071812634),
            ('Red Summer', 0.014488388146875208),
            ('Near Infrared Early Spring', 0.014109373888127854),
            ('Blue Summer', 0.014008990183727296),
            ('Band 3 Late Spring', 0.012889125815902564),
            ('Shortwave Infrared 1 Summer', 0.011456235384148413),
            ('Longitude', 0.011414648884118032),
            ('Average Maximum Temperature, May', 0.011356055510761928),
            
            ('Average Maximum Temperature, April', 0.011262788934088353),
            ('Shortwave Infrared 1 Late Spring', 0.010766815521641755),
            ('tmax_6_1', 0.010381679009479833),
            ('prec_5', 0.010237884870189656),
            ('tpi_250', 0.01010375436780672),
            ('tpi_150', 0.009646955491424625),
            ('tmax_8', 0.00962357858336669),
            ('elevation', 0.009548001216463549),
            ('tmax_9', 0.009384967919768793),
            ('tpi_1250', 0.009177353266752366),
            ('prec_4', 0.008615873598120697),
            ('tmax_3_1', 0.008562484434796583),
            ('Band 3 Summer', 0.008005155368602353),
            ('prec_6', 0.0078851822152077),
            ('tmax_8_1', 0.007682154983091757),
            ('tmax_11', 0.007561127363055792),
            ('tavg_6', 0.007337233094385815),
            ('prec_3', 0.007332025556682602),
            ('tavg_5', 0.007312472482971807),
            ('prec_7', 0.007311856536881584),
            ('tmax_7_1', 0.0068430822338193),
            ('tmax_10', 0.006765866971534662),
            ('prec_10', 0.006633957215546568),
            ('prec_11', 0.006474117707037606),
            ('prec_1', 0.006313820949409482),
            ('tmin_5_1', 0.0062825593501239785),
            ('tmin_7_1', 0.0060392553253056066),
            ('prec_9', 0.005993855454584021),
            ('prec_8', 0.005908564364526284),
            ('tavg_4', 0.005860604537902074),
            ('prec_2', 0.0054741202130253915),
            ('tmax_1_1', 0.0054726663853758035),
            ('tmin_6_1', 0.005343130873879674),
            ('prec', 0.00524861040132165),
            ('B6', 0.005166791290553566),
            ('tavg', 0.004819368648763654),
            ('tavg_7', 0.004787644548246965),
            ('tmin_4_1', 0.004677801517941165),
            ('tmax_2_1', 0.004628333655043371),
            ('B7', 0.004076416939486642),
            ('tmin_8_1', 0.004027227707450473),
            ('tmin_9', 0.003892805334454492),
            ('tmin_8', 0.0037766228345785017),
            ('tavg_11', 0.003663487324016229),
            ('tavg_8', 0.0035220368663057304),
            ('B6_1', 0.003480281433773459),
            ('pet_total_wy_espr', 0.0034753767102169916),
            ('B7_1', 0.003414854431499345),
            ('tavg_1', 0.003393793463175746),
            ('tavg_3', 0.003204547438746576),
            ('tmin_3_1', 0.0030731040262944737),
            ('tavg_10', 0.0030714853239895224),
            ('tavg_2', 0.0030557217163336655),
            ('tmin_11', 0.00304178194524441),
            ('tmin_1_1', 0.0029906827746985316),
            ('B5', 0.002980391543357021),
            ('tmin_2_1', 0.0029191089040493247),
            ('tmax_1', 0.0027054223591845014),
            ('pet_total_wy', 0.0027034958389201775),
            ('tmax', 0.002700484587488438),
            ('tmin_10', 0.002600364234622706),
            ('pet_total_fl', 0.0025421688027858548),
            ('pet_total_wy_espr_1', 0.002539382646194657),
            ('tavg_9', 0.002500463007314728),
            ('tmmn_p90_cy', 0.0024873590100329304),
            ('tmmn_p50_cy', 0.0024635513246822967),
            ('tmin_4', 0.00246038297740898),
            ('tmin', 0.0023933942310409148),
            ('tmmx_p50_cy', 0.0023838148331634425),
            ('tmax_4', 0.0023286382092591014),
            ('tmax_5', 0.0023173336524520494),
            ('B4_1', 0.0023171209316247767),
            ('tmmx_p10_cy', 0.0023154604791868517),
            ('B2_1', 0.0023102795316000827),
            ('tmax_7', 0.0022711951709503166),
            ('precip_total_smr', 0.0022257296564084),
            ('tmax_6', 0.0021187256151930984),
            ('B3_1', 0.0021161789238096722),
            ('tmmn_p10_cy', 0.0021085689204314905),
            ('tmax_3', 0.0021075258554974744),
            ('pet_total_wy_smr', 0.0020804911841324674),
            ('tmax_2', 0.0020795145172560646),
            ('pet_total_espr', 0.0020071672368384757),
            ('wd_est_smr', 0.0019384548490692314),
            ('tmin_5', 0.0019219678140427767),
            ('wd_est_lspr', 0.0018610307229229388),
            ('precip_total_fl', 0.0017979859656002905),
            ('B4', 0.0017831679254514993),
            ('B3', 0.0017800721928572319),
            ('precip_total_lspr', 0.0017617688409138851),
            ('precip_total_wy_espr', 0.0017593943097505243),
            ('wd_est_fl', 0.0017578045585903152),
            ('pet_total_smr', 0.0017567031169599286),
            ('wd_est_espr', 0.001756147745065555),
            ('tmin_7', 0.0017554845563464935),
            ('wd_est_wy', 0.0017524453356127106),
            ('tmmx_p90_cy', 0.0016868057083063495),
            ('pet_total_lspr', 0.0016763868785166242),
            ('wd_est_wy_espr', 0.0016725601856504662),
            ('wd_est_wy_smr', 0.001647812393423027),
            ('tmin_6', 0.0016388750099385503),
            ('wd_est_cy', 0.0016123594375595275),
            ('tmin_3', 0.0015816629631309202),
            ('tmin_2', 0.0015699658039169718),
            ('wd_est_wy_espr_1', 0.0015266629501),
            ('tmin_1', 0.001507045548027179),
            ('B2', 0.0014528605524679072),
            ('precip_total_espr', 0.0014415072432761317),
            ('precip_total_wy', 0.001408804378669008),
            ('precip_total_wy_smr', 0.0013952117301119387),
            ('precip_total_wy_espr_1', 0.0012903256152915522),
            ('aspect', 0.0009753544678820362)]


def original_names():
    return [('nd_max_cy', 1.123669376175075),
            ('cdl', 0.6335157366711089),
            ('nlcd', 0.6277971880312423),
            ('nd_max_m1', 0.46110953330358045),
            ('nd_max_m2', 0.3952109157526078),
            ('slope', 0.32994448078951216),
            ('LAT_GCS', 0.24825634842267602),
            ('Lon_GCS', 0.24681129064240176),
            ('prec_5', 0.14147191034108403),
            ('elevation', 0.13410563221501595),
            ('tmin_5_1', 0.1297061794160177),
            ('prec_3', 0.1237544715866357),
            ('prec_7', 0.12017946136956616),
            ('prec_6', 0.116260405911803),
            ('prec_4', 0.11261507952037447),
            ('prec_8', 0.10857502069826248),
            ('tpi_250', 0.10493711253360248),
            ('tpi_150', 0.1013573426487323),
            ('tmin_4_1', 0.1002741375141118),
            ('tmin_7_1', 0.09349233514919655),
            ('tmin_6_1', 0.08876373571285734),
            ('tavg_6', 0.08859195991138616),
            ('prec_9', 0.08850640265618763),
            ('tavg_5', 0.08793610612331132),
            ('tpi_1250', 0.0824715451301573),
            ('tmax_4_1', 0.08063916400135623),
            ('tavg_4', 0.0796714944151321),
            ('prec_1', 0.07605744063003231),
            ('prec_2', 0.07587854307943792),
            ('prec', 0.07489639881482567),
            ('prec_11', 0.0746024988987807),
            ('prec_10', 0.07218814928469883),
            ('tmax_8', 0.07146876235496298),
            ('tmax_11', 0.0653938855233019),
            ('tavg_7', 0.06479639031511003),
            ('tmax_5_1', 0.06321178861860438),
            ('B6_3', 0.06251399336325851),
            ('tmin_3_1', 0.06053205412158286),
            ('tmax_10', 0.06031478888956829),
            ('tmax_3_1', 0.0561022060303009),
            ('B6', 0.05547696392821559),
            ('tmax_7_1', 0.05522810151030568),
            ('tmax_9', 0.054801355245730876),
            ('tmin_8_1', 0.05467464824519319),
            ('tmin_8', 0.05461610318123322),
            ('B6_1', 0.05364072370317913),
            ('tmax_6_1', 0.05253842132461088),
            ('tavg', 0.05218882357189648),
            ('tmax_2_1', 0.05155078197503294),
            ('B6_2', 0.05125147274521081),
            ('tmax_1_1', 0.050260240593881),
            ('tmax_8_1', 0.04812251888400358),
            ('tmin_11', 0.04779688247716514),
            ('tavg_3', 0.04710519465632969),
            ('tmmn_p90_cy', 0.04705987701475324),
            ('tmin_9', 0.04704818231662117),
            ('tavg_11', 0.046249144319856675),
            ('B7', 0.04589921188088317),
            ('tmin_1_1', 0.044863996487846725),
            ('precip_total_smr', 0.04426142551640924),
            ('tavg_1', 0.04388274520549059),
            ('B7_3', 0.042394949675845624),
            ('pet_total_wy_espr', 0.04194866732288152),
            ('B7_2', 0.04150474279382775),
            ('tmin_10', 0.04058311056746127),
            ('tmax_1', 0.03918046723657307),
            ('B7_1', 0.03904916089888027),
            ('tavg_2', 0.03830979546482897),
            ('tmax_2', 0.038128694194381085),
            ('tavg_10', 0.03695449432245409),
            ('tavg_9', 0.03468661756199653),
            ('precip_total_lspr', 0.03452237488577307),
            ('tavg_8', 0.03395105798500401),
            ('tmin_2_1', 0.033797207792251406),
            ('wd_est_smr', 0.03369611792919266),
            ('wd_est_lspr', 0.03222822798861234),
            ('tmmn_p50_cy', 0.0322198397945636),
            ('tmax', 0.03210552561048149),
            ('pet_total_wy_espr_1', 0.0318955720821772),
            ('pet_total_wy', 0.03134962721714284),
            ('tmax_4', 0.031193467899054982),
            ('tmmn_p10_cy', 0.03119247203739063),
            ('pet_total_lspr', 0.030951973955982613),
            ('tmax_3', 0.03067226441830118),
            ('pet_total_fl', 0.030245773803623914),
            ('wd_est_fl', 0.030181155388864782),
            ('precip_total_wy', 0.029902883596859102),
            ('precip_total_fl', 0.02987594561595978),
            ('tmax_5', 0.029677329582174897),
            ('pet_total_smr', 0.02929621759414766),
            ('tmax_6', 0.029185986466906542),
            ('tmax_7', 0.028321679797730717),
            ('precip_total_wy_smr', 0.028209672916074527),
            ('tmmx_p10_cy', 0.027650572794850403),
            ('B5_3', 0.027238985763224838),
            ('nd', 0.02694704387286878),
            ('pet_total_espr', 0.026580350104406097),
            ('tmmx_p50_cy', 0.02654090494587063),
            ('B5', 0.026475482021625432),
            ('B5_1', 0.026371745641371885),
            ('pet_total_wy_smr', 0.02616079953570917),
            ('tmmx_p90_cy', 0.02614533320671197),
            ('B5_2', 0.026068747544105375),
            ('wd_est_cy', 0.025865608504198414),
            ('nd_1', 0.02542323686093907),
            ('nd_2', 0.025423112403829065),
            ('wd_est_wy', 0.024934396899890108),
            ('nd_1_1', 0.02492405987102031),
            ('tmin_1', 0.02462302386382525),
            ('wd_est_wy_espr', 0.02436929956901151),
            ('tmin', 0.024227575276435667),
            ('wd_est_wy_smr', 0.024032748238249368),
            ('tmin_2', 0.023727011774036327),
            ('precip_total_wy_espr', 0.023623564161912525),
            ('wd_est_wy_espr_1', 0.0235578547139526),
            ('precip_total_wy_espr_1', 0.02320505264024162),
            ('wd_est_espr', 0.023114468105789182),
            ('precip_total_espr', 0.023078921870580298),
            ('tmin_3', 0.023014214774608972),
            ('tmin_4', 0.021838439955570683),
            ('tmin_7', 0.020759646494493463),
            ('B4_2', 0.019895982562541138),
            ('tmin_6', 0.01986759367832651),
            ('B4_1', 0.01965927956332427),
            ('tmin_5', 0.019382198528460497),
            ('B4', 0.018564005074093195),
            ('B4_3', 0.01776682139645029),
            ('B3_1', 0.017754640131369247),
            ('B3', 0.017362697784505818),
            ('B3_3', 0.016805139340410523),
            ('B3_2', 0.0163928032794072),
            ('B2_3', 0.014203316587390867),
            ('B2_1', 0.014064291318986845),
            ('B2', 0.013578303113797971),
            ('B2_2', 0.013556292774949966),
            ('aspect', 0.011713277707947677)]



if __name__ == '__main__':
    pass
# ========================= EOF ====================================================================
