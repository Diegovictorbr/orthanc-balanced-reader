#!/bin/bash

set -e
cd

URL=http://lsb.orthanc-server.com/
VERSION_DICOM_WEB=1.8
VERSION_GDCM=1.5
VERSION_MYSQL=5.1
VERSION_PYTHON=4.1

wget ${URL}/plugin-dicom-web/${VERSION_DICOM_WEB}/libOrthancDicomWeb.so
wget ${URL}/plugin-mysql/${VERSION_MYSQL}/libOrthancMySQLIndex.so
wget ${URL}/plugin-mysql/${VERSION_MYSQL}/libOrthancMySQLStorage.so
wget ${URL}/plugin-gdcm/${VERSION_GDCM}/libOrthancGdcm.so
wget ${URL}/plugin-python/debian-buster-python-3.7/${VERSION_PYTHON}/libOrthancPython.so
wget --no-check-certificate https://orthanc.osimis.io/lsb/plugin-osimis-webviewer/releases/1.4.2/libOsimisWebViewer.so

mv ./libOrthancDicomWeb.so             /usr/local/share/orthanc/plugins/
mv ./libOrthancMySQLIndex.so           /usr/local/share/orthanc/plugins/
mv ./libOrthancMySQLStorage.so         /usr/local/share/orthanc/plugins/
mv ./libOrthancGdcm.so                 /usr/local/share/orthanc/plugins/
mv ./libOsimisWebViewer.so             /usr/local/share/orthanc/plugins/
mv ./libOrthancPython.so               /usr/local/share/orthanc/plugins/