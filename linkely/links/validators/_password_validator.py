"""A password validator that kind of follows the NIST guidelines
https://pages.nist.gov/800-63-3/sp800-63b.html"""

from collections import Counter
from rest_framework import serializers


MOST_COMMON = (
    "mandrake|qazxswedc|sonyfuck|01021985|12091991|06041988|forsaken|valentine|02011986|delpiero|02021984|starfish|baracuda|16061987|qwert123|03031988|02051981|bradford|05031987|02021991|12071990|04041987|barcelon|killer12|therock1|12365478|qwertyqwerty|harrypotter|16051989|04051985|exchange|buddyboy|15081991|24041984|sandwich|rfnthbyf|21031987|wrestler|salamander|rosemary|01011974|nintendo|fyutkjxtr|jessica1|qazwsx12|slapshot|diamond1|fireball|consumer|creampie|blackout|14021986|01011986|10293847|longhair|02061988|25061987|usmarine|07071982|robinson|dodgeram|18071990|universa|18436572|16091988|elizaveta|francisc|seahawks|25802580|03041986|catalina|balloons|01041988|charlie2|27061985|abrakadabra|31011987|friendly|golfgolf|roadrunner|charlton|telephon|1z2x3c4v|20031987|01011978|darkside|10061984|threesom|whocares|formula1|22031984|30031992|castillo|19781978|usuckballz1|gandalf1|just4fun|22051991|letsdoit|16061986|18091985|buffalo1|02081980|123456qwerty|02041975|25071990|vjqgfhjkm|"
    "26021992|24061986|05071988|katherine|hayabusa|17061989|13021990|alcatraz|cherries|16121986|22051989|15011986|pianoman|wildcard|kittykat|25031987|romantic|fuckface|06061986|16121991|scoobydoo|labrador|19751975|sausages|11235813|elcamino|andersen|lonesome|fuckyou2|14101987|friendster|alessandro|temppass|15061985|24121988|01021990|rangers1|kingkong|predator|01021988|wildcats|jackson1|18021987|bastards|engineer|paranoid|chris123|qwe123qwe|gangster|tomorrow|24061992|02041980|whatwhat|hannibal|capricorn|03041991|christin|jeremiah|28081990|bismillah|pingpong|23021985|13091987|19051987|antelope|enterpri|barcelona|24021988|standard|12021990|applepie|dbrnjhbz|06041987|23041988|pantyhos|123456789qwe|yeahbaby|18121983|25051980|fountain|eleonora|supernova|01041980|22111988|19071990|capricor|hyperion|william1|21051986|23051983|17071987|megadeth|02101985|73501505|17091985|02081989|18011987|fearless|eatpussy|gamecube|135792468|mckenzie|15091989|05081986|bearbear|implants|12101989|06101989|"
    "20041988|02071989|27071988|anhyeuem|rhfcjnrf|16031990|valentina|25061986|tottenham|19101987|26011990|12081988|fktrcfylhf|ncc74656|22051987|butthead|qazwsxedc123|02021986|11091986|elizabet|18051987|02061984|15011985|06031992|syracuse|armagedon|14021989|bigmoney|nthvbyfnjh|buttfuck|maxwell1|17091987|frontier|chemical|reckless|1q2w3e4r5t|karolina|chandler|cocksuck|14031988|sweetnes|18061990|chainsaw|cygnusx1|02081977|28011987|argentin|01051986|123454321|superstar|marianne|aardvark|dilligaf|03101991|windsurf|18071989|bullseye|14051990|infinity|29061989|22041988|22121989|bordeaux|10011988|starfire|firefigh|03051987|sporting|mash4077|romashka|prospect|webmaster|19091983|designer|02041974|medicine|19051983|ashleigh|27061988|azertyuiop|makaveli|pakistan|lovelife|03031991|klondike|asdf1234|31121985|tkbpfdtnf|lawrence|veronika|slipknot|nebraska|18051990|millenium|bunghole|12345678a|caligula|theforce|bonehead|northern|kakashka|21011991|22041985|devil666|drpepper|clifford|srinivas|19851985|"
    "playball|15111984|14081988|22011985|broncos1|swinging|01071990|sebastian|american|12101990|derparol|giuseppe|starligh|zeppelin|14101986|marathon|08051989|24101990|motherlode|happyday|seinfeld|hopeless|spongebob|magician|benessere|qawsedrf|27091991|rhiannon|12051986|greenday|brucelee|davidson|09041987|29061985|05021988|fkbyjxrf|18071986|reddevil|02031989|12041990|14011988|23456789|manchest|05061988|cherokee|pavilion|jackass1|riccardo|20091986|06061985|something|eastwood|marianna|16091987|22111985|21031990|02051978|wolfpack|23061987|margaret|13071989|02081979|30031986|bigdicks|nostromo|25091987|02011976|18121990|28021985|03051986|02051987|iverson3|lemonade|anastasi|02041984|a12345678|monsters|25011985|platinum|zxasqw12|blizzard|25061985|31051991|02051975|navyseal|margarita|04091986|summer69|16041988|31031988|16081986|04071986|13101992|stefanie|senators|starwars|success1|porsche1|17021989|shaney14|28061986|a1s2d3f4|26031991|03061988|binladen|30121987|22011992|tottenha|asdqwe123|"
    "29041989|23041986|02031983|verbatim|aolsucks|realmadrid|21081987|02061989|25111987|logitech|02011979|30061987|wildwood|11091985|26061987|notebook|katerina|valkyrie|underdog|deeznutz|29051992|21111985|freefall|metallic|faithful|15071987|20061983|02041973|snowball|redwings|christopher|kingfish|cocacola|thisisit|svetlana|11081987|17051987|06061981|adgjmptw|14021987|josephin|florence|a123456789|nwo4life|1234567a|konstantin|06061987|4815162342|good123654|cheshire|10121986|babylon5|shepherd|02071980|budweiser|07071984|02101986|20091991|soccer12|21111986|traveler|01011979|bobmarley|mikemike|michael1|02011983|01051990|piercing|08061987|browning|04031991|pinnacle|vsjasnel12|15071983|hastings|resident|06041984|08031985|triangle|50spanks|02051985|matchbox|nuttertools|11051984|01011994|06021986|carlitos|nightwish|monalisa|22071983|28021990|cambiami|assassin|02091983|buttercup|lollipop|16011989|superior|22011988|13091984|25081985|godfather|robotics|hardcore|12341234|sinister|mandarin|velocity|"
    "25011993|moonligh|soso123aljg|15091988|nineball|confused|02031991|albatros|sidekick|q123456789|19041985|14051983|peaches1|rfhfylfi|asdfghjk|elephant|poohbear|columbia|lakewood|17111987|02071985|23061990|28041992|shopping|devildog|12041991|billabon|pornporn|19061991|31121986|05111986|25091991|23111986|gabriele|qweasd123|21091989|starcraf|genesis1|01041985|terminal|masterbate|04061984|specialk|handball|02041978|infiniti|military|03082006|tokiohotel|firefire|1234567890q|feelgood|nathalie|super123|01011960|123456ru|22011986|28051986|preacher|terminator|31011990|meredith|fgtkmcby|february|01011970|12qw34er|13011988|francois|21101988|27021990|waterloo|sergeant|10091986|05081992|lighting|viewsoni|20081990|01121987|24121987|02101977|02051973|01031983|greenbay|azsxdcfv|cavalier|blahblah|starbuck|southpaw|12031988|chocolate|02101984|03111987|10081990|asdfghjkl|sunlight|30041985|gordon24|03021986|lunchbox|trinidad|mushroom|31051982|california|heinrich|railroad|blueball|princess|bluejays|"
    "futurama|magicman|ghbdtnbr|longjohn|smoothie|12345679|12345qwe|anastasiya|together|19031985|26061985|illinois|02021971|carpedie|23091987|chrysler|freedom1|savannah|19111985|05051987|paintball|motherfucker|acidburn|buckeyes|27021991|pumpkins|24121986|microlab|charlene|02051983|barbados|02011980|sexysexy|sebastia|17061991|02021973|fastball|webmaste|trouble1|johnson1|08081988|password99|14031989|pancakes|explorer|02041989|wildfire|playstat|darklord|whistler|sylveste|skywalke|29061988|semperfi|washingt|fuckhead|patrick1|29111988|volleyba|amethyst|1234567891|pussycat|03051988|anderson|22061985|25041991|02081987|rhbcnbyf|talisman|johndeer|teddybear|gateway1|westwood|04041983|01011992|trustno1|showtime|02041983|02091971|07071977|david123|redalert|gfhjkmgfhjkm|webhompas|24071990|369258147|budlight|asdffdsa|22071984|31031987|10071986|10021987|dragonfl|stingray|htubcnhfwbz|flipflop|playmate|10101986|minemine|30051989|02101978|vacation|jamesbon|25041985|15021983|plastics|electric|25091989|"
    "dthjybrf|20081991|jennifer|playstation|12071989|03041987|11223344|polniypizdec0211|22021989|america1|stephen1|ghbywtccf|iloveyou2|pornking|ncc1701a|security|17071985|blessing|aspirine|vendetta|blink182|rush2112|fredrick|qwerty123|sexylady|infantry|reddwarf|11061987|longdong|marcius2|sapphire|eclipse1|12121986|mypassword|bynthytn|12121982|28051990|lifetime|987456321|pipeline|ironmaiden|09876543|clarissa|789456123|screamer|12081985|18051988|21071989|dominion|paramedi|17071990|montrose|23111989|01061986|15081990|progress|treasure|passport|kissmyass|drummer1|liverpoo|butthole|02051989|kristian|digital1|smashing|16031988|01011972|moonshin|flounder|01011995|nevermind|16051990|02011971|hoosiers|02091978|halflife|lonestar|mustang6|fairlane|01091992|midnight|02031975|02071981|monkeybo|12348765|01081989|14021985|12081990|raistlin|27081986|z1x2c3v4|happy123|catwoman|vipergts|fuckoff1|lollypop|08041985|02111987|gertrude|rfhnjirf|yamahar1|29011985|alexande|22071985|02091987|27071987|12021988|"
    "rocknroll|brittany|saturday|02101983|19011989|highbury|dfktynby|freebird|06031983|francesc|01041983|basketball|seminole|foxylady|16021987|12344321|wishbone|stephani|pineappl|02031990|15121987|spongebo|patches1|19701970|maryjane|crawford|sentinel|blackcat|01021992|07041989|13121985|08081990|starship|01051985|10091984|goldfing|123456qwe|1qaz1qaz|16061988|mallrats|11041985|cameron1|12101984|r2d2c3po|20031990|20061990|vladimir|10081985|10061985|panther1|14071987|chester1|22031986|concorde|jefferso|13081986|cjkysirj|21101986|10021986|dominiqu|basketba|02081983|19721972|12061988|01071987|21021989|1234567890a|20051983|22051988|14091990|12345qwert|beefcake|titleist|blackman|spectrum|15091987|19801980|18061991|1qazzaq1|thursday|02071975|rainbow1|1qw23er4|keystone|05081988|bearcats|stephanie|qwert12345|rasputin|scorpio1|mandingo|green123|192837465|asdfzxcv|pinetree|sprinter|02081985|q1w2e3r4|02091984|charles1|02051976|123456654321|05091988|krokodil|23101987|frederic|07091988|campbell|"
    "fyutkbyf|01011988|19741974|mariposa|25071987|bluefish|sullivan|saratoga|paradigm|james123|tropical|courtney|fyfcnfcbz|wp2003wp|gtnhjdbx|02101976|nineinch|alexalex|02031973|samantha|brigitte|19091988|98765432|11041990|10071990|facebook|22121983|22081991|8j4ye3uz|16101987|dolphin1|jeanette|18011985|chrisbln|19061992|lockdown|idontkno|04041986|musicman|argentina|25091990|01011984|123456aa|training|blackdog|millions|welcome1|rochelle|24051989|hellyeah|nightmare|goldberg|7894561230|gonzales|11041991|17101986|roadrunn|20021985|45m2do5bs|warcraft|14789632|02061981|rainyday|beautiful|gameover|macintos|15071990|23091991|magazine|vfrcbvrf|napoleon|mustangs|kamasutra|magnolia|stardust|electron|15011987|22041986|pineapple|majestic|q1w2e3r4t5y6|01011981|21121989|viewsonic|blackhaw|paradise|qwerty12|james007|25071985|01234567|corvette|ferrari1|atlantis|istheman|02011989|18021984|hollywood|08031986|warriors|02071978|december|babylove|21061986|10011992|knickers|16071991|pussy123|yankees2|"
    "27051987|19071986|14021983|18101985|pa55word|istanbul|angelina|universe|24031990|telephone|0987654321|achilles|20061986|anaconda|09031988|05121990|charlie1|christmas|18081988|bitchass|sweetpea|30121985|doughboy|intercourse|scotland|access14|koroleva|01031989|cucumber|destiny1|testing1|lowrider|11031986|cosworth|02061982|18111987|16111990|02061979|02011984|02071979|penetration|02041988|radiohead|09051986|27061983|5wr2i7h8|13061986|angelica|16051987|tomahawk|01031986|butterfl|wg8e3wjf|pokemon1|02031982|29031990|02101973|02101980|kordell1|bigdaddy|swimming|15051990|03061985|26041991|18091986|maserati|presario|f00tball|commande|rhtdtlrj|costello|26071989|hardware|snuggles|printing|12121989|02061974|goodgirl|21011988|12121987|anthony1|12081993|crjhgbjy|31051987|15081988|30081984|fordf150|24021991|05011987|31051993|supernov|22061989|21021990|firebird|september|19071988|28051985|pizzaman|02041987|stallion|19071989|chelsea1|celebrity|kcj9wx5n|23021992|19101986|inuyasha|squirrel|guinness|"
    "a1234567|15051987|30051986|mazda626|28071987|25121987|mississippi|kingking|monster1|scooter1|cannabis|smackdow|23031986|16021988|ihateyou|babyface|25101989|12345qwerty|chipmunk|thuglife|29071985|02071971|minimoni|123456789|25011986|gatorade|18031991|national|borussia|mechanic|angel123|sundevil|gannibal|singapor|28121989|lakeside|28041987|penguin1|fireblad|pimpdadd|juventus|1029384756|12301230|27111990|02091988|09081985|skittles|smirnoff|austin31|beatrice|gabriel1|azertyui|vkontakte|23031987|ultimate|tinkerbell|21051990|16111982|assholes|01061992|02061983|hotstuff|02051984|hounddog|19011987|27091985|overlord|23071985|17051989|29121987|jermaine|p0o9i8u7|1122334455|12369874|krasotka|charisma|10101980|blacklab|warrior1|panthers|02031974|dickhead|silverad|buddy123|13031986|stephane|02021978|bubbles1|vasilisa|thompson|lovelove|trinitro|bollocks|dynamite|freeporn|flamengo|18041990|1qa2ws3ed|chiquita|21011989|wolverine|27031986|geoffrey|fishing1|festival|jackjack|gabriell|02021987|"
    "charlott|somethin|christop|undertaker|business|21111989|candyman|20061988|coventry|annmarie|1234512345|01011980|goldeneye|07061988|13243546|cocksucker|peterpan|laurence|03071985|01121990|13081985|123456789s|02031984|kayleigh|sithlord|02031980|25081988|03091988|25121985|evolution|19831983|rjirfrgbde|14725836|enternow|imperial|21111983|19651965|27111989|gfhjkm123|sabrina1|rachelle|mitchell|12071992|01061987|01061988|rockford|123qwe123|southpark|10011983|03061987|apollo13|elizabeth|chocolat|pass1234|02031986|14081985|eternity|dfktynbyf|26071986|trombone|fletcher|29041985|1234567899|stratfor|02101989|brewster|22061990|18021986|04111991|28061988|fortress|leavemealone|31071990|04071988|columbus|23021988|11111987|04081987|02041977|qwerty11|muhammad|bigblock|limewire|22091984|precious|brittney|spaceman|11051988|plymouth|soulmate|cristian|penthous|mobydick|kristina|tinkerbe|1passwor|immortal|12111985|23011990|simpsons|qwerty12345|emmanuel|qwer1234|fredfred|17051988|montecar|15031991|"
    "14031986|26061989|16011987|22121987|darkness|19283746|truelove|complete|lacrosse|12051988|oblivion|21051991|10041986|24061988|20041986|wireless|archange|thegreat|17041991|buttercu|mortgage|25031991|ghbdtn123|navigator|19671967|13091986|21071992|classics|michaels|24091986|15041988|garfield|stranger|02061985|04041985|20121986|22051986|caliente|bookworm|11071985|987654321|director|daisydog|ericsson|qwertyuiop|hallo123|erection|12345qwer|rjycnfynby|22021985|challeng|14071988|rockwell|13071984|29041988|03041983|sandrine|awesome1|02021982|cromwell|21101987|tigercat|29051990|alleycat|26011986|hotpussy|skinhead|pornstar|11071987|marines1|atlantic|18021992|12051987|qwerasdfzxcv|0192837465|zxcvbnm123|mariners|02051977|sherwood|danielle|streaming|corleone|21041992|skywalker|whiteboy|20011983|cnfybckfd|03061986|14041986|10071987|andromed|sersolution|portland|28051987|19761976|johnjohn|13051986|darkstar|11101986|augustus|24011987|27031987|raiders1|gbhfvblf|21021985|wetpussy|freckles|"
    "1357924680|26061986|revolution|blueeyes|mistress|phialpha|10071988|05051991|coolness|michael2|zerocool|02021988|clitoris|bluemoon|ambrosia|sigmachi|alexandr|24111987|30051987|einstein|15081986|alejandr|07071988|02061987|deepthroat|poontang|voyager1|isabelle|14021990|summer99|10031990|qwerqwer|sammy123|goldwing|trfnthbyf|opendoor|22121986|19681968|02051972|17011990|deadpool|11121985|shamrock|yankees1|22081983|02041982|01051988|18031988|guardian|02091985|14121989|bluebell|28071986|stickman|01041993|melissa1|14081990|04071987|patriots|hurricane|24111990|hardcock|02061976|30031988|superman|vanhalen|chevelle|playtime|23051986|terrapin|leedsutd|hardball|cassandra|21041991|30051985|ghjcnjnfr|02081986|beautifu|kamikaze|13041988|22091990|bullshit|nokia6233|stanislav|optimist|15051981|christian|18121984|camaross|21101989|43214321|dkflbckfd|11091989|01031988|20041990|smackdown|07071987|terminat|15071988|11111986|23121986|12071988|roadster|taekwondo|stockton|daylight|letmein2|15081989|"
    "holidays|services|24071987|30061988|ghjcnbnenrf|farscape|downtown|cfitymrf|10203040|21081985|07081987|meowmeow|02041976|billyboy|pleasure|dirtbike|creature|22081986|25021985|03041984|changeme|01081985|teddybea|gangbang|19021990|blueblue|31101987|letmein1|solution|09051945|08051990|megapass|ferguson|25041988|backdoor|02021989|hedgehog|washington|funstuff|motorola|anything|03011987|patience|salvador|30041986|weare138|01061990|criminal|21031985|slowhand|01071984|29061990|sunflowe|candyass|23051990|thanatos|rastaman|07091990|dutchess|customer|08081989|cabernet|26081986|bluebird|14091987|discover|gilligan|16021990|ilovesex|fandango|avalanch|11121987|valentin|20081986|thankyou|diamonds|28121984|normandy|10041983|alexandra|springer|rockhard|abcd1234|vfitymrf|02031985|mustang1|chevrolet|hotgirls|calimero|socrates|10081987|islander|16051988|password123|marriage|valencia|honolulu|08051987|23091985|30061983|almighty|17041986|satan666|mailcreated5240|12051985|newcastle|peterbil|26071984|"
    "moneyman|18011988|09041986|24682468|963852741|fantomas|superman1|09091986|cristina|icehouse|chicken1|26101987|slamdunk|30041991|undertak|02021979|elisabet|pool6123|baseball|22061941|13021985|happiness|reynolds|12021984|painting|123qq123|treefrog|p0015123|20011988|02031977|20031991|swordfis|lokiloki|splinter|theodore|21061985|fuckinside|dolemite|03091983|02031978|madeline|technics|southpar|13101988|dolphins|gsxr1000|password|1a2s3d4f|09021988|1x2zkg8w|21021987|14041988|05071985|airplane|321654987|swingers|capetown|mamacita|gesperrt|20031985|luckydog|metallica|veronica|123456789m|27011988|coldbeer|grateful|19041986|02091976|12081983|nevermore|23011985|29051985|zxcvbnm1|26031984|17121987|bangbang|02041986|05071984|18121987|woodstoc|wrestling|illusion|blackbir|26031986|10101985|vagabond|20041985|obsidian|02051979|scarlett|iloveyou|23051987|27031992|1234qwer|canadian|02071986|26031987|sundance|123789456|qwertyuio|catherine|newpass6|magellan|godfathe|panasoni|12345678|07071985|04111988|"
    "15031990|yjdsqgfhjkm|amsterdam|holyshit|12061986|26111985|maverick|10031993|15011983|03041980|9876543210|softball|02011981|baseball1|eatmenow|12101988|q2w3e4r5|123qwert|meridian|stigmata|19021991|16091990|tiffany1|iloveyou1|lineage2|insomnia|09091988|20031986|04061987|frederik|montgom240|turkey50|10071985|contract|marseill|10031980|brandon1|armstron|doberman|babydoll|zachary1|money123|26101986|keyboard|1234asdf|somerset|delaware|21101983|stargate|casanova|master12|vancouve|17061988|kittycat|passwords|hercules|segblue2|22071990|mercedes|hamilton|shadow12|personal|marjorie|nounours|zildjian|07071990|nightmar|slippery|cerberus|12051990|rocknrol|jonathon|rjhjktdf|escalade|homework|flexible|10031987|13071985|deftones|dukeduke|12qw12qw|02021981|19861986|08121987|passwort|underground|scrapper|wonderboy|16071987|nautilus|15041987|experienced|jamesbond|08111984|whiskers|forever1|24011985|22021988|10101988|loverboy|04041988|alejandro|gonzalez|04051988|01011976|jayhawks|12021991|21041985|"
    "19821982|12061987|13061991|02081988|pathfind|05061990|comanche|andromeda|strawber|19641964|spitfire|santiago|09081988|asshole1|multiplelo|20011989|smeghead|rebecca1|26071987|pa55w0rd|03031987|johannes|nascar24|03031990|01091988|01011975|liverpool1|10041991|13071987|18111986|21051988|icecream|marcello|computer|anastasia|rfntymrf|twilight|snickers|nokia6300|02101988|tiberius|snowboar|dogpound|02011985|newyork1|buckshot|shannon1|02061978|10051988|abcdefgh|19051986|barefoot|penelope|kirkland|26041986|umbrella|crazybab|callaway|zaq12wsx|22071989|22021986|02031987|chicago1|22061987|22021990|spartan1|francesco|19841984|entrance|25011990|01121988|bobafett|17101987|13111990|cassandr|minecraft|colorado|7ugd5hip2j|16031986|yogibear|lightning|11121986|123654789|shitface|1232323q|getmoney|20091988|chouchou|maradona|dannyboy|24071992|12041988|fktrcfylh|16121987|maryland|herewego|lonewolf|panasonic|12021985|20021986|airforce|slimshad|bcfields|estrella|22091986|12131415|07041987|munchkin|"
    "23091986|budapest|123qweasd|defender|gargoyle|02101981|29061986|02031988|jordan23|sterling|04021990|meathead|01021987|dragonballz|02061971|123qweasdzxc|12071987|dreamcas|30121988|peekaboo|fuckyou1|californ|deeznuts|mcdonald|30121986|lkjhgfdsa|irishman|isabella|agent007|pinkfloy|carolina|recovery|14071986|15021985|25041987|shanghai|puppydog|billybob|1qazxsw2|123456789d|whiplash|cardinal|07091982|17041987|zxcasdqwe|15111988|20031988|02091982|44332211|01081992|03031984|24041985|carnival|sheridan|antonina|pringles|palmtree|02051980|25031984|ncc1701e|01011982|margarit|01041987|15051992|12031985|20061987|02081974|blue1234|children|robotech|21031984|01091987|01071986|01012009|volkswag|12081984|mischief|christina|solitude|22071992|hellokitty|02051970|14041987|02061990|02011987|30011985|26051988|sparkles|02071987|14061988|heritage|28081986|viktoriya|suburban|private1|abc12345|monopoly|cheyenne|24101989|25081986|134679852|thunder1|cutiepie|19061987|cricket1|porkchop|26051986|24081988|"
    "thunderb|sasha_007|power123|02021985|kjrjvjnbd|05051990|12091988|vanguard|02021990|16101986|07041988|hollywoo|apple123|02071988|16051985|22031991|masamune|checkers|translator|22091991|caroline|13061987|cashmone|01041990|sexygirl|juliette|13031989|creative|lancelot|clemente|hardrock|24031988|19121989|bluesman|07021980|trucking|titanium|brighton|24041986|20121988|evolutio|research|741852963|bigballs|pathetic|maksimka|07081984|24041988|23061989|28021986|02011977|03011991|zaq1xsw2|berkeley|20101988|1234509876|15021986|123456789z|24091991|02071982|20051985|australi|jellybean|martinez|15051986|12121988|26121989|11061984|inspiron|cleopatra|remingto|123456qqq|135798642|05061986|amateurs|12111990|aberdeen|callisto|02081982|hetfield|babygirl|ragnarok|fantasia|pallmall|10121987|123qwerty|lightnin|21071987|perfect1|snowflak|12345678910|29011987|74108520|werewolf|24101984|download|bullfrog|02101987|13031987|lkjhgfds|cdtnkfyf|29071983|scrabble|18041986|02081970|hurrican|westside|02081984|"
    "02061986|27021992|tiger123|27041985|bigbooty|homemade|wonderful|23031983|02061980|speakers|20071988|valhalla|richmond|07051990|capslock|hairball|gotohell|matthews|09021989|snoopdog|20031992|warhammer|12345qaz|28021992|12071984|richard1|sunshine|23041987|20051987|fishbone|christine|asdfasdf|thirteen|20021988|17061987|borabora|spiderma|passw0rd|02081976|25031983|1234567q|12011987|football|scissors|11021985|29011982|november|10041987|crackers|internet|24101988|22061988|10121985|sandiego|luckyone|01021989|02041985|whatever|18101987|sojdlg123aljg|goodluck|14011987|qazwsxedcrfv|carebear|20121989|papillon|02061977|wordpass|02011990|02091975|babycake|rfvfcenhf|lokomotiv|fuckfuck|08071988|hellsing|06081987|01121986|baritone|mulligan|punisher|07101984|08031987|vikings1|17021985|01081990|13091988|vfhufhbnf|honeybee|everlast|amsterda|windmill|10111986|liverpool|straight|intrepid|23061992|goldfish|29111989|annabell|15111989|laetitia|chestnut|blackjack|colonial|02021983|gretchen|thrasher|"
    "pussyman|fyfnjkbq|cooldude|jiggaman|morpheus|12041986|29081985|27031989|warhamme|stanford|1qazxsw23edc|1234zxcv|speedway|02091973|rockstar|123456789q|10011986|mynameis|07051987|eldorado|earthlink|14041992|johngalt|28011988|kcchiefs|matthew1|reginald|cornwall|syncmaster|noname123|08041986|qazwsx123|123456123|01101987|kimberly|19081987|megatron|05031991|01031981|missouri|meatball|14061991|15121983|blackjac|18011986|26091986|11061991|24051990|10071989|15061984|02101979|12qwaszx|aquarius|17011987|nirvana1|concrete|lorraine|highheel|13021987|harrison|charlotte|hawaiian|02051990|30101988|catherin|phoenix1|13101987|cbr900rr|jackson5|06071983|clippers|microsoft|zaqxswcde|13051990|12031987|darkangel|23091989|0123456789|oklahoma|10101989|clarinet|penguins|04061991|sherlock|sunnyday|function|17071989|08071987|favorite6|12011985|21041987|zxcasdqwe123|26031990|flamingo|republic|10061989|washburn|samsung1|02091986|swordfish|ncc1701d|sweetness|attitude|24011990|insanity|rainbows|13041989|"
    "17111985|password2|cowboys1|knuckles|11031988|qazwsxedc|evangelion|ghostrider|testpass|18111983|10081983|lifehack|manchester|enterprise|sneakers|rolltide|19731973|winston1|captain1|christia|alphabet|fishhead|madison1|18031986|strength|fullmoon|crusader|19871987|03031992|09111987|deadhead|02091980|scarface|13111984|02031979|18121985|football1|earnhard|hongkong|1234567890|lesbians|spartans|peterson|01011985|19121988|macaroni|11061985|19111987|poiuytre|qwerty1234|revolver|ghjuhfvvf|gn56gn56|06021987|loveless|20061984|23021986|slimshady|05041985|11011987|25021988|13071990|25051988|a1b2c3d4|scoobydo|bulldog1|17031987|dragster|mohammed|supersta|22091988|10051990|30111987|26021987|vampires|24111989|tazmania|02041981|11071988|15011990|31051985|12071991|05061989|06061988|13061985|whiteout|drowssap|phillips|rhjrjlbk|1qaz2wsx|cannibal|radiohea|17061986|31121988|01011983|25081989|jellybea|sinclair|natasha1|01011977|01091985|toriamos|10041990|stripper|vauxhall|qwertyui|lisalisa|30011987|"
    "morrowind|virginia|mazafaka|university|heineken|kazantip|overkill|mudvayne|05051985|01011971|q1w2e3r4t5|marino13|kathleen|05031990|woodland|1123581321|22071986|30011986|01031985|cleopatr|04061986|absolute|chevrole|username|colombia|kristine|virginie|stonecold|02071983|paintbal|skorpion|21121985|touching|147896325|qweasdzxc|09041985|excalibur|24121989|02011988|firewall|zxcv1234|startrek|nokian73|suckdick|creation|mollydog|dragonba|vanessa1|1234abcd|daughter|20051988|goodtime|17051983|golfball|11011989|idontknow|australia|qwerty123456|12031990|dkflbvbh|nicholas|franklin|cadillac|motocros|zaqwsxcde|07071989|20111986|wareagle|tunafish|24071991|ekaterina|longhorn|tommyboy|25051985|moonlight|01020304|15031988|03041989|147258369|13071982|30091989|packers1|24101986|12081987|18061985|shithead|hattrick|12121985|02011982|02091989|10031989|harddick|kangaroo|08011986|williams|22071991|florida1|mazdarx7|southern|pressure|yfcntymrf|10061987|macdaddy|15051985|06051986|01011989|moonbeam|abnormal|"
    "06011988|02091981|alliance|survivor|05051989|stocking|03031986|vladislav|offshore|19111986|hawaii50|positive|conquest|superfly|jonathan|10091985|bobdylan|excalibu|22061984|mohammad|lalakers|28101986|1qaz2wsx3edc|punkrock|10041984|steelers|tacobell|commando|23021989|modelsne|strawberry|marijuana|11051986|remember|arsenal1|21111990|22041987|sonysony|12011989|intruder|21031986|25071983|02041972|japanese|champion|marlboro|misfit99|28021983|butterfly|jasmine1|microphone|18091987|15071986|snowbird|08121986|02081973|original|sonyericsson|masterbating|23051985|07021991|gladiato|kentucky|knockers|01011987|skateboard|stafford|01051989|mountain|serenity|andyod22|poiuytrewq|01011993|14011986|05051986|scorpion|scheisse|24061985|birthday|24031987|1234567890-|pumpkin1|redskins|pharmacy|waterboy|12121990|pavement|07101987|presiden|15051989|poseidon|dinosaur|10031988|02021980|freepass|bergkamp|21031988|sunflower|clevelan|asdfgh01|transfer|sailboat|19031987|ghhh47hj7649|22071987|spencer1|"
    "vqsablpzla|thailand|123698745|millwall|fernando|18051989|02061972|piramida|sergbest|28031982|dragon69|babyblue|11031983|02011975|password9|pinkfloyd|9293709b13|hooligan|playboy1|03081989|wrangler|tarheels|bulldogs|junkmail|sniffing|ghblehjr|07081986|coltrane|michigan|31121987|05121988|01091989|23041991|15101991|dontknow|soccer10|1234rewq|freeuser|monkey12|dodgers1|montreal|01061983|software|pufunga7782|cinnamon|bigboobs|barselona|crystal1|12345abc|21061988|pearljam|dragon12|25800852|roadkill|coldplay|03071987|stonecol|11071989|09051987|11081986|arkansas|15011988|aleksandra|marijuan|universal|absolutely|16011986|02071984|zanzibar|23031990|08081986|angelika|1234554321|giovanni|sheepdog|ilikepie|10011980|cheerleaers|02051982|23111987|13121983|espresso|president|test1234|26061991|12091986|11051990|20071984|greatone|christie|lipstick|starstar|michaela|godzilla|kleopatra|01071988|handyman|27041990|victoria|13021991|hello123|chuckles|starcraft|password1|leonardo|25051987|02031981|"
    "13051987|31415926|doomsday|rainbow6|11081990|789654123|eggplant|newcastl|lfitymrf|doghouse|pasadena|23skidoo|patricia|02051988|geronimo|wrinkle1|rootbeer|19411945|wildbill|25101988|forgetit|fellatio|thedoors|20101987|jeepster|10051987|05091987|property|cameltoe|25111991|31121990|brooklyn|bigpoppa|budweise|11091984|30041987|11061986|violetta|29031988|goldstar|adrienne|airborne|gladiator|15091985|morrison|19061985|19081986|mephisto|11081989|wanderer|meatloaf|lasvegas|blowfish|passwor1|26031988|24101991|richards|katherin|highlander|24061987|adrenalin|09051984|18041991|pantera1|17021987|14111986|brothers|enforcer|mortimer|christma|cardinals|08071985|20071986|p4ssw0rd|portugal|marshall|11061989|18021988|aleksandr|10031991|17071986|ministry|09031987|pictures|chargers|wrestlin|federico|claymore|register|21021988|operator|12345678q|22071988|platypus|kawasaki|1q2w3e4r|septembe|12111984|yosemite|27081990|snowboard|02081981|katarina|01051980|handsome|death666|redbaron|03031993|benjamin|"
    "toonarmy|mersedes|01011973|12101985|02041979|clarence|13101982|gabriela|viktoria|02091977|15021990|lionking|kenworth|20051989|29051989|15101986|29091987|11051987|87654321|14101988|netscape|marseille|pentagon|porsche9|05021987|spiderman|building|13011987|gamecock|04041991|darkange|25021986|04041990|jakejake|qazwsxed|q1234567|14011989|07031989|dietcoke|cashmoney|phillies|1q2w3e4r5t6y|02071976|renegade|heather1|hellfire|fuckthis|02021976|1q2w3e4r5|19061990|03071986|wolfgang|21121986|michelle|philippe|13041987|17121985|roadking|eastside|fishfish|nygiants|qwerasdf|runescape|mongoose|suckmydick|15061988|08101986|30011990|alexander|kingston|1a2b3c4d|killbill|01041992|28071985|123456789a|30051988|aviation|ghjcnjgfhjkm|10081989|dragonball|147852369|fuck_inside|password12|16061985|godsmack|01031984|15071985|20061991|hawkeyes|cartoons|question|17041985|bubba123|17051990|justdoit|23051991|16041985|15426378|29081990|dingdong|matthias|06011982|30071986|carpente|11071986|12051989|gorgeous|"
    "spanking|killer123|sexybabe|02071977|tennesse|08021990|10061986|alexandre|vfntvfnbrf|highland|rammstein|front242|78945612|rightnow|chambers|02051986|elements|broadway|johncena|11081988|whitesox|graphics|microsof|wolverin|ilovegod|23021983|salasana|123456qw|chickens|27111985"
).split("|")


CONTEXT = ["linkely"]


def password_validator(value):
    test = value.lower()

    not_long_enough(test)
    has_repetitive_characters(test)
    is_common_password(test)
    has_context_words(test)
    too_many_sequential(test)


def not_long_enough(value):
    if len(value) < 8:
        raise serializers.ValidationError("The password is too short.")


def has_repetitive_characters(value):
    if len(Counter(value)) <= 2:
        raise serializers.ValidationError(
            "The password has too many repetetive characters."
        )


def is_common_password(value):
    if value in MOST_COMMON:
        raise serializers.ValidationError("The password is too common.")


def has_context_words(value):
    for word in CONTEXT:
        if word in value:
            raise serializers.ValidationError("The password is too easy to guess.")


def too_many_sequential(value):
    character_map = list(map(ord, value))
    distances = [abs(a - b) for a, b in zip(character_map[1:], character_map[:-1])]
    if len(list(distance for distance in distances if distance > 1)) < 3:
        raise serializers.ValidationError(
            "The password has too many sequential characters."
        )
