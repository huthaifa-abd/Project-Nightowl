import subprocess
import sys
import time
print("Project Nightowl v0.1")
print("Video Stream Agent v0.1")
print("initializing required python packages...")
install("py_eureka_client")
print("Establishing connection to HDFS...")
while True:
    print("Waiting for video stream.")
    time.sleep(60) # Delay for 1 minute (60 seconds).
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
