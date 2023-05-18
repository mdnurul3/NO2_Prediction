import ee 
#from ee_plugin import Map 

l8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA"),
    

    # shown: False #
geom =ee.Geometry.Polygon(
        [[[-115.02016881393736, 34.90413690992207],
          [-116.90981725143736, 35.00318711746454],
          [-118.23916295456236, 34.651469707462574],
          [-118.82143834518736, 32.82439958230415],
          [-115.65737584518736, 31.905731861680593],
          [-115.62441686081236, 33.59650578636102],
          [-114.99819615768736, 34.74179680606179]]]),
   

    # shown: False #
water =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-115.97278956855662, 33.443742629714656]),
            {
              "LC": 0,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.88489894355662, 33.3336654048209]),
            {
              "LC": 0,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.72559718574412, 33.29235052719973]),
            {
              "LC": 0,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.78052882636912, 33.24182798649531]),
            {
              "LC": 0,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.72559718574412, 33.17288653346188]),
            {
              "LC": 0,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.45020656074412, 33.86441102228299]),
            {
              "LC": 0,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.32386378730662, 33.38872144059121]),
            {
              "LC": 0,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.35706691230662, 33.126895411057596]),
            {
              "LC": 0,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.63253942151083, 33.90127575063992]),
            {
              "LC": 0,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.6201798023702, 33.90697471695407]),
            {
              "LC": 0,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.6146866383077, 33.9035553828816]),
            {
              "LC": 0,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.17798009533895, 33.852248917860976]),
            {
              "LC": 0,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.44165197033895, 33.84768685057153]),
            {
              "LC": 0,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.4334122242452, 33.837421308447915]),
            {
              "LC": 0,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.62429967541708, 33.9035553828816]),
            {
              "LC": 0,
              "system:index": "14"
            })]),
    

    # shown: False #
forest =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-116.95825353283895, 34.14825996342487]),
            {
              "LC": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.93628087658895, 34.15053297067074]),
            {
              "LC": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.90744176526083, 34.15394236685185]),
            {
              "LC": 1,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.7193008961202, 33.803193929566255]),
            {
              "LC": 1,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.7302872242452, 33.78150950579959]),
            {
              "LC": 1,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.71518102307333, 33.77694366414588]),
            {
              "LC": 1,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.53044979628866, 33.71927898642317]),
            {
              "LC": 1,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.50710384902304, 33.71299633387087]),
            {
              "LC": 1,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.4665917640621, 33.67243360968597]),
            {
              "LC": 1,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.48169796523398, 33.67471934248559]),
            {
              "LC": 1,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.53353970107382, 33.71870785518837]),
            {
              "LC": 1,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.54555599746054, 33.73384154904329]),
            {
              "LC": 1,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.61525051650351, 33.801482201071174]),
            {
              "LC": 1,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.51774685439413, 33.722134585602944]),
            {
              "LC": 1,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.53285305556601, 33.71642329225411]),
            {
              "LC": 1,
              "system:index": "14"
            })]),
    

    # shown: False #
indust =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.23157524077578, 33.83892305482116]),
            {
              "LC": 2,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.22290634123965, 33.83892305482116]),
            {
              "LC": 2,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.21938728301211, 33.83885176327515]),
            {
              "LC": 2,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25818275420352, 33.83664169585194]),
            {
              "LC": 2,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.22488044707461, 33.81796077908724]),
            {
              "LC": 2,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.21990226714297, 33.81753292402876]),
            {
              "LC": 2,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.23749755828067, 33.842416267722264]),
            {
              "LC": 2,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.23758338896914, 33.839921130220716]),
            {
              "LC": 2,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.20694183318301, 33.83628522801208]),
            {
              "LC": 2,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.20737098662539, 33.834930636661845]),
            {
              "LC": 2,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.20488189665957, 33.83614264045987]),
            {
              "LC": 2,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.19638465850039, 33.83542969913065]),
            {
              "LC": 2,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.19715713469668, 33.83207879522715]),
            {
              "LC": 2,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.1967279812543, 33.830938032012746]),
            {
              "LC": 2,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.22239135710879, 33.81753292402876]),
            {
              "LC": 2,
              "system:index": "14"
            })]),
    

    # shown: False #
land =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.27234481780215, 33.83364731979055]),
            {
              "LC": 3,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.26831077544375, 33.83043894331958]),
            {
              "LC": 3,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.27114318816348, 33.82302356809442]),
            {
              "LC": 3,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.27560638396426, 33.820242636584766]),
            {
              "LC": 3,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.31483100859805, 33.840562743965116]),
            {
              "LC": 3,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.31011032073184, 33.84177466789448]),
            {
              "LC": 3,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.32075332610293, 33.83535840467064]),
            {
              "LC": 3,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.31843589751406, 33.834217685223145]),
            {
              "LC": 3,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.26341842620059, 33.82608961852539]),
            {
              "LC": 3,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25045799224063, 33.82544789613703]),
            {
              "LC": 3,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25157379119082, 33.831722308357925]),
            {
              "LC": 3,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25698112456485, 33.831864903284014]),
            {
              "LC": 3,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.2487413784711, 33.83257787434654]),
            {
              "LC": 3,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.26805328337832, 33.827087843778656]),
            {
              "LC": 3,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.27131484954043, 33.8415608002147]),
            {
              "LC": 3,
              "system:index": "14"
            })]),
    

    # shown: False #
agrucal =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.42203353850527, 33.90049918750603]),
            {
              "LC": 4,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.4355089565961, 33.902671983138184]),
            {
              "LC": 4,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.43507980315371, 33.90128282510156]),
            {
              "LC": 4,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.43808387725039, 33.90142530389059]),
            {
              "LC": 4,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.43735431639834, 33.900285466911825]),
            {
              "LC": 4,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.43246196715518, 33.89764953553652]),
            {
              "LC": 4,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.41559623686953, 33.90046356744421]),
            {
              "LC": 4,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.41439460723086, 33.89910999406785]),
            {
              "LC": 4,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.41808532683535, 33.901069106471624]),
            {
              "LC": 4,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.402893294975, 33.90477348688964]),
            {
              "LC": 4,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.40190624205752, 33.90377616953394]),
            {
              "LC": 4,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.42117523162051, 33.89975116308255]),
            {
              "LC": 4,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.43023036925479, 33.89558347830791]),
            {
              "LC": 4,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.3505365750043, 33.892804908630275]),
            {
              "LC": 4,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.38615631072207, 33.91047221938226]),
            {
              "LC": 4,
              "system:index": "14"
            })]),
    

    # shown: False #
develop =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.34071889205877, 33.89609353532702]),
            {
              "LC": 5,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33956017776434, 33.89620040094451]),
            {
              "LC": 5,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.34636225982611, 33.8927628231212]),
            {
              "LC": 5,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.3384014634699, 33.890785707830005]),
            {
              "LC": 5,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33765044494574, 33.893190301482456]),
            {
              "LC": 5,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33432450576727, 33.89067883542756]),
            {
              "LC": 5,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33475365920965, 33.89012665921504]),
            {
              "LC": 5,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33202853485052, 33.894365855928086]),
            {
              "LC": 5,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33151355071966, 33.895630449437085]),
            {
              "LC": 5,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.35451617523138, 33.89725123905003]),
            {
              "LC": 5,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.34550395294134, 33.89896104964637]),
            {
              "LC": 5,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.3022882012934, 33.8944371011313]),
            {
              "LC": 5,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.30636515899603, 33.892620329857955]),
            {
              "LC": 5,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.30190196319525, 33.893760269297886]),
            {
              "LC": 5,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.30108657165472, 33.891800988974474]),
            {
              "LC": 5,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.32164302154486, 33.885815999461364]),
            {
              "LC": 5,
              "system:index": "15"
            })]),
    

    # shown: False #
highway =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.25650883201259, 33.85582305900079]),
            {
              "LC": 6,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25655174735682, 33.85532411563621]),
            {
              "LC": 6,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25631571296351, 33.854629153949624]),
            {
              "LC": 6,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25603676322596, 33.85443313809259]),
            {
              "LC": 6,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25582218650477, 33.85384508782231]),
            {
              "LC": 6,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25565052512782, 33.853221393717654]),
            {
              "LC": 6,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.2555217790951, 33.85254423496186]),
            {
              "LC": 6,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25511408332484, 33.852472954780566]),
            {
              "LC": 6,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25498533729213, 33.85193835152471]),
            {
              "LC": 6,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25483513358729, 33.85147502599654]),
            {
              "LC": 6,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25464201453822, 33.85101169795528]),
            {
              "LC": 6,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25455618384974, 33.85047708555416]),
            {
              "LC": 6,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25401974204676, 33.849336567916104]),
            {
              "LC": 6,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25378370765345, 33.84867719921047]),
            {
              "LC": 6,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.25356913093226, 33.84816039315384]),
            {
              "LC": 6,
              "system:index": "14"
            })]),
    

    # shown: False #
grass =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.40416604240534, 33.84985539986808]),
            {
              "LC": 7,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.39721375663873, 33.85028309316922]),
            {
              "LC": 7,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.38961774070856, 33.84714662590285]),
            {
              "LC": 7,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.39133435447809, 33.84390311251184]),
            {
              "LC": 7,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.3986299629986, 33.84443776605163]),
            {
              "LC": 7,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.40408021171686, 33.84522191852505]),
            {
              "LC": 7,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.41553860862848, 33.84433083561131]),
            {
              "LC": 7,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.41940098960993, 33.847004056472905]),
            {
              "LC": 7,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.42197591026422, 33.85178000286031]),
            {
              "LC": 7,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.41322118003961, 33.848643590553266]),
            {
              "LC": 7,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.38592702110407, 33.84507934588332]),
            {
              "LC": 7,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.38099175651666, 33.843012015844465]),
            {
              "LC": 7,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.39120560844538, 33.84126543941981]),
            {
              "LC": 7,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.39498215873834, 33.84714662590285]),
            {
              "LC": 7,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.39592629631159, 33.84308330391982]),
            {
              "LC": 7,
              "system:index": "14"
            })]),
    

    # shown: False #
