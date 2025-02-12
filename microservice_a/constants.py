# Name: Takafumi Suzuki
# OSU Email: suzukt@oregonstate.edu
# Course: CS361
# Assignment: Microservice A
# Due Date:
# Description: Constants data class
# version: 0.1


class Constants:
    # Common
    SUCCESS = "200"
    FAILURE = "400"

    # Personal Data Management Service
    PORT_PDMS = 5555

    # getCustomerRecords event
    PORT_CUSTOMER = 30001
    EVENT_CUSTOMER_AGE_DATA = "customerAgeData"
    CSV_CUSTOMER_DATA = "../csv/customers_data.csv"
    HEADER_AGE = "Age"