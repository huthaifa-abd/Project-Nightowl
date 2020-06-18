echo off
ECHO Initialize Development Environment PROJECT NIGHTOWL V0.1
ECHO Initialize Eurka Application Gateway Service
ECHO Starting Eurka Application Gateway Service (This might take a while)...
docker-compose -f Components\applicationGateway\src\main\docker\jhipster-registry.yml up -d
ECHO The application gateway service can be accessed using the following url http://127.0.0.1:8761/
ECHO Initialize Video Processing Unit Dependencies
ECHO Important: Dont forget to start ftp server on localhost:21 and configure your cameras to save videos to it
mkdir VideoProcessingUnit
git clone https://github.com/ageitgey/face_recognition.git VideoProcessingUnit
xcopy "initvpu.sh" "VideoProcessingUnit" /S
cd VideoProcessingUnit
docker-compose up --build
docker run -it --privileged face_recognition /bin/bash -c "git clone -b 'develop' https://github.com/huthaifa-abd/Project-Nightowl.git && python Project-Nightowl/Components/video-stream-agent/video_stream_agent.py"

