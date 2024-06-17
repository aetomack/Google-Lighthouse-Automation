import os
sites = [r'http://www.olaparishpa.org/',
         r'http://www.faysouth.org/',
         r'http://www.sevendolors.org/',
         r'http://www.partnerparishesmas.org/',
         r'http://www.stannerostraver.org/',
         r'http://stbarbarahc.wpenginepowered.com/',
         r'http://www.stbartholomewcrabtree.org/',
         r'http://www.saintbernardparish.org/',
         r'http://www.saint-edward.org/',
         r'http://www.saintflorian.org/',
         r'http://www.sfoafayette.org/',
         r'http://www.sgcatholic.org/',
         r'http://www.sjoafarmington.org/',
         r'http://www.sjbperry.org/',
         r'http://www.stjohnsandstjosephs.org/',
         r'http://www.stmartinstjoseph.org/',
         r'http://www.saintmaryyatesboro.org/',
         r'http://www.stmarykittanning.org/',
         r'http://www.stpatrickbradysbend.org/',
         r'http://www.pbcatholic.org/',
         r'http://www.stpeterstcecilia.org/',
         r'http://www.mpcatholicchurches.org/',
         r'http://www.straymondchurch.org/',
         r'http://www.stregistrafford.org/',
         r'http://www.saintsebastianchurch.org/',
         r'http://www.stmup.org/',
         r'http://theaccentonline.org/'
         ]

for site in sites:
    os.sys('auto-lighthouse -u %s -d desktop --format html -v' % site)