import requests
from typing import Optional

'''
v: String,      // apiVersion           e.g: v1

tc:String,      // team code            e.g: 137fb5dbcff742fda8893d8db1ca3d0d
did: String,    // datasource id        e.g: 11

uid: String,    // member id            e.g: 1
cid: String,    // cdp user id          e.g: 11111111.1111111

at: String,     // action               e.g: view, click, watch...
tg: String,     // target               e.g  btn01, link03,....

pt: String,     // path                 e.g: https://ezorderly.com/
tl: String,     // title                e.g: ORDERLY CRM - 系統化管理會員行銷活動

de: String,     // encoding             e.g: UTF-8
ul: String,     // language             e.g: zh-tw
sd: String,     // screenColors         e.g: 24-bit
sr: String,     // screenResolution     e.g: 1920x1080
vp: String,     // viewportSize         e.g: 1905x887
'''


class Tracker:
    def __init__(self, team_code, ds_id, relay_url, cerem_url) -> None:
        self.team_code = team_code
        self.ds_id = ds_id
        self.relay_url = relay_url
        self.cerem_url = cerem_url

    def click_event(self, v: str = '', pt: str = '', tl: str = '',
                    ul: str = 'zh-tw', uid: Optional[str] = '', cid: Optional[str] = None, de: str = '',
                    sd: str = '', sr: str = '', did: str = '', vp: str = '',
                    tg: str = '',
                    ):

        result, cid = self._record_event(
            v=v, pt=pt, tl=tl,
            ul=ul, uid=uid, cid=cid, de=de,
            sd=sd, sr=sr, did=did, vp=vp,
            at='click', tg=tg,
        )

    def view_event(self, v: str = '', pt: str = '', tl: str = '',
                   ul: str = 'zh-tw', uid: Optional[str] = '', cid: Optional[str] = None, de: str = '',
                   sd: str = '', sr: str = '', did: str = '', vp: str = '',
                   tg: str = '',
                   ):

        result, cid = self._record_event(
            v=v, pt=pt, tl=tl,
            ul=ul, uid=uid, cid=cid, de=de,
            sd=sd, sr=sr, did=did, vp=vp,
            at='view', tg=tg,
        )

    def _record_event(self, v: str = '', pt: str = '', tl: str = '',
                      ul: str = 'zh-tw', uid: Optional[str] = '', cid: Optional[str] = None, de: str = '',
                      sd: str = '', sr: str = '', did: str = '', vp: str = '',
                      at: str = '', tg: Optional[str] = ''
                      ):

        if cid is None:
            try:
                response = requests.get(self.cerem_url + '/tracking/generate-cid/', params={'team_code': self.team_code})
                cid = response.json()['cid']
            except Exception:
                return False, ''

        payload = {
            'tc': self.team_code,
            'did': did,
            'v': v,
            'uid': uid,
            'cid': cid,
            'tg': tg,
            'de': de,
            'at': action,
            'ul': ul,
            'pt': pt,
            'sd': sd,
            'sr': sr,
            'tl': tl,
            'vp': vp
        }

        requests.get(self.relay_url + '/api/' + self.ds_id + '/tracking/', params=payload)

        return True, cid