nodevelop =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.04943728650811, 33.85794516696535]),
            {
              "LC": 8,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.04342913831475, 33.86250668636492]),
            {
              "LC": 8,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.03621936048272, 33.85937066795275]),
            {
              "LC": 8,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.0465190430999, 33.8535259626906]),
            {
              "LC": 8,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.03793597425225, 33.84853626369757]),
            {
              "LC": 8,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.05596041883233, 33.84212050817495]),
            {
              "LC": 8,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.0926959535003, 33.855806870869145]),
            {
              "LC": 8,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.10574221814873, 33.85309828562596]),
            {
              "LC": 8,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.1040256043792, 33.84853626369757]),
            {
              "LC": 8,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.14007449353936, 33.833422826029825]),
            {
              "LC": 8,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.15466571058037, 33.826435522273094]),
            {
              "LC": 8,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.15827059949639, 33.822014688235676]),
            {
              "LC": 8,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.0102984925628, 33.84126503770649]),
            {
              "LC": 8,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.01939654554131, 33.83527650463887]),
            {
              "LC": 8,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.04308581556084, 33.839411488978776]),
            {
              "LC": 8,
              "system:index": "14"
            })]),
    

    # shown: False #
ocean =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-119.23030360896297, 33.72433927823861]),
            {
              "LC": 9,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-119.23030360896297, 33.37870553634147]),
            {
              "LC": 9,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.98311122615047, 33.22490270053802]),
            {
              "LC": 9,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.94740565974422, 33.323643162651095]),
            {
              "LC": 9,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.82380946833797, 33.61461890833523]),
            {
              "LC": 9,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.96113856990047, 33.79740838439028]),
            {
              "LC": 9,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.00532802302547, 33.176640050004856]),
            {
              "LC": 9,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-119.38737808038887, 33.614004347567075]),
            {
              "LC": 9,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-119.38188491632637, 33.47894718779179]),
            {
              "LC": 9,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-119.10997329523262, 33.18521738586423]),
            {
              "LC": 9,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.89024673273262, 33.095524978624226]),
            {
              "LC": 9,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-119.00011001398262, 33.67573971914002]),
            {
              "LC": 9,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.65404067804512, 33.77853356292046]),
            {
              "LC": 9,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-119.12919936945137, 33.87436332326914]),
            {
              "LC": 9,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.10197768976387, 33.42853289237118]),
            {
              "LC": 9,
              "system:index": "14"
            })]),
    

    # shown: False #
open_space =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-116.02182100004782, 33.16810042955021]),
            {
              "LC": 10,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.20309541411032, 33.23245099181157]),
            {
              "LC": 10,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.14816377348532, 33.04846686230101]),
            {
              "LC": 10,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.08224580473532, 32.96093939887935]),
            {
              "LC": 10,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.91195771879782, 32.96093939887935]),
            {
              "LC": 10,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.86801240629782, 32.99319646272519]),
            {
              "LC": 10,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.63180635161032, 34.42341688224072]),
            {
              "LC": 10,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.52743623442282, 34.25105353808907]),
            {
              "LC": 10,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.36264131254782, 34.31005980082516]),
            {
              "LC": 10,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.25827119536032, 34.15564827654539]),
            {
              "LC": 10,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.36813447661032, 34.11472726675979]),
            {
              "LC": 10,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.42855928129782, 34.160193832200264]),
            {
              "LC": 10,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.57138154692282, 34.19200586935699]),
            {
              "LC": 10,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.18136689848532, 34.041929903375376]),
            {
              "LC": 10,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.14291475004782, 32.98858903221169]),
            {
              "LC": 10,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.14291475004782, 32.88255178271352]),
            {
              "LC": 10,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.02206514067282, 32.9102259284886]),
            {
              "LC": 10,
              "system:index": "16"
            })]),
    

    # shown: False #
soil =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-116.05947341618645, 34.54947735535196]),
            {
              "LC": 11,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.04299392399895, 34.556829134852634]),
            {
              "LC": 11,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.07045974431145, 34.53364054713986]),
            {
              "LC": 11,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.0567268341552, 34.54325611147813]),
            {
              "LC": 11,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.81777419743645, 34.55513262801157]),
            {
              "LC": 11,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.82326736149895, 34.55230503973004]),
            {
              "LC": 11,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.93107070622551, 34.52119522705764]),
            {
              "LC": 11,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.93381728825676, 34.51044549950346]),
            {
              "LC": 11,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.08350600895989, 34.52515530336298]),
            {
              "LC": 11,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.07183303532707, 34.52968087430603]),
            {
              "LC": 11,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.05329360661614, 34.5392968959673]),
            {
              "LC": 11,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.04093398747551, 34.55230503973004]),
            {
              "LC": 11,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.10204543767082, 34.642175267333165]),
            {
              "LC": 11,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-115.80678786931145, 34.55230503973004]),
            {
              "LC": 11,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.27233352360832, 34.47875402513028]),
            {
              "LC": 11,
              "system:index": "14"
            })]),
    

geometry =ee.Geometry.Polygon(
        [[[-118.99748153258662, 34.94344488570756],
          [-118.99748153258662, 32.49479014154221],
          [-114.87760848571162, 32.49479014154221],
          [-114.87760848571162, 34.94344488570756]]], {}, False),
    

    # shown: False #
very_high =ee.Geometry.Polygon(
        [[[-117.87881097510744, 33.852674520465605],
          [-117.89529046729494, 33.9028409268627],
          [-117.90627679541994, 33.98942249320485],
          [-117.94472894385744, 34.08956473057982],
          [-118.01614007666994, 34.10321132674285],
          [-118.20840081885744, 34.116855722363375],
          [-118.30178460791994, 34.135044826067535],
          [-118.38418206885744, 34.053163052461805],
          [-118.51052484229494, 33.94386422606809],
          [-118.48305902198244, 33.87092026214236],
          [-118.29079827979494, 33.78878373259781],
          [-118.00515374854494, 33.770520456848466],
          [-117.85683831885744, 33.77508664085528]]]),
    

    # shown: False #
high =ee.Geometry.Polygon(
        [[[-117.88705072120119, 33.679145693969595],
          [-117.93374261573244, 33.66314511217227],
          [-117.92000970557619, 33.6448550884033],
          [-117.85409173682619, 33.642568562137896],
          [-117.80739984229494, 33.66771701071961],
          [-117.77444085791994, 33.690572858276866],
          [-117.73873529151369, 33.71342262905322],
          [-117.74422845557619, 33.77280357927201],
          [-117.73324212745119, 33.809325262414575],
          [-117.68929681495119, 33.82758026076244],
          [-117.63161859229494, 33.84355018772114],
          [-117.65633783057619, 33.88004167082042],
          [-117.69478997901369, 33.88460200956376],
          [-117.72500238135744, 33.86635919223945],
          [-117.75521478370119, 33.83670629868333],
          [-117.76620111182619, 33.784218278745946],
          [-117.76620111182619, 33.74311824295774],
          [-117.79092035010744, 33.71799185381717],
          [-117.84585199073244, 33.69285810884298]]]),
    

    # shown: False #
middle1 =ee.Geometry.MultiPolygon(
        [[[[-118.64510736182619, 34.02357517440585],
           [-118.58468255713869, 34.03950839123531],
           [-118.52975091651369, 34.078190886443224],
           [-118.49679193213869, 34.10093704685314],
           [-118.46383294776369, 34.1191295743291],
           [-118.48580560401369, 34.135044826067535],
           [-118.52425775245119, 34.13277140212077],
           [-118.54073724463869, 34.105485545506376],
           [-118.59566888526369, 34.08274060742591],
           [-118.65060052588869, 34.057714117557666],
           [-118.69729242041994, 34.02585153142827]]],
         [[[-117.47369012549807, 33.85381499353739],
           [-117.44347772315432, 33.87434090463969],
           [-117.40502557471682, 33.88574205616403],
           [-117.36382684424807, 33.88118177835709],
           [-117.32812127784182, 33.89258201582782],
           [-117.35558709815432, 33.924494574293306],
           [-117.39403924659182, 33.93588902068929],
           [-117.44347772315432, 33.93588902068929],
           [-117.47643670752932, 33.9108192265467],
           [-117.48742303565432, 33.87434090463969]]]]),
    

    # shown: False #
middle2 =ee.Geometry.MultiPolygon(
        [[[[-117.48467645362307, 33.76937887282226],
           [-117.43798455909182, 33.744260176734585],
           [-117.40227899268557, 33.75339509959192],
           [-117.38854608252932, 33.79449020760555],
           [-117.35558709815432, 33.82187599233715],
           [-117.29790887549807, 33.81731230362093],
           [-117.27318963721682, 33.7990551137466],
           [-117.23748407081057, 33.7990551137466],
           [-117.22100457862307, 33.824157745371416],
           [-117.16881952002932, 33.83784698491785],
           [-117.16881952002932, 33.88118177835709],
           [-117.19903192237307, 33.894861880495384],
           [-117.24572381690432, 33.86293822989105],
           [-117.28966912940432, 33.846971926698664],
           [-117.33910760596682, 33.85609589399742],
           [-117.41051873877932, 33.824157745371416],
           [-117.45995721534182, 33.78992505802746]]],
         [[[-117.10015496924807, 34.07022828659905],
           [-117.13860711768557, 34.031542156842754],
           [-117.16332635596682, 33.995115560489246],
           [-117.18804559424807, 33.97006321153339],
           [-117.13860711768557, 33.94044637238474],
           [-117.11663446143557, 33.974618733254786],
           [-117.08916864112307, 34.01788401472528]]],
         [[[-118.26470575049807, 33.47408232193863],
           [-118.35808953956057, 33.490117986940426],
           [-118.37731561377932, 33.43054198558172],
           [-118.23998651221682, 33.37780602531756],
           [-118.20702752784182, 33.446585705377885],
           [-118.22900018409182, 33.471791270337185]]]]),
    

    # shown: False #
