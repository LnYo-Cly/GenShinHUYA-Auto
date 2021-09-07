import requests
from bs4 import BeautifulSoup

hasDone=[]
falseDone=[]
receive=[]
noneHave=[]
#url='https://www.douyu.com/topic/yskbkb?rid=5239782#bc4'
url='https://www.douyu.com/japi/carnival/nc/roomTask/getPrize'
headers={
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.84',
    "Cookie":r"acf_auth=9f75NiNRyZKdS69plE2TdP221fZiUWTyg7cctfraIG0VYL1%2Br5sGSwf%2F0Aw68Tip13n8JHoh4UmD2xj3sNvpu3AIDrb7%2Bhkn8uTL0GtBTyXrQWEX0e3mR5A; dy_auth=b080%2BEeaKLegjIt%2BS8Fnlsnlp1Q6eeruL%2F2PvltsKPDc90dPXM9SRDIgxc38j2vRyiPGI%2F1eNxEsgsTa0JWuCNF2rxCQrslIVu%2FBW%2Bxv4RX98UdMhmV5QK0; wan_auth37wan=c64b94bf4889izV0LbTN%2BvEmOWD4%2BIua%2FG4INw47EIjEnGGKfDUnOx20Us4RjtE7GwrxKgm%2FiFUqgalegEGzXRbyotN1bhT%2BBCwNTiVM4YpFhUpaQz4; acf_uid=419868680; acf_username=419868680; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=40237212; acf_biz=1; acf_stk=b233b44c6b125274; acf_isNewUser=1; acf_nickname=%E7%92%80%E7%92%A8%E6%98%9F%E8%BE%B0%E4%B8%AD%E7%9A%84%E6%B5%81%E5%85%89; acf_own_room=1; dy_did=94c7805c89c9176ace834cea16441601; acf_did=94c7805c89c9176ace834cea16441601; acf_avatar=//apic.douyucdn.cn/upload/avatar/default/15_; PHPSESSID=f8n8n3f7tvro87330njukf45g4; acf_ccn=f67738efd0addb910a53310449bc647d; cvl_csrf_token=2625a362e30649febe465fa1aea49d38",
    'referer': 'https://www.douyu.com/topic/yskbkb?rid=5239782'
}
data={
    'taskId': '80237'
}


res = requests.post(url,headers=headers,data=data)
i=1

for id in range(80237,80241):
    data['taskId']=str(id)
    requests.post(url,headers=headers,data=data).json()

