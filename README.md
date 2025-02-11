# Personal Data Management Service (PDMS)

## Index

* [Specifications](#Specifications)
* [Sequence diagrams](#Sequence diagrams)

## Basic Information
* CS361, 2025 Winter term
* Developer name: Takafumi Suzuki

## Specifications
Main programs can communicate with this service via <span style="color: red;">**ZeroMQ**</span> in the local environment.<br>
The port number of this service is <span style="color: red;">**#5555**</span>.

### 1.How to request data

To request data from this service, main programs must create requests in the specified format and a socket with the port number, then send it.<br>

Request Specification:

| Attribute | Meaning                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------|
| request   | Top level attribute, which must include event and body attributes.                              |
| event     | The name of event used to invoke functions related to each user story.                          |
| body      | The data to be used in functions related to user stories. The value varies depending on events. |

Example:
```
{
    "request": {
        "event": "customerAgeData",
        "body": ""
    }
}
```

### 2.How to receive data

To retrieve data from this service, main programs must create a socket for receiving beforehand.<br>
After sending the request, your main program receive a response in the following format.<br>

Response Specification:

| Attribute | Meaning                                                                   |
|-----------|---------------------------------------------------------------------------|
| response  | Top level attribute, which must include event, body, and code attributes. |
| event     | The name of event used to invoke functions related to each user story.    |
| body      | The data returned from this service.                                      |
| code      | Response status. In the case of success, its value is 200, otherwise 400. |

Example:
```
{
    "request": {
        "event": "customerAgeData",
        "body": {
            "customerAge": [18, 25, 33, 45]
        },
        "code": "200"
    }
}
```

## Sequence diagrams
### Routing

```plantuml
@startuml

' Participants
Participant "Main Program" as main
Participant "PDMS" as pdms #LightGreen

' Flow
activate main

main -> pdms: Send a request via ZeroMQ

activate pdms

pdms -> pdms: parse the request
alt TBD: User Story: Calculating labor costs
else TBD:User Story: Calculating labor costs
else event == customerAgeData
    ref over pdms: See the sub-sequence of customerAgeData event
end

pdms -> pdms: create a response
pdms -> pdms: create a socket for main programs
main <- pdms: Send a response via ZeroMQ

deactivate pdms
deactivate main


' notes
note right
Port#:
 Andrew's Mian program: TBD
 Shinji's Main program: #30001
end note
@enduml
```

### customerAgeData event
```plantuml
@startuml

' Participants
Participant Controller as cont #LightGreen
Participant customerAgeDataUsecase as uc #LightGreen
database customerData as cd

activate cont

cont -> cont: create the instance of \ncustomerAgeDataUsecase class
cont -> uc: execute()

activate uc

uc -> cd: get_customer_data()
activate cd
cd -> uc: return customer data
deactivate cd

alt customer data is not empty
    uc -> uc: extract_customer_ages()
    uc -> uc: set status code = 200
else
    uc -> uc: set status code = 400
end

note right
 DB is a csv file format.
 File path: ../customer_data.csv
end note

cont <- uc: return customer ages and status code

deactivate uc
deactivate cont
@enduml
```