low =ee.Geometry.MultiPolygon(
        [[[[-117.12762078956057, 33.606859604621604],
           [-117.10015496924807, 33.63659203410878],
           [-117.06719598487307, 33.680028663248855],
           [-117.02325067237307, 33.70516616112294],
           [-116.97381219581057, 33.74171666503811],
           [-117.05895623877932, 33.82389836544953],
           [-117.10564813331057, 33.79423073772672],
           [-117.12762078956057, 33.71658986545365],
           [-117.21276483252932, 33.67774307157805],
           [-117.22375116065432, 33.63430528841132],
           [-117.13586053565432, 33.58169338332602]]],
         [[[-117.41784240409383, 33.66174222881453],
           [-117.47277404471883, 33.68688507370227],
           [-117.47552062675008, 33.59542132336418],
           [-117.42608215018758, 33.446585705377885],
           [-117.34917785331258, 33.439710188723765],
           [-117.23107482596883, 33.51073090799547],
           [-117.37115050956258, 33.64930201757318]]]]),
    

    # shown: False #
very_low =ee.Geometry.MultiPolygon(
        [[[[-116.77788879081258, 33.685876287205176],
           [-116.84380675956258, 33.67673417780146],
           [-116.90972472831258, 33.64472914053606],
           [-116.89324523612508, 33.53490725640481],
           [-116.88775207206258, 33.42494568246685],
           [-116.78338195487508, 33.489106897099596],
           [-116.74492980643758, 33.57610684501676],
           [-116.68999816581258, 33.653874651685214],
           [-116.71197082206258, 33.685876287205176]]],
         [[[-119.79363586112508, 33.62643520346115],
           [-119.82659484550008, 33.72700374645183],
           [-119.90899230643758, 33.658447042855926],
           [-119.95293761893758, 33.521169694298614],
           [-119.93645812675008, 33.43869851072996],
           [-119.81560851737508, 33.38826082162297],
           [-119.78814269706258, 33.50284955034646]]],
         [[[-117.36016418143758, 34.7352165847824],
           [-117.27776672050008, 34.77583483809846],
           [-117.22283507987508, 34.87053302356739],
           [-117.17339660331258, 34.93360463182369],
           [-117.14593078300008, 35.02362285966928],
           [-117.16790343925008, 35.100060513119665],
           [-117.42608215018758, 35.09556616195351],
           [-117.43706847831258, 35.02362285966928],
           [-117.35467101737508, 34.893064158278236],
           [-117.38763000175008, 34.79839189942491]]]]),
    

    # shown: False #
clear =ee.Geometry.MultiPolygon(
        [[[[-118.44521340601845, 37.08481140105456],
           [-118.68691262476845, 36.751038115228276],
           [-118.62099465601845, 36.39812242976876],
           [-118.46718606226845, 36.07912170742531],
           [-118.02773293726845, 36.15012321560942],
           [-118.15956887476845, 36.48650251503506],
           [-118.31337746851845, 36.78624090754]]],
         [[[-106.36025246851845, 36.46883455198238],
           [-105.81093606226845, 36.64533280799959],
           [-106.14052590601845, 37.08481140105456],
           [-106.64589699976845, 36.962012279880575],
           [-106.68984231226845, 36.610065415235425]]]]),
   

    # shown: False #
h1 =ee.Geometry.MultiPolygon(
        [[[[-118.04420945995632, 34.09402490225861],
           [-118.05450914257351, 34.092887646515834],
           [-118.05897233837429, 34.08862280140084],
           [-118.06446550243679, 34.086632466818926],
           [-118.05450914257351, 34.080092466624805],
           [-118.05622575634304, 34.07582697698938],
           [-118.06618211620632, 34.070708105872875],
           [-118.06892869823757, 34.0664421436625],
           [-118.0706453120071, 34.059047300367126],
           [-118.06892869823757, 34.054496306851455],
           [-118.05897233837429, 34.04795382560769],
           [-118.05279252880398, 34.04311775411708],
           [-118.04626939647976, 34.039703890546114],
           [-118.03837297313991, 34.04368671801896],
           [-118.02384844739535, 34.04738489033558],
           [-118.02762499768832, 34.052220718465826],
           [-118.04616442639926, 34.05620295805402],
           [-118.0595540138016, 34.061038283193355],
           [-118.06298724134066, 34.064451287792224],
           [-118.05165759046176, 34.06985493061432],
           [-118.04101458509066, 34.069001746763895],
           [-118.02796832044223, 34.069286142335336],
           [-118.01869860608676, 34.068432952757064],
           [-118.02728167493441, 34.07440509937371],
           [-118.03552142102816, 34.07838629654919],
           [-118.04204455335238, 34.08208295493674],
           [-118.04204455335238, 34.090613089192544]]],
         [[[-118.22351829843905, 34.039411648742245],
           [-118.22592155771639, 34.04581255226828],
           [-118.22849647837069, 34.05121738344759],
           [-118.22780983286287, 34.05704852541105],
           [-118.22695152597811, 34.06159938189554],
           [-118.22163002329256, 34.064159131283226],
           [-118.2262648804703, 34.07183791551165],
           [-118.23845283823397, 34.06714540784403],
           [-118.24875252085116, 34.06799861038777],
           [-118.25476066904451, 34.06501236389689],
           [-118.26420204477694, 34.057332961100094],
           [-118.26883690195467, 34.04879947524548],
           [-118.26986687021639, 34.038558158438],
           [-118.26437370615389, 34.03258348584752],
           [-118.25441734629061, 34.028457871100876],
           [-118.23639290171053, 34.031018621109986],
           [-118.22523491220858, 34.03301026213031],
           [-118.22248833017733, 34.037277906879005]]],
         [[[-118.06558983164217, 34.07283326251285],
           [-118.13906090097811, 34.071980108656405],
           [-118.14300911264803, 34.072122301562494],
           [-118.15382377939608, 34.06757201018984],
           [-118.16154854135897, 34.063021474434265],
           [-118.16549675302889, 34.06273705783567],
           [-118.17098991709139, 34.062594849178375],
           [-118.17579643564608, 34.06031947820735],
           [-118.18403618173983, 34.05591077311011],
           [-118.17957298593905, 34.057332961100094],
           [-118.17047493296053, 34.060888326677336],
           [-118.16601173715975, 34.06046169068278],
           [-118.16532509165194, 34.05690630720861],
           [-118.16429512339022, 34.053492998764995],
           [-118.1658400757828, 34.05036401195584],
           [-118.1691016419449, 34.046239261992554],
           [-118.17030327158358, 34.043821211830526],
           [-118.17030327158358, 34.03514411134115],
           [-118.168758319191, 34.03656664766348],
           [-118.16892998056795, 34.042967765899725],
           [-118.16755668955233, 34.044959126378004],
           [-118.16395180063631, 34.05064847007416],
           [-118.16412346201326, 34.06060390291959],
           [-118.15914528208162, 34.063163682375645],
           [-118.14833061533358, 34.0687096059445],
           [-118.14489738779451, 34.070415970937376],
           [-118.14197914438631, 34.07098475163109],
           [-118.06576149301912, 34.07155352850613]]],
         [[[-118.05532217787378, 33.917149008918074],
           [-118.05600882338159, 33.92996875934423],
           [-118.04879904554956, 33.936235490716356],
           [-118.05909872816675, 33.9487675698749],
           [-118.05154562758081, 33.953893797761914],
           [-118.05257559584253, 33.95901971684676],
           [-118.05223227308862, 33.96329108017739],
           [-118.06287527845971, 33.96955535843146],
           [-118.06665182875268, 33.96471482029389],
           [-118.07489157484643, 33.95987400667022],
           [-118.07454825209253, 33.95218508944316],
           [-118.08210135267846, 33.94905236841397],
           [-118.07763815687768, 33.93481127408119],
           [-118.06871176527612, 33.92370156683152],
           [-118.06493521498315, 33.917149008918074],
           [-118.05772543715112, 33.915439563106375]]]]),
    

    # shown: False #
