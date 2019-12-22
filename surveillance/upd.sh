git pull https://github.com/methodmath/home_surveillance.git

docker run -v /Users/:/host -p 5000:5000 -t -i bjoffe/openface_flask_v2  /bin/bash
cd host/soldierforce/Documents/Developer/home_surveillance/system/
pkill python
pkill luajit
python WebApp.py > /dev/null 2>&1 &

rtsp://172.22.120.212:8080/h264_ulaw.sdp
