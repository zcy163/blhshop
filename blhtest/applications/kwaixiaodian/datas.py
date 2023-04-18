from django.conf import settings


datas = {
    "AUTHORIZE_DATA": {
        "app_id": settings.KWAIXIAODIAN_APP_ID,
        "redirect_uri": settings.KWAIXIAODIAN_OAUTH2_AUTHORIZE_URL,
        "scope": settings.KWAIXIAODIAN_SCOPE,
        "response_type": settings.KWAIXIAODIAN_RESPONSE_TYPE,
    },
    "ACCESS_TOKEN_PARAMS": {
        "app_id": settings.KWAIXIAODIAN_APP_ID,
        "grant_type": settings.KWAIXIAODIAN_GRANT_TYPE,
        "code": "",
        "app_secret": settings.KWAIXIAODIAN_APP_SECRET,
    },
    "REFRESH_TOKEN_DATA": {
        "grant_type": "refresh_token",
        "refresh_token": "",
        "app_id": settings.KWAIXIAODIAN_APP_ID,
        "app_secret": settings.KWAIXIAODIAN_APP_SECRET,
    },
    "SIGN_DATA": {
        "access_token": "",
        "appkey": settings.KWAIXIAODIAN_APP_ID,
        "method": "",
        "param": {},
        "signMethod": settings.KWAIXIAODIAN_SIGN_METHOD,
        "timestamp": "",
        "version": "1",
        "signSecret": settings.KWAIXIAODIAN_SIGN_SECRET,
    }
}
    