h2 =ee.Geometry.MultiPolygon(
        [[[[-118.22526694105737, 33.98094377313087],
           [-118.22458029554956, 33.97496504561298],
           [-118.21977377699487, 33.969270628520185],
           [-118.215653903948, 33.95958924434889],
           [-118.21359396742456, 33.94933716600002],
           [-118.22355032728784, 33.945065102143104],
           [-118.22389365004175, 33.9353809635938],
           [-118.21634054945581, 33.93053848125224],
           [-118.19196463392846, 33.919713113335135],
           [-118.18166495131128, 33.91657919745785],
           [-118.19265127943628, 33.953324232134655],
           [-118.19574118422143, 33.962436824668806],
           [-118.18475485609643, 33.962436824668806],
           [-118.17685843275659, 33.95702634056484],
           [-118.17376852797143, 33.96272157745822],
           [-118.17239523695581, 33.97154844111748],
           [-118.17308188246362, 33.97895091067593],
           [-118.1772017555105, 33.98407531973865],
           [-118.18509817885034, 33.991192042036786],
           [-118.1995177345144, 33.99289996670617],
           [-118.20260763929956, 33.99147669853236],
           [-118.20020438002221, 33.98151315382265],
           [-118.20947409437768, 33.98322127301468],
           [-118.22183371351831, 33.9849293578811]]],
         [[[-118.27882529066675, 33.97354147709026],
           [-118.24792624281518, 33.968985897655635],
           [-118.2379698829519, 33.97724270567355],
           [-118.24243307875268, 33.98806075764895],
           [-118.25170279310815, 33.9980235347293],
           [-118.25376272963159, 34.01026191864761],
           [-118.25273276136987, 34.01879928158214],
           [-118.25273276136987, 34.025628553763966],
           [-118.26200247572534, 34.03046562240636],
           [-118.26921225355737, 34.03359534341755],
           [-118.27298880385034, 34.0244903798946],
           [-118.27779532240503, 34.016522735411115],
           [-118.27813864515893, 34.00770054236143],
           [-118.27745199965112, 33.99603107276939],
           [-118.2764220313894, 33.984644679453794],
           [-118.27813864515893, 33.97695800150286],
           [-118.27848196791284, 33.98065908135481]]]]),
    

    # shown: False #
h3 =ee.Geometry.Polygon(
        [[[-118.26353321202568, 34.06163357380775],
          [-118.27760944493583, 34.06902819142513],
          [-118.2810426724749, 34.07755964062006],
          [-118.28756580479912, 34.084668525226625],
          [-118.29443225987724, 34.08495286819825],
          [-118.29889545567802, 34.08068762336654],
          [-118.29958210118583, 34.075000296081186],
          [-118.30026874669365, 34.05964260496616],
          [-118.30164203770927, 34.04911813557371],
          [-118.30404529698662, 34.04229075411085],
          [-118.30816517003349, 34.0317641308],
          [-118.31915149815849, 34.02180531193349],
          [-118.32910785802177, 34.009568591758196],
          [-118.33803424962333, 34.00216878905869],
          [-118.35005054601005, 33.99448369616034],
          [-118.35417041905693, 33.98793658719709],
          [-118.35691700108818, 33.977972627456566],
          [-118.35451374181083, 33.96715329163861],
          [-118.3473039639788, 33.97398671652878],
          [-118.33975086339287, 33.97825732822948],
          [-118.33288440831474, 33.97142424654421],
          [-118.33219776280693, 33.96259736999481],
          [-118.32842121251396, 33.95747166646383],
          [-118.32155475743583, 33.94721933297082],
          [-118.29546222813896, 33.93012936592257],
          [-118.28241596349052, 33.93098394574388],
          [-118.28481922276787, 33.95974979504903],
          [-118.28722248204521, 33.975694986950614],
          [-118.28310260899833, 33.99619155466418],
          [-118.28378925450615, 34.01554488475857],
          [-118.27726612218193, 34.030910563550755],
          [-118.2758928311663, 34.043144206854684],
          [-118.26559314854912, 34.05651384514719]]]),
    

    # shown: False #
m1 =ee.Geometry.MultiPolygon(
        [[[[-117.90945182386115, 34.13464195746244],
           [-117.91597495618537, 34.1269688699897],
           [-117.91940818372443, 34.113326105898054],
           [-117.9231847340174, 34.103945428893034],
           [-117.92833457532599, 34.091151920428416],
           [-117.93794761243537, 34.087739991568895],
           [-117.94790397229865, 34.083474887129995],
           [-117.94893394056037, 34.0760815305172],
           [-117.93279777112677, 34.0729533776579],
           [-117.89297233167365, 34.07579715775812],
           [-117.8685964161463, 34.077219012006076],
           [-117.84147391858771, 34.09570094500105],
           [-117.85005698743537, 34.10678816813197],
           [-117.8792394215174, 34.12924245000375],
           [-117.89949546399787, 34.13435778145877],
           [-117.90361533704474, 34.13435778145877]]],
         [[[-117.90052543225958, 34.06698112869948],
           [-117.95339713636115, 34.06811873238755],
           [-117.97605643811896, 34.06186172309322],
           [-117.98154960218146, 34.05531981030947],
           [-117.98120627942755, 34.05019970028177],
           [-117.95854697766974, 34.02943163984533],
           [-117.93829093518927, 34.029716168175256],
           [-117.92043815198615, 34.03170783976934],
           [-117.91700492444708, 34.044225847762355],
           [-117.90910850110724, 34.05048415895138],
           [-117.89812217298224, 34.05901747522991]]]]),
    

    # shown: False #
m2 =ee.Geometry.Polygon(
        [[[-118.38255775613507, 34.02693892877759],
          [-118.36470497293195, 34.02608531298771],
          [-118.35303199929913, 34.01840238449488],
          [-118.34067238015851, 34.013849209812925],
          [-118.33071602029523, 34.01470294866731],
          [-118.32110298318585, 34.022101659102894],
          [-118.31148994607648, 34.035190105372905],
          [-118.30634010476788, 34.04827653258291],
          [-118.30256355447492, 34.07103072622185],
          [-118.29947364968976, 34.08496465272491],
          [-118.29535377664288, 34.09008266221814],
          [-118.29157722634992, 34.093778809992315],
          [-118.29535377664288, 34.10060204340829],
          [-118.30222023172101, 34.10515056006909],
          [-118.31869972390851, 34.10458200885789],
          [-118.34513557595929, 34.100886332862714],
          [-118.36813820047101, 34.095200362316824],
          [-118.38564766092023, 34.08638635306226],
          [-118.38564766092023, 34.06704918333613],
          [-118.38599098367413, 34.04543182887494],
          [-118.39148414773663, 34.03632813572214],
          [-118.38255775613507, 34.03120687892459]]]),
    

    # shown: False #
m3 =ee.Geometry.Polygon(
        [[[-118.00001661281973, 33.79830485352807],
          [-117.9928068349877, 33.78946004926869],
          [-117.96602766018302, 33.77604844186381],
          [-117.95504133205802, 33.76120762069777],
          [-117.92070905666739, 33.76491806695484],
          [-117.90594617824942, 33.78232647700256],
          [-117.9210523794213, 33.79630771954105],
          [-117.93100873928458, 33.80714874389755],
          [-117.93444196682364, 33.82340770526481],
          [-117.94611494045645, 33.82854147201003],
          [-117.97739622925444, 33.83110823979],
          [-117.98185942505522, 33.84736264597988],
          [-117.99284575318022, 33.84850318997071],
          [-118.02408812378569, 33.851924730582475],
          [-118.03988097046538, 33.853920565984396],
          [-118.04743407105131, 33.84707750760304],
          [-118.04915068482084, 33.83424529575281],
          [-118.04571745728178, 33.81941456247701],
          [-118.03408158283916, 33.80955810921624],
          [-118.00146592121807, 33.80014387896518]]]),
    

    # shown: False #
l1 =ee.Geometry.MultiPolygon(
        [[[[-118.48443378736016, 34.17810841998755],
           [-118.48443378736016, 34.18606086536288],
           [-118.49130024243829, 34.185208853500036],
           [-118.49301685620782, 34.180380623728595],
           [-118.50091327954766, 34.180096601607346],
           [-118.50091327954766, 34.174699999645554],
           [-118.49851002027032, 34.16873493278088],
           [-118.49130024243829, 34.16617834649549],
           [-118.48443378736016, 34.16788274595598],
           [-118.48306049634454, 34.173563828937766]]],
         [[[-118.52940906812188, 34.145722868940716],
           [-118.52803577710625, 34.15140544304376],
           [-118.5304390363836, 34.15964449643355],
           [-118.53387226392266, 34.160212677381956],
           [-118.53970875073907, 34.15254191198994],
           [-118.55412830640313, 34.148848332004604],
           [-118.56030811597344, 34.14288143853796],
           [-118.55550159741875, 34.13890327543003],
           [-118.54348530103204, 34.14174483961915],
           [-118.53352894116875, 34.14089238039615]]],
         [[[-118.46349109937188, 34.14316558587859],
           [-118.4755073957586, 34.11474612208338],
           [-118.47344745923516, 34.104512776466926],
           [-118.46726764966485, 34.097405558170536],
           [-118.44117512036797, 34.09541543008285],
           [-118.40752949048516, 34.091150712322836],
           [-118.38590015698907, 34.09626834785047],
           [-118.34607471753594, 34.103944220970064],
           [-118.29903950025079, 34.1130406504484],
           [-118.27947010327813, 34.11758849838795],
           [-118.27603687573907, 34.1272518632453],
           [-118.28015674878594, 34.14288143853796],
           [-118.28221668530938, 34.14941658559222],
           [-118.28839649487969, 34.152257796187016],
           [-118.30247272778985, 34.152826026837104],
           [-118.32410206128594, 34.14913245927626],
           [-118.33543171216485, 34.14401802216676],
           [-118.34882129956719, 34.13890327543003],
           [-118.37560047437188, 34.13691412364091],
           [-118.39207996655938, 34.1374824575013],
           [-118.42160572339532, 34.14202899078229],
           [-118.44151844312188, 34.14373387769301],
           [-118.45456470777032, 34.14401802216676]]],
         [[[-117.64944359900842, 33.914439295937306],
           [-117.64532372596155, 33.898482627548965],
           [-117.63296410682092, 33.88936319038442],
           [-117.60275170447717, 33.90361188240773],
           [-117.5821523392428, 33.9321021228766],
           [-117.55193993689905, 33.94406518285044],
           [-117.52310082557092, 33.95659610934096],
           [-117.50799462439905, 33.96570835143804],
           [-117.51829430701623, 33.97197245165534],
           [-117.54713341834436, 33.95773519298094],
           [-117.56429955603967, 33.94805249596199],
           [-117.58833214881311, 33.93779902773546],
           [-117.60481164100061, 33.9212769536862],
           [-117.62266442420373, 33.921846733730405],
           [-117.63571068885217, 33.92013738216605],
           [-117.64051720740686, 33.933241534338904],
           [-117.66317650916467, 33.94919169397154]]]]),
    

    # shown: False #
l2 =ee.Geometry.Polygon(
        [[[-117.4540244735258, 34.17073013585037],
          [-117.4210654891508, 34.209352654413216],
          [-117.44715801844768, 34.23433426911617],
          [-117.59959332118206, 34.23546962101895],
          [-117.72044293055706, 34.23546962101895],
          [-117.95802227626018, 34.247957481463814],
          [-118.2120811141508, 34.300159365349295],
          [-118.29310528407268, 34.337588570489004],
          [-118.38923565516643, 34.38406826421415],
          [-118.49733723530682, 34.36479932465847],
          [-118.50969685444744, 34.33645459740481],
          [-118.38060749897869, 34.280871140716556],
          [-118.27623738179119, 34.26271347325806],
          [-118.11281575093182, 34.19231548826052],
          [-118.01805867085369, 34.169593911697405],
          [-117.87798298725994, 34.145729671558264],
          [-117.78322590718182, 34.12754286722135],
          [-117.72142781147869, 34.1400467156479],
          [-117.61568440327557, 34.16050356785007],
          [-117.48522175679119, 34.17413871653288]]]),
    

    # shown: False #
l3 =ee.Geometry.MultiPolygon(
        [[[[-117.55561836001202, 34.37119572144761],
           [-117.5129581444115, 34.36546773603748],
           [-117.47571205972473, 34.35625664382891],
           [-117.4577364904716, 34.353923978383015],
           [-117.43148604108059, 34.36525294015388],
           [-117.40377339620349, 34.360730022179474],
           [-117.38465055156425, 34.355132762987616],
           [-117.36833407142767, 34.35180585137804],
           [-117.34096756260226, 34.377935273653954],
           [-117.32584038940462, 34.40414472996622],
           [-117.2955482149152, 34.462060585188624],
           [-117.27627097641101, 34.50745695726056],
           [-117.35199793540723, 34.54829417289688],
           [-117.61360402822571, 34.57777557264372],
           [-117.74440745975625, 34.583442506079734],
           [-117.9027477675407, 34.565300257015586],
           [-117.91513832801677, 34.52900956529933],
           [-117.89035362284346, 34.498377930297906],
           [-117.86694650094347, 34.485895452908714],
           [-117.81875608443413, 34.480221706940135],
           [-117.76230439601888, 34.46773693904351],
           [-117.67969225054195, 34.437083357297496],
           [-117.61773335043686, 34.39846588656781],
           [-117.56816658242518, 34.37460498052803]]],
         [[[-117.85349781249015, 35.01796237172381],
           [-117.93589527342765, 34.914425718967166],
           [-117.92490894530265, 34.83330581806112],
           [-117.81504566405265, 34.8197780544419],
           [-117.74912769530265, 34.93244149086589],
           [-117.78757984374015, 34.99546553534098]]],
         [[[-114.99155933592765, 34.27231052887144],
           [-114.95310718749015, 34.21327776941665],
           [-114.90366871092765, 34.15420362550665],
           [-114.75535328124015, 34.18601792032351],
           [-114.82127124999015, 34.317692161685365],
           [-114.92014820311515, 34.353979812123676]]],
         [[[-115.82449864289129, 34.91172959491243],
           [-116.18704747101629, 35.04675586521774],
           [-116.32986973664129, 34.99277207560532],
           [-116.69791172882879, 34.83511594097305],
           [-116.75833653351629, 34.60484710078991],
           [-116.32437657257879, 34.49626361404928],
           [-115.91788243195379, 34.32405026332289],
           [-115.74210118195379, 34.22418587837304],
           [-115.53885411164129, 34.44191876007722],
           [-115.57181309601629, 34.758430926524255],
           [-115.69815586945379, 34.88920357911809]]]]),
    

    # shown: False #
high1 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-118.16521474530495, 34.09395855498055]),
            {
              "EM": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.12538930585183, 34.095664411282506]),
            {
              "EM": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.19954702069558, 34.08486007409962]),
            {
              "EM": 1,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.22426625897683, 34.05642101989352]),
            {
              "EM": 1,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.22975942303933, 34.032524838047685]),
            {
              "EM": 1,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.21396657635964, 34.00065278987936]),
            {
              "EM": 1,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.17551442792214, 33.987559018245335]),
            {
              "EM": 1,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.13706227948464, 33.9921136024666]),
            {
              "EM": 1,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.09586354901589, 33.995529380427215]),
            {
              "EM": 1,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.07801076581276, 34.00520667220255]),
            {
              "EM": 1,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.06221791913308, 34.0416289393942]),
            {
              "EM": 1,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.04367849042214, 34.06495373852361]),
            {
              "EM": 1,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.07045766522683, 34.08827211901885]),
            {
              "EM": 1,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.09929677655495, 34.08656611374699]),
            {
              "EM": 1,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.1679613273362, 34.07462311437623]),
            {
              "EM": 1,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.13843557050026, 34.08144789168173]),
            {
              "EM": 1,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.18512746503151, 34.060403062161306]),
            {
              "EM": 1,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.18512746503151, 34.038215015895354]),
            {
              "EM": 1,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.13980886151589, 34.025127036267754]),
            {
              "EM": 1,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.0965501945237, 34.05755876534563]),
            {
              "EM": 1,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.13568898846901, 34.0706417403238]),
            {
              "EM": 1,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.14667531659401, 34.06666017915766]),
            {
              "EM": 1,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.12607595135964, 34.05186988537208]),
            {
              "EM": 1,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.10616323163308, 34.03081771026821]),
            {
              "EM": 1,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.08075734784401, 34.046180623634235]),
            {
              "EM": 1,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.16315480878151, 34.022850659812015]),
            {
              "EM": 1,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.15628835370339, 34.05471437308128]),
            {
              "EM": 1,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.18650075604714, 34.022850659812015]),
            {
              "EM": 1,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.20298024823464, 33.986420334047516]),
            {
              "EM": 1,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.22426625897683, 33.98528163459319]),
            {
              "EM": 1,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.23868581464089, 34.01659030973752]),
            {
              "EM": 1,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.20298024823464, 34.034800954987745]),
            {
              "EM": 1,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.20710012128151, 34.06552255588668]),
            {
              "EM": 1,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.0306322257737, 34.06154075416109]),
            {
              "EM": 1,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.12264272382058, 34.01715945155094]),
            {
              "EM": 1,
              "system:index": "34"
            })]),
    

    # shown: False #
high2 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-118.07251760175026, 34.122953435897294]),
            {
              "EM": 2,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.04779836346901, 34.11783741434344]),
            {
              "EM": 2,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.99424001385964, 34.100213193339606]),
            {
              "EM": 2,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.95990773846901, 34.08486007409962]),
            {
              "EM": 2,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.98394033124245, 34.07860430130452]),
            {
              "EM": 2,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.02376577069558, 34.109878543393485]),
            {
              "EM": 2,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.98874684979714, 34.05755876534563]),
            {
              "EM": 2,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.95647451092995, 34.06950417051197]),
            {
              "EM": 2,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.96883413007058, 34.04504272547766]),
            {
              "EM": 2,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.99561330487526, 34.033662904151036]),
            {
              "EM": 2,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.01209279706276, 34.02569612084125]),
            {
              "EM": 2,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.9702074210862, 34.03195579927109]),
            {
              "EM": 2,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.94617482831276, 34.05585214144062]),
            {
              "EM": 2,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.02719899823464, 34.013175378727404]),
            {
              "EM": 2,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.05466481854714, 33.96762984230817]),
            {
              "EM": 2,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.10135671307839, 33.95567009455051]),
            {
              "EM": 2,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.15354177167214, 33.94940479376017]),
            {
              "EM": 2,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.15354177167214, 33.92319944776905]),
            {
              "EM": 2,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.12195607831276, 33.94598716254419]),
            {
              "EM": 2,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.27713796307839, 34.00577589032515]),
            {
              "EM": 2,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.28194448163308, 33.9847122791449]),
            {
              "EM": 2,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.25997182538308, 33.9613654222336]),
            {
              "EM": 2,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.27027150800026, 33.977310311251266]),
            {
              "EM": 2,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.24211904217995, 33.94883519808764]),
            {
              "EM": 2,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.20778676678933, 33.9465567772769]),
            {
              "EM": 2,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.19886037518776, 33.92319944776905]),
            {
              "EM": 2,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.18512746503151, 33.90895402970548]),
            {
              "EM": 2,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.11920949628151, 33.93915148842878]),
            {
              "EM": 2,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.07045766522683, 33.94029080556519]),
            {
              "EM": 2,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.09243032147683, 33.95111355790481]),
            {
              "EM": 2,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.10890981366433, 33.93003640249109]),
            {
              "EM": 2,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.13362905194558, 33.91807137161228]),
            {
              "EM": 2,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.17551442792214, 33.94313903170209]),
            {
              "EM": 2,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.05672475507058, 33.93003640249109]),
            {
              "EM": 2,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.03818532635964, 33.99894502106158]),
            {
              "EM": 2,
              "system:index": "34"
            })]),
    

    # shown: False #
