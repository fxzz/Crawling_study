import requests
import json
from datetime import datetime


# 첨부 지점코드(유인관서)

# 지점	지점명	관리관서	지점	지점명	관리관서
# 90	속초	강원지방기상청	212	홍천	춘천기상대
# 93	북춘천	춘천기상대	216	태백	강원지방기상청
# 95	철원	강원지방기상청	217	정선군	강원지방기상청
# 98	동두천	수도권기상청	221	제천	청주기상지청
# 99	파주	수도권기상청	226	보은	청주기상지청
# 100	대관령	강원지방기상청	232	천안	대전지방기상청
# 101	춘천	춘천기상대	235	보령	대전지방기상청
# 102	백령도	수도권기상청	236	부여	대전지방기상청
# 104	북강릉	강원지방기상청	238	금산	대전지방기상청
# 105	강릉	강원지방기상청	239	세종	대전지방기상청
# 106	동해	강원지방기상청	243	부안	전주기상지청
# 108	서울	수도권기상청	244	임실	전주기상지청
# 112	인천	수도권기상청	245	정읍	전주기상지청
# 114	원주	강원지방기상청	247	남원	전주기상지청
# 115	울릉도	대구지방기상청	248	장수	전주기상지청
# 119	수원	수도권기상청	251	고창군	전주기상지청
# 121	영월	강원지방기상청	252	영광군	광주지방기상청
# 127	충주	청주기상지청	253	김해시	부산지방기상청
# 129	서산	홍성기상대	254	순창군	전주기상지청
# 130	울진	안동기상대	255	북창원	창원기상대
# 131	청주	청주기상지청	257	양산시	울산기상대
# 133	대전	대전지방기상청	258	보성군	광주지방기상청
# 135	추풍령	청주기상지청	259	강진군	목포기상대
# 136	안동	안동기상대	260	장흥	목포기상대
# 137	상주	대구지방기상청	261	해남	목포기상대
# 138	포항	대구지방기상청	262	고흥	광주지방기상청
# 140	군산	전주기상지청	263	의령군	창원기상대
# 143	대구	대구지방기상청	264	함양군	창원기상대
# 146	전주	전주기상지청	266	광양시	광주지방기상청
# 152	울산	울산기상대	268	진도군	목포기상대
# 155	창원	창원기상대	271	봉화	대구지방기상청
# 156	광주	광주지방기상청	272	영주	안동기상대
# 159	부산	부산지방기상청	273	문경	안동기상대
# 162	통영	부산지방기상청	276	청송군	대구지방기상청
# 165	목포	목포기상대	277	영덕	대구지방기상청
# 168	여수	광주지방기상청	278	의성	대구지방기상청
# 169	흑산도	광주지방기상청	279	구미	대구지방기상청
# 170	완도	목포기상대	281	영천	대구지방기상청
# 172	고창	전주기상지청	283	경주시	대구지방기상청
# 174	순천	광주지방기상청	284	거창	울산기상대
# 177	홍성	홍성기상대	285	합천	울산기상대
# 184	제주	제주지방기상청	288	밀양	울산기상대
# 185	고산	제주지방기상청	289	산청	창원기상대
# 188	성산	제주지방기상청	294	거제	부산지방기상청
# 189	서귀포	제주지방기상청	295	남해	부산지방기상청
# 192	진주	창원기상대			
# 201	강화	인천기상대			
# 202	양평	수도권기상청			
# 203	이천	수도권기상청			
# 211	인제	강원지방기상청			


# 현재 날짜와 시간
current_datetime = datetime.now()

url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'
params ={'serviceKey' : 'HxIe5DJezM9Ttm/cyiMjrvAI9TqqYKnmI6vu7uzo/NXfwaSfvEZFE8iXGEak8pV2wENfzd1vb7jx3/82RAnAZg==',
        'pageNo' : '1',
        'numOfRows' : '24',
        'dataType' : 'JSON',
        'dataCd' : 'ASOS',
        'dateCd' : 'HR',
        'startDt' : '20240114',
        'startHh' : '00',
        'endDt' : '20240115',
        'endHh' : '23',
        'stnIds' : '211' }

response = requests.get(url, params=params)

data = json.loads(response.content)

# items 안에 있는 item들 추출
items = data['response']['body']['items']['item']
# 각 item 출력
for item in items:
    print(item)
    print()




CREATE TABLE WeatherData (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tm VARCHAR(255),
    rnum VARCHAR(255),
    stnId VARCHAR(255),
    stnNm VARCHAR(255),
    ta VARCHAR(255),
    taQcflg VARCHAR(255),
    rn VARCHAR(255),
    rnQcflg VARCHAR(255),
    ws VARCHAR(255),
    wsQcflg VARCHAR(255),
    wd VARCHAR(255),
    wdQcflg VARCHAR(255),
    hm VARCHAR(255),
    hmQcflg VARCHAR(255),
    pv VARCHAR(255),
    td VARCHAR(255),
    pa VARCHAR(255),
    paQcflg VARCHAR(255),
    ps VARCHAR(255),
    psQcflg VARCHAR(255),
    ss VARCHAR(255),
    ssQcflg VARCHAR(255),
    icsr VARCHAR(255),
    dsnw VARCHAR(255),
    hr3Fhsc VARCHAR(255),
    dc10Tca VARCHAR(255),
    dc10LmcsCa VARCHAR(255),
    clfmAbbrCd VARCHAR(255),
    lcsCh VARCHAR(255),
    vs VARCHAR(255),
    gndSttCd VARCHAR(255),
    dmstMtphNo VARCHAR(255),
    ts VARCHAR(255),
    tsQcflg VARCHAR(255),
    m005Te VARCHAR(255),
    m01Te VARCHAR(255),
    m02Te VARCHAR(255),
    m03Te VARCHAR(255)
);

INSERT INTO WeatherData (tm, rnum, stnId, stnNm, ta, taQcflg, rn, rnQcflg, ws, wsQcflg, wd, wdQcflg, hm, hmQcflg, pv, td, pa, paQcflg, ps, psQcflg, ss, ssQcflg, icsr, dsnw, hr3Fhsc, dc10Tca, dc10LmcsCa, clfmAbbrCd, lcsCh, vs, gndSttCd, dmstMtphNo, ts, tsQcflg, m005Te, m01Te, m02Te, m03Te)
VALUES ('2024-01-14 23:00', '24', '211', '인제', '-0.4', '', NULL, '9', '0.2', '', '0', '', '88', '', '5.2', '-2.1', '997.5', '', '1022.9', '', '', '9', '', '3.7', '', '0', '0', '', '', '1942', '', '', '', '0.3', '', '', '', '');






