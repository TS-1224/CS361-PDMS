# Name: Takafumi Suzuki
# OSU Email: suzukt@oregonstate.edu
# Course: CS361
# Assignment: Course Project
# Due Date:
# Description: Driver test module
# version: 0.1

import zmq
import time
import json
from microservice_a.constants import Constants

# create a context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://localhost:{Constants.PORT_PDMS}")

# test data
customer_age_data_request = {
    "request": {
        "event": "customerAgeData",
        "body": ""
    }
}
customer_age_data_request = json.dumps(customer_age_data_request)

print("[LOG] Launch Driver Service")
while True:
    time.sleep(1)

    input("Press any key to send a request: ")

    # customerAgeData event
    print(f"[Sent->] {customer_age_data_request}")
    socket.send_string(customer_age_data_request)

    response = socket.recv()
    response = json.loads(response)
    print(f"[Received<-] {response}")