high3 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-118.32520314862526, 33.98357355680628]),
            {
              "EM": 3,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.33206960370339, 33.96762984230817]),
            {
              "EM": 3,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.30391713788308, 33.95396142190105]),
            {
              "EM": 3,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.28675100018776, 34.04788744223904]),
            {
              "EM": 3,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.27919789960183, 34.09395855498055]),
            {
              "EM": 3,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.22975942303933, 34.13034269833698]),
            {
              "EM": 3,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.18581411053933, 34.137731314887176]),
            {
              "EM": 3,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.13912221600808, 34.149097155914845]),
            {
              "EM": 3,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.10478994061745, 34.137162982700424]),
            {
              "EM": 3,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.04436513592995, 34.13943628851394]),
            {
              "EM": 3,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.01003286053933, 34.13602630686037]),
            {
              "EM": 3,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.98325368573464, 34.12920593076935]),
            {
              "EM": 3,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.9537279288987, 34.12465870763045]),
            {
              "EM": 3,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.94136830975808, 34.11385807248182]),
            {
              "EM": 3,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.97158071210183, 34.12579553634495]),
            {
              "EM": 3,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.91115590741433, 34.08258530109826]),
            {
              "EM": 3,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.91733571698464, 34.03650800261722]),
            {
              "EM": 3,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.92832204510964, 34.0154520146635]),
            {
              "EM": 3,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.95853444745339, 34.007483521801795]),
            {
              "EM": 3,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.99424001385964, 33.995529380427215]),
            {
              "EM": 3,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.0086595695237, 33.990405661991026]),
            {
              "EM": 3,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.0251390617112, 33.92490873789627]),
            {
              "EM": 3,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.21808644940651, 33.84909727662716]),
            {
              "EM": 3,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.21396657635964, 33.82514282214345]),
            {
              "EM": 3,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.18238088300026, 33.84795674056762]),
            {
              "EM": 3,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.23319265057839, 33.900405635854305]),
            {
              "EM": 3,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.23731252362526, 33.85023779745995]),
            {
              "EM": 3,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.07663747479714, 33.900405635854305]),
            {
              "EM": 3,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.09723684003151, 33.89356630363311]),
            {
              "EM": 3,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.12332936932839, 33.87874586886039]),
            {
              "EM": 3,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.28125783612526, 33.93915148842878]),
            {
              "EM": 3,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.23456594159401, 33.82400196637973]),
            {
              "EM": 3,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.21121999432839, 33.81259257161392]),
            {
              "EM": 3,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.23044606854714, 33.8091694564067]),
            {
              "EM": 3,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.15354177167214, 33.86164216826209]),
            {
              "EM": 3,
              "system:index": "34"
            })]),
    

    # shown: False #
med1 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.97089406659401, 33.95168313832862]),
            {
              "EM": 4,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.94068166425026, 33.90724441951083]),
            {
              "EM": 4,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.98874684979714, 33.898125919396215]),
            {
              "EM": 4,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.02994558026589, 33.87646557346064]),
            {
              "EM": 4,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.93106862714089, 33.972185494386245]),
            {
              "EM": 4,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.89124318768776, 34.007483521801795]),
            {
              "EM": 4,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.87339040448464, 34.07803557177176]),
            {
              "EM": 4,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.86240407635964, 34.03593899055751]),
            {
              "EM": 4,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.85553762128151, 34.07689810124911]),
            {
              "EM": 4,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.96265432050026, 33.9049648859136]),
            {
              "EM": 4,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.94617482831276, 33.95737873288775]),
            {
              "EM": 4,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.29087087323464, 34.168983698096035]),
            {
              "EM": 4,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.27439138104714, 34.14625583900454]),
            {
              "EM": 4,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.30872365643776, 34.09168402643289]),
            {
              "EM": 4,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.32245656659401, 34.06210959443375]),
            {
              "EM": 4,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.32108327557839, 34.04504272547766]),
            {
              "EM": 4,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.36914846112526, 33.99723721791058]),
            {
              "EM": 4,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.39249440839089, 33.968768778206986]),
            {
              "EM": 4,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.37052175214089, 33.94940479376017]),
            {
              "EM": 4,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.34717580487526, 33.93231526544644]),
            {
              "EM": 4,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.31970998456276, 33.920920340916275]),
            {
              "EM": 4,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.28949758221901, 33.9049648859136]),
            {
              "EM": 4,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.27027150800026, 33.87646557346064]),
            {
              "EM": 4,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.27027150800026, 33.85023779745995]),
            {
              "EM": 4,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.26615163495339, 33.80460508974589]),
            {
              "EM": 4,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.25241872479714, 33.78520381539114]),
            {
              "EM": 4,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.22357961346901, 33.77264770678731]),
            {
              "EM": 4,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.18512746503151, 33.78976921669942]),
            {
              "EM": 4,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.14942189862526, 33.826283662685654]),
            {
              "EM": 4,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.10135671307839, 33.85822101691968]),
            {
              "EM": 4,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.57950612714089, 34.09964460895295]),
            {
              "EM": 4,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.53556081464089, 34.07803557177176]),
            {
              "EM": 4,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.56851979901589, 34.068935379878155]),
            {
              "EM": 4,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.48200246503151, 34.09623302240991]),
            {
              "EM": 4,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.51770803143776, 34.07121051950177]),
            {
              "EM": 4,
              "system:index": "34"
            })]),
    

    # shown: False #
med2 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.77039357831276, 34.068935379878155]),
            {
              "EM": 5,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.70996877362526, 34.06666017915766]),
            {
              "EM": 5,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.40509816815651, 34.13375290931493]),
            {
              "EM": 5,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.36801931073464, 34.10305605796891]),
            {
              "EM": 5,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.37076589276589, 34.07917302701823]),
            {
              "EM": 5,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.75391408612526, 34.06324726352448]),
            {
              "EM": 5,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.67563649823464, 34.05528325916988]),
            {
              "EM": 5,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.38837453534401, 34.26664375104922]),
            {
              "EM": 5,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.39661428143776, 34.23372452394967]),
            {
              "EM": 5,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.34442922284401, 34.222370080735196]),
            {
              "EM": 5,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.34854909589089, 34.18261747693201]),
            {
              "EM": 5,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.33206960370339, 34.149665407828515]),
            {
              "EM": 5,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.35266896893776, 34.09737023320463]),
            {
              "EM": 5,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.36914846112526, 34.05414548317493]),
            {
              "EM": 5,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.42957326581276, 33.973324369272795]),
            {
              "EM": 5,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.43094655682839, 33.942569394098165]),
            {
              "EM": 5,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.38150808026589, 33.916361944304406]),
            {
              "EM": 5,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.34854909589089, 33.89926578524409]),
            {
              "EM": 5,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.32108327557839, 33.870764568393234]),
            {
              "EM": 5,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.30048391034401, 33.82514282214345]),
            {
              "EM": 5,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.87201711346901, 33.86506318253921]),
            {
              "EM": 5,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.88986989667214, 33.920920340916275]),
            {
              "EM": 5,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.88712331464089, 33.96990769885311]),
            {
              "EM": 5,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.84043142010964, 34.006345104632565]),
            {
              "EM": 5,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.80884572675026, 34.04845637413915]),
            {
              "EM": 5,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.73331472089089, 34.04959422648694]),
            {
              "EM": 5,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.81571218182839, 34.115563527634556]),
            {
              "EM": 5,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.57813283612526, 34.141709533170435]),
            {
              "EM": 5,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.40372487714089, 34.115563527634556]),
            {
              "EM": 5,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.40097829510964, 34.07234806640163]),
            {
              "EM": 5,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.31446096112526, 34.10646736945126]),
            {
              "EM": 5,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33506032635964, 34.07803557177176]),
            {
              "EM": 5,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.42432424237526, 34.0473185065215]),
            {
              "EM": 5,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.05603810956276, 33.83312838627298]),
            {
              "EM": 5,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.94617482831276, 33.859361415929556]),
            {
              "EM": 5,
              "system:index": "34"
            })]),
    

    # shown: False #
med3 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.39960500409401, 34.20306401448202]),
            {
              "EM": 6,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.32407399823464, 34.17807312874091]),
            {
              "EM": 6,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.76078054120339, 34.14511928548147]),
            {
              "EM": 6,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.64267751385964, 34.157620533206426]),
            {
              "EM": 6,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.48337575604714, 34.175800862859646]),
            {
              "EM": 6,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.17850515057839, 34.09623302240991]),
            {
              "EM": 6,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.20185109784401, 34.059834210434246]),
            {
              "EM": 6,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.27600881268776, 34.03707701086013]),
            {
              "EM": 6,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.35977956464089, 34.02000510338066]),
            {
              "EM": 6,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.50260183026589, 33.9778797162796]),
            {
              "EM": 6,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.59598561932839, 33.9778797162796]),
            {
              "EM": 6,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.54654714276589, 33.95168313832862]),
            {
              "EM": 6,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.64542409589089, 33.97446322890563]),
            {
              "EM": 6,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.59873220135964, 33.93801215604603]),
            {
              "EM": 6,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.69623586346901, 33.9778797162796]),
            {
              "EM": 6,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.77451345135964, 33.988128354622965]),
            {
              "EM": 6,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.74842092206276, 33.972185494386245]),
            {
              "EM": 6,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.81983205487526, 33.956239644475424]),
            {
              "EM": 6,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.78961965253151, 33.91978076462623]),
            {
              "EM": 6,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.77176686932839, 33.86734378257322]),
            {
              "EM": 6,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.79648610760964, 33.82172020918876]),
            {
              "EM": 6,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.48587819745339, 34.2473478349685]),
            {
              "EM": 6,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.49137136151589, 34.21669228510694]),
            {
              "EM": 6,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.45841237714089, 34.190569497267916]),
            {
              "EM": 6,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.41172048260964, 34.141709533170435]),
            {
              "EM": 6,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.48175832440651, 34.024557947878066]),
            {
              "EM": 6,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.52295705487526, 33.9847122791449]),
            {
              "EM": 6,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.49686452557839, 33.97446322890563]),
            {
              "EM": 6,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.49137136151589, 33.95282228773945]),
            {
              "EM": 6,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.53119680096901, 33.960795906622266]),
            {
              "EM": 6,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.51471730878151, 33.9243389783313]),
            {
              "EM": 6,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.47489186932839, 33.91180330383066]),
            {
              "EM": 6,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.41309377362526, 33.87874586886039]),
            {
              "EM": 6,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.36914846112526, 33.85594017321399]),
            {
              "EM": 6,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.35953542401589, 33.817156512159514]),
            {
              "EM": 6,
              "system:index": "34"
            })]),
    

    # shown: False #
