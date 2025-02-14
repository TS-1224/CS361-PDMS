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

total_labor_cost_request = {
    "request": {
        "event": "getLaborCost",
        "body": {
            "labor":{
                "Worker": [6, 20],
                "CrewLeader": [1, 25],
                "Supervisoer": [1, 30]
            },
            "duration": 2
        }
    }
}
total_labor_cost_request = json.dumps(total_labor_cost_request)

print("[LOG] Launch Driver Service")
while True:
    # getLaborCost event
    input("Press any key to send a request: ")

    print(f"[Sent->] {total_labor_cost_request}")
    socket.send_string(total_labor_cost_request)

    response = socket.recv()
    response = json.loads(response)
    print(f"[Received<-] {response}")

    # customerAgeData event
    input("Press any key to send a request: ")

    print(f"[Sent->] {customer_age_data_request}")
    socket.send_string(customer_age_data_request)

    response = socket.recv()
    response = json.loads(response)
    print(f"[Received<-] {response}")
