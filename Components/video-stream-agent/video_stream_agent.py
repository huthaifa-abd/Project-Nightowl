import subprocess
import sys
import time

# The install method allows the easy installation of Python packages in realtime
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
print("Project Nightowl v0.1")
print("Video Stream Agent v0.1")
print("initializing required python packages...")
# Install Eureka Client to be used to connected to the Application Gateway
install("py_eureka_client")

import py_eureka_client.eureka_client as eureka_client

# Setup the application gateway connection params
your_rest_server_port = 8761
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server="http://YWRtaW4=:YWRtaW4=@127.0.0.1:8761/eurka",
                                app_name="video_stream_agent",
                                instance_port=your_rest_server_port)

# Conenct to HDFS
print("Establishing connection to HDFS...")
while True:
    print("Waiting for video stream.")
    time.sleep(60) # Delay for 1 minute (60 seconds).