low1 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.13593312909401, 34.05300769190891]),
            {
              "EM": 7,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.18949147870339, 34.01886685409635]),
            {
              "EM": 7,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.24304982831276, 33.947126388197624]),
            {
              "EM": 7,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.29248830487526, 33.95282228773945]),
            {
              "EM": 7,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.41471120526589, 33.943708665494206]),
            {
              "EM": 7,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.42707082440651, 33.89128640433201]),
            {
              "EM": 7,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.47925588300026, 33.85822101691968]),
            {
              "EM": 7,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.48062917401589, 33.827424488006095]),
            {
              "EM": 7,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.62345143964089, 33.859361415929556]),
            {
              "EM": 7,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.73056813885964, 33.92205990196396]),
            {
              "EM": 7,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.68387624432839, 33.87874586886039]),
            {
              "EM": 7,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.47650930096901, 33.79205182607191]),
            {
              "EM": 7,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.51908132245339, 33.853659268595344]),
            {
              "EM": 7,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.56415578534401, 34.242806976268646]),
            {
              "EM": 7,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.55866262128151, 34.201928225789665]),
            {
              "EM": 7,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.52021047284401, 34.1769370034489]),
            {
              "EM": 7,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.48999807050026, 34.13829964325169]),
            {
              "EM": 7,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.48725148846901, 34.115563527634556]),
            {
              "EM": 7,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.00110646893776, 33.68470343370605]),
            {
              "EM": 7,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.92694875409401, 33.67556119957868]),
            {
              "EM": 7,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.86103078534401, 33.670989717979694]),
            {
              "EM": 7,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.72095510175026, 33.65041504386873]),
            {
              "EM": 7,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.70722219159401, 33.74410425233921]),
            {
              "EM": 7,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.71820851971901, 33.80802838756791]),
            {
              "EM": 7,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.68250295331276, 33.85822101691968]),
            {
              "EM": 7,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.36664601971901, 33.91978076462623]),
            {
              "EM": 7,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.27600881268776, 33.91978076462623]),
            {
              "EM": 7,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.31995412518776, 33.903825096256476]),
            {
              "EM": 7,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.55066701581276, 33.84453504103104]),
            {
              "EM": 7,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.13043996503151, 34.0154520146635]),
            {
              "EM": 7,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.54218312909401, 34.167847450433]),
            {
              "EM": 7,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.51770803143776, 33.820579307761975]),
            {
              "EM": 7,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.37351247479714, 33.8958461419885]),
            {
              "EM": 7,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.20871755292214, 33.99609866340298]),
            {
              "EM": 7,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.69898244550026, 33.70869717240253]),
            {
              "EM": 7,
              "system:index": "34"
            })]),
    

    # shown: False #
low2 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.05765554120339, 34.03138675667793]),
            {
              "EM": 8,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.65366384198464, 33.79775808324881]),
            {
              "EM": 8,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.65366384198464, 33.76922299410717]),
            {
              "EM": 8,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.60834523846901, 33.80460508974589]),
            {
              "EM": 8,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.42707082440651, 33.725831454414234]),
            {
              "EM": 8,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.38312551190651, 33.788627889192405]),
            {
              "EM": 8,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.26639577557839, 33.82856529810449]),
            {
              "EM": 8,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.15378591229714, 33.9049648859136]),
            {
              "EM": 8,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.08237477948464, 33.97104660424627]),
            {
              "EM": 8,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.17987844159401, 33.88786644111155]),
            {
              "EM": 8,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.20871755292214, 33.82400196637973]),
            {
              "EM": 8,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.31720754315651, 33.82856529810449]),
            {
              "EM": 8,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33448530259628, 33.82435589444638]),
            {
              "EM": 8,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.5171330076744, 33.75245160299435]),
            {
              "EM": 8,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.10377241197128, 33.95317568171835]),
            {
              "EM": 8,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.6544621092369, 33.73760669589622]),
            {
              "EM": 8,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.72724653306503, 34.19319375948006]),
            {
              "EM": 8,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.64072919908065, 34.197737293109505]),
            {
              "EM": 8,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.19990278306503, 33.87339874106174]),
            {
              "EM": 8,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.10377241197128, 34.12387454713847]),
            {
              "EM": 8,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.08179975572128, 34.095448598373586]),
            {
              "EM": 8,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.32715016486135, 34.347398578738606]),
            {
              "EM": 8,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.29075795294729, 34.33719346282604]),
            {
              "EM": 8,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.23925953986135, 34.31280954850456]),
            {
              "EM": 8,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.20698720099416, 34.28955317192498]),
            {
              "EM": 8,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.14930897833791, 34.253237666469545]),
            {
              "EM": 8,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.06210499884573, 34.23450635622797]),
            {
              "EM": 8,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.98039418341604, 34.21860985469886]),
            {
              "EM": 8,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.8904436218926, 34.21520307118776]),
            {
              "EM": 8,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.84512501837698, 34.21520307118776]),
            {
              "EM": 8,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.7970598328301, 34.19873500913905]),
            {
              "EM": 8,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.45940619186017, 34.432271737777945]),
            {
              "EM": 8,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.46215277389142, 34.396017998840165]),
            {
              "EM": 8,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.53356390670392, 34.41414683272016]),
            {
              "EM": 8,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-118.57476263717267, 34.096325880280375]),
            {
              "EM": 8,
              "system:index": "34"
            })]),
    

    # shown: False #
low3 =ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-117.23168402389142, 34.289431807207905]),
            {
              "EM": 9,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.04766302779767, 34.30077720201626]),
            {
              "EM": 9,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.94603949264142, 34.18725433834185]),
            {
              "EM": 9,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.09160834029767, 34.2463053362671]),
            {
              "EM": 9,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.93505316451642, 34.29397014899583]),
            {
              "EM": 9,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.83068304732892, 33.95519355324181]),
            {
              "EM": 9,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.69060736373517, 33.957471742826]),
            {
              "EM": 9,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.54778509811017, 33.96202793898928]),
            {
              "EM": 9,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.49834662154767, 33.84804986995575]),
            {
              "EM": 9,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.45141058639142, 33.63793256792782]),
            {
              "EM": 9,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.39647894576642, 33.56243908595215]),
            {
              "EM": 9,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.27837591842267, 33.54641682301761]),
            {
              "EM": 9,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.33605414107892, 33.55099491565639]),
            {
              "EM": 9,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.21245794967267, 33.52581240471753]),
            {
              "EM": 9,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.05864935592267, 33.55786159978141]),
            {
              "EM": 9,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.99547796920392, 33.69279538935045]),
            {
              "EM": 9,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.93230658248517, 33.61734999129322]),
            {
              "EM": 9,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.85540228561017, 33.834362264563836]),
            {
              "EM": 9,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.94054632857892, 33.95063699107811]),
            {
              "EM": 9,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.00097113326642, 34.191798191970875]),
            {
              "EM": 9,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.94329291061017, 34.1190671676841]),
            {
              "EM": 9,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.86913519576642, 34.06675306946087]),
            {
              "EM": 9,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.78124457076642, 34.04399772729431]),
            {
              "EM": 9,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.35253363326642, 34.31665818037703]),
            {
              "EM": 9,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.14379339889142, 34.24403490941743]),
            {
              "EM": 9,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.92132025436017, 33.88225928979047]),
            {
              "EM": 9,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.73729925826642, 33.93468710226146]),
            {
              "EM": 9,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.59722357467267, 33.92557153844745]),
            {
              "EM": 9,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.89110785201642, 33.76817460916402]),
            {
              "EM": 9,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.02019720748517, 33.66536835231576]),
            {
              "EM": 9,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.97625189498517, 33.56930486029843]),
            {
              "EM": 9,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-117.10259466842267, 33.528102027040745]),
            {
              "EM": 9,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.82244330123517, 33.76817460916402]),
            {
              "EM": 9,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.88286810592267, 33.72021367553803]),
            {
              "EM": 9,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-116.57250433639142, 33.86173528272919]),
            {
              "EM": 9,
              "system:index": "34"
            })]),
    

geometry2 =ee.Geometry.Polygon(
        [[[-121.5671875, 36.4784571222803],
          [-121.5671875, 31.451813558136784],
          [-114.5359375, 31.451813558136784],
          [-114.5359375, 36.4784571222803]]], {}, False),
l7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_RT"),
    

    # shown: False #
