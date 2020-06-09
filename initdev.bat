echo off
ECHO Initialize Development Environment PROJECT NIGHTOWL V0.1
ECHO Initialize Video Processing Unit Dependencies
mkdir VideoProcessingUnit
git clone https://github.com/ageitgey/face_recognition.git VideoProcessingUnit
cd VideoProcessingUnit
docker-compose up --build