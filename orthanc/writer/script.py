import orthanc
from datetime import datetime, timezone, timedelta
import base64
import json

CONFIGURATION = json.loads(orthanc.GetConfiguration()) # orthanc.json attributes
processingStudies = {} # Hold a timestamp for each incoming study

def requestFilter(uri, **request):
    auth = str(base64.b64decode(request['headers']['authorization'].split()[1]), 'utf-8')
    user = auth.split(':')[0]
    password = auth.split(':')[1]
    return user == '###ORTHANC_ADMIN###' and password == '###ORTHANC_ADMIN_PASSWORD###'

def onNewStudy(resourceId):
    study = json.loads(orthanc.RestApiGet(f"/studies/{resourceId}"))
    processingStudies[study.get('MainDicomTags').get('StudyInstanceUID')] = datetime.now(timezone.utc)
    orthanc.LogWarning(f"NEW STUDY: {resourceId}")

def onStableStudy(resourceId):
    study = json.loads(orthanc.RestApiGet(f"/studies/{resourceId}"))
    studyInstanceUID = study.get('MainDicomTags').get('StudyInstanceUID')
    studyCreationDate = processingStudies[studyInstanceUID]

    delta = datetime.now(timezone.utc) - studyCreationDate - timedelta(seconds = CONFIGURATION.get('StableAge'))
    processingStudies.pop(studyInstanceUID, None)

    orthanc.LogWarning(f"STABLE. ELAPSED TIME: {delta}")
    orthanc.LogWarning(f"STUDY DATA: {study}")

def onChange(changeType, level, resourceId):
    if changeType == orthanc.ChangeType.NEW_STUDY:
        onNewStudy(resourceId)

    if changeType == orthanc.ChangeType.STABLE_STUDY:
        onStableStudy(resourceId)

orthanc.RegisterOnChangeCallback(onChange)
orthanc.RegisterIncomingHttpRequestFilter(requestFilter)