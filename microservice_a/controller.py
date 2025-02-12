# Name: Takafumi Suzuki
# OSU Email: suzukt@oregonstate.edu
# Course: CS361
# Assignment: Microservice A
# Due Date:
# Description: Controller
# version: 0.1

import os
import json
import zmq
from constants import *
from usecase.customer_age_data import CustomerAgeDataUsecase
from exceptions import InvalidEventException

class Controller:
    def __init__(self):
        self._port_pdms = 5555

    def execute(self):
        """
        Function: Controller of this service.
        Params: nothing
        Return: nothing
        """
        print(f"[LOG] Start PDMS")

        # create a context and socket
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(f"tcp://*:{self._port_pdms}")

        while True:
            # clear a terminal
            os.system('clear')

            # receive a request
            request = json.loads(socket.recv())
            print(f"[->Received] request: {request}")
            event = request["request"]["event"]
            request_body = request["request"]["body"]

            # decode
            if len(request) > 0:
                if event == Constants.EVENT_CUSTOMER_AGE_DATA:
                    usecase = CustomerAgeDataUsecase(request_body)
                    return_body, status_code = usecase.execute()
                else:
                    raise InvalidEventException

                # create a response
                response = json.dumps(self._create_response(event, return_body, status_code))

                # send a response to main services
                print(f"[<-Sent]: {response}")
                socket.send_string(response)

    def _create_response(self, event, body, code):
        """
        Function: Create the content of responses
        Params:
            event(str): event name
            body(any): response body
            code(str): status code
        Return:
            response(dict)
        """
        response = {
            "request": {
                "event": event,
                "body": body,
                "code": code
            }
        }
        return response

if __name__ == "__main__":
    controller = Controller()
    controller.execute()