
cookies= {
    "guest_id": "v1%3A167537407404289669",
    "d_prefs": "MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw",
    "guest_id_ads": "v1%3A167537407404289669",
    "guest_id_marketing": "v1%3A167537407404289669",
    "personalization_id": "\"v1_XllVzr6CA3iW4P2Qdk6k/A",
    "_ga": "GA1.2.1665478394.1675374080",
    "_gid": "GA1.2.1606044619.1675374080",
    "dt": "kQOKNb6nZhJWzlMjB5fp3L3pGiVfJ0w8GqN149bZ",
    "auth_token": "8ecbe38432e6d3064f3e2619263396348e83365c",
    "ct0": "c8f4f21427963eb14e563d10cf4f2f0c00bed7473f59cfb20e1013d415fbc4880675d135aafebcd5289abbe5d4a9d0986cee528c106ec60e8637ac6e44ce96697343b96cabcd3fa310e7833bf556ce36",
    "twid": "u%3D1621259590124945408",
    "u_cn": "1"
}

headers= {
    "Content-Length": "1556",
    "Sec-Ch-Ua": "\"Chromium\";v=\"109\", \"Not_A Brand\";v=\"99\"",
    "X-Twitter-Client-Language": "en",
    "X-Csrf-Token": "c8f4f21427963eb14e563d10cf4f2f0c00bed7473f59cfb20e1013d415fbc4880675d135aafebcd5289abbe5d4a9d0986cee528c106ec60e8637ac6e44ce96697343b96cabcd3fa310e7833bf556ce36",
    "Sec-Ch-Ua-Mobile": "?0",
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "X-Twitter-Auth-Type": "OAuth2Session",
    "X-Twitter-Active-User": "yes",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Origin": "https://twitter.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://twitter.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

params= {
    "keepalive": "false"
}

data= {
    "category": "perftown",
    "log": "[{\"description\":\"rweb:seen_ids:persistence:get:success\",\"product\":\"rweb\",\"duration_ms\":10},{\"description\":\"rweb:seen_ids:persistence:get:success\",\"product\":\"rweb\",\"duration_ms\":10},{\"description\":\"rweb:init:storePrepare\",\"product\":\"rweb\",\"duration_ms\":9},{\"description\":\"rweb:ttft:perfSupported\",\"product\":\"rweb\",\"duration_ms\":1},{\"description\":\"rweb:ttft:perfSupported:DE\",\"product\":\"rweb\",\"duration_ms\":1},{\"description\":\"rweb:ttft:connect\",\"product\":\"rweb\",\"duration_ms\":52},{\"description\":\"rweb:ttft:connect:DE\",\"product\":\"rweb\",\"duration_ms\":52},{\"description\":\"rweb:ttft:process\",\"product\":\"rweb\",\"duration_ms\":63},{\"description\":\"rweb:ttft:process:DE\",\"product\":\"rweb\",\"duration_ms\":63},{\"description\":\"rweb:ttft:response\",\"product\":\"rweb\",\"duration_ms\":1},{\"description\":\"rweb:ttft:response:DE\",\"product\":\"rweb\",\"duration_ms\":1},{\"description\":\"rweb:ttft:interactivity\",\"product\":\"rweb\",\"duration_ms\":657},{\"description\":\"rweb:ttft:interactivity:DE\",\"product\":\"rweb\",\"duration_ms\":657}]"
}

r = requests.post(
    'https://api.twitter.com/1.1/jot/client_event.json',
    params=params,
    data=data,
    cookies=cookies,
    headers=headers
)