h1V =ee.Geometry.Polygon(
        [[[-118.12315409229599, 34.0046239353184],
          [-118.14375205776292, 34.00747000538305],
          [-118.1705297961632, 34.01486894818309],
          [-118.18494857805332, 34.01600718986854],
          [-118.20348701185003, 34.016576305314715],
          [-118.21515935880453, 34.020560005138954],
          [-118.22683170507739, 34.030233925785204],
          [-118.23713083468115, 34.03023392647269],
          [-118.24674335636749, 34.024543519619996],
          [-118.25223622743864, 34.01088498477302],
          [-118.2453701429585, 33.99323945651773],
          [-118.22408486991344, 33.9864083410898],
          [-118.20348694020218, 33.99452171247897],
          [-118.19593417290587, 33.99580304042733],
          [-118.18323072359769, 33.99281446405596],
          [-118.1629770994447, 33.9807145976344],
          [-118.14993406215157, 33.97673965005114],
          [-118.13619935979742, 33.98071459890872],
          [-118.12933327333508, 33.98640794487879],
          [-118.11972075218428, 33.991531630477425],
          [-118.11903425516226, 34.000070388227506]]]),
   

    # shown: False #
h2V =ee.Geometry.Polygon(
        [[[-118.21790638533626, 33.94739955880231],
          [-118.21515980330501, 33.954234570566854],
          [-118.21927967635189, 33.965340293779995],
          [-118.23781910506283, 33.975021023352376],
          [-118.24228230086361, 33.97188914320345],
          [-118.24502888289486, 33.96761821164624],
          [-118.26013508406673, 33.9701807963199],
          [-118.28210774031673, 33.97245858453796],
          [-118.28451099959408, 33.96647926033921],
          [-118.27558460799251, 33.95451935081036],
          [-118.25704517928158, 33.940279171165884],
          [-118.24434223738704, 33.94569072008863],
          [-118.23472920027767, 33.94739955880231]]]),
    

    # shown: False #
h3V =ee.Geometry.Polygon(
        [[[-118.2529208593583, 33.88166698431145],
          [-118.20725893308877, 33.87967179747078],
          [-118.20004915525674, 33.87596632671058],
          [-118.19318270017861, 33.877106488696946],
          [-118.18837618162392, 33.890787244300476],
          [-118.1873462133622, 33.900761412159085],
          [-118.18494295408486, 33.90788510350155],
          [-118.19386934568642, 33.914723287138315],
          [-118.20588564207314, 33.92184581164747],
          [-118.21618532469033, 33.92611904055889],
          [-118.21652864744424, 33.914438373774225],
          [-118.21584200193642, 33.90532064319299],
          [-118.22270845701455, 33.91044948665997],
          [-118.22751497556924, 33.92213070024366],
          [-118.23266481687783, 33.92497953380844],
          [-118.24845766355752, 33.92554928908907],
          [-118.26013063719033, 33.92469465473905],
          [-118.27283357908486, 33.92355512893459],
          [-118.27386354734658, 33.91899687328991],
          [-118.26081728269814, 33.91130426390115],
          [-118.25086092283486, 33.91158918774318],
          [-118.24536775877236, 33.90161628654971]]]),
    

    # shown: False #
m1V =ee.Geometry.Polygon(
        [[[-118.18539932196292, 33.871662993734425],
          [-118.19363906805667, 33.86339594702789],
          [-118.19913223211917, 33.85313229261573],
          [-118.2005055231348, 33.84229709705674],
          [-118.20187881415042, 33.82204870759585],
          [-118.20256545965823, 33.80550421084021],
          [-118.2011921686426, 33.789241846871064],
          [-118.18917587225589, 33.78553245400296],
          [-118.17509963934573, 33.78724450144794],
          [-118.16411331122073, 33.790383166194154],
          [-118.16342666571292, 33.79751606726332],
          [-118.1785328668848, 33.80350724484677],
          [-118.17715957586917, 33.816058828311746],
          [-118.17063644354495, 33.818911204099734],
          [-118.1678898615137, 33.82889377021504],
          [-118.16685989325198, 33.84001582815719],
          [-118.16960647528323, 33.85854937504858],
          [-118.17544296209964, 33.870237697970076],
          [-118.18265273993167, 33.8713779364855]]]),
    

    # shown: False #
m2V =ee.Geometry.Polygon(
        [[[-118.32762611551007, 33.91418744363343],
          [-118.34719551248273, 33.91475727108693],
          [-118.34822548074445, 33.92472863471067],
          [-118.35543525857648, 33.93042603280766],
          [-118.36092842263898, 33.928716853393745],
          [-118.36642158670148, 33.922164681238],
          [-118.36813820047101, 33.90934375644399],
          [-118.35612190408429, 33.89851569563747],
          [-118.35303199929913, 33.890536244539526],
          [-118.34067238015851, 33.88968125907004],
          [-118.32625282449445, 33.887401255920466],
          [-118.32419288797101, 33.87942076500487],
          [-118.31148994607648, 33.87001422815947],
          [-118.29672706765851, 33.87257975011629],
          [-118.29226387185773, 33.88255604688914],
          [-118.29672706765851, 33.891961201277276],
          [-118.31526649636945, 33.8948110433332],
          [-118.3238495652171, 33.90108036064355],
          [-118.32419288797101, 33.911908095717486]]]),
    

    # shown: False #
m3V =ee.Geometry.Polygon(
        [[[-117.96755468062257, 33.75991859655252],
          [-117.97716771773194, 33.766197813631244],
          [-117.99605046919679, 33.769337249650526],
          [-118.01115667036866, 33.771905793568784],
          [-118.02488958052491, 33.771049620818104],
          [-118.02042638472413, 33.762202001445004],
          [-118.00944005659913, 33.75592249162228],
          [-117.99570714644288, 33.75335346865752],
          [-117.98884069136476, 33.751926200414225],
          [-117.98643743208741, 33.74222014630825],
          [-117.98472081831788, 33.73508264103096],
          [-117.98609410933351, 33.72052028901694],
          [-117.98815404585694, 33.705669856833225],
          [-117.9802576225171, 33.68967421181909],
          [-117.9637781303296, 33.68367507724325],
          [-117.95862828902101, 33.68995987445008],
          [-117.96034490279054, 33.715094467332825],
          [-117.9582849662671, 33.731370903605544],
          [-117.95416509322023, 33.74364757610003],
          [-117.9637781303296, 33.75849143760491]]]),
    

    # shown: False #
l1V =ee.Geometry.MultiPolygon(
        [[[[-117.4361100002296, 33.85458639213786],
           [-117.45602271995617, 33.85116495813941],
           [-117.46082923851085, 33.839188859961254],
           [-117.44434974632335, 33.833485366096546],
           [-117.42443702659679, 33.83006308709565],
           [-117.41070411644054, 33.830633476443445],
           [-117.42443702659679, 33.84660283296183],
           [-117.4306168361671, 33.85344592936598]]],
         [[[-117.16557167015148, 33.84603255018483],
           [-117.15115211448742, 33.86028847757316],
           [-117.1504654689796, 33.872261617675306],
           [-117.15527198753429, 33.87625229121135],
           [-117.17999122581554, 33.86542002894196],
           [-117.19235084495617, 33.86142884897363],
           [-117.19509742698742, 33.854016162655405],
           [-117.18617103538585, 33.84831365845339],
           [-117.1779312892921, 33.843751381011984]]],
         [[[-117.00989140400799, 34.005746694441434],
           [-117.03083409199627, 34.00048127942884],
           [-117.04182042012127, 33.99108810710576],
           [-117.04971684346111, 33.98112451683704],
           [-117.03787220845135, 33.978135211991074],
           [-117.01452626118572, 33.97941635551078],
           [-116.99839009175213, 33.98126686206486],
           [-116.98912037739666, 33.987387481361225],
           [-116.98036564717205, 33.996923381797544],
           [-116.99066532978924, 34.00133515268661],
           [-117.00096501240643, 34.006458211974206]]]]),
    

    # shown: False #
l2V =ee.Geometry.Polygon(
        [[[-118.54029766688518, 34.35006126251562],
          [-118.64878765711956, 34.38860148807788],
          [-118.70371929774456, 34.392001244889116],
          [-118.73805157313518, 34.39993347378834],
          [-118.76963726649456, 34.39086800796074],
          [-118.77925030360393, 34.379534794899],
          [-118.72569195399456, 34.35686376708072],
          [-118.6790000594633, 34.347793638322365],
          [-118.61033550868206, 34.322845724660866],
          [-118.53205792079143, 34.31717470955658]]]),
    

    # shown: False #
l3V =ee.Geometry.Polygon(
        [[[-117.2566685987405, 34.523132861070664],
          [-117.24636891612332, 34.49484178498379],
          [-117.23332265147488, 34.46484276064553],
          [-117.2127232862405, 34.432567622715474],
          [-117.14704281706369, 34.42727450839223],
          [-117.09417111296213, 34.41594622603601],
          [-116.99718847115729, 34.37798529903318],
          [-116.9594229682276, 34.37231801239544],
          [-116.94431676705572, 34.38421887140701],
          [-116.95598974068854, 34.4153797716295],
          [-117.00268163521979, 34.4357697128492],
          [-117.04800023873541, 34.44596281834416],
          [-117.12765111764166, 34.475402581081084],
          [-117.1461905463526, 34.513319274691156],
          [-117.15511693795416, 34.545563183504974],
          [-117.1791495307276, 34.577229248852646],
          [-117.22378148873541, 34.598710068947376],
          [-117.26360692818854, 34.60266645638776],
          [-117.29587926705572, 34.597014416635986],
          [-117.31510534127447, 34.58627448151772],
          [-117.27184667428229, 34.54330086041216]]]),
    

    # shown: False #
geom1 =ee.Geometry.Polygon(
        [[[-114.87333335488508, 34.665387037041974],
          [-118.98222007363508, 35.42093297399078],
          [-119.59745444863508, 33.00461405308321],
          [-115.62040366738508, 32.19012224993344]]])
