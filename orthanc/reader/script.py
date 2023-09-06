import orthanc
import base64

def requestFilter(uri, **request):
    headers = request['headers']
    auth = str(base64.b64decode(headers['authorization'].split()[1]), 'utf-8')
    user = auth.split(':')[0]
    password = auth.split(':')[1]
    userAuthenticated = (user == '###ORTHANC_USER###' and password == '###ORTHANC_USER_PASSWORD###')
    
    if 'reconstruct' in uri:
        return userAuthenticated

    return userAuthenticated and request['method'] == orthanc.HttpMethod.GET 

orthanc.RegisterIncomingHttpRequestFilter(requestFilter)
