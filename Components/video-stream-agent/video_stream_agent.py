import subprocess
import sys
import time
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
print("Project Nightowl v0.1")
print("Video Stream Agent v0.1")
print("initializing required python packages...")
install("py_eureka_client")

import py_eureka_client.eureka_client as eureka_client

your_rest_server_port = 8761
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server="http://YWRtaW4=:YWRtaW4=@127.0.0.1:8761/eurka",
                                app_name="video_stream_agent",
                                instance_port=your_rest_server_port)

print("Establishing connection to HDFS...")
while True:
    print("Waiting for video stream.")
    time.sleep(60) # Delay for 1 minute (60 seconds).

