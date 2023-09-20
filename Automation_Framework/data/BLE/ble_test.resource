| *** Settings ***   |
| Documentation      | Test the DUT connection with host and its functionality in BLE mode
| Library            | OperatingSystem
| Library            | BuiltIn
| Library            | Process
| Library            | asyncio
| *** Variables ***  |
| ${APPLICATION}     | python ../Automation_Framework/ble_host.py

| *** Keywords ***              |
| Read Temparature              | [Documentation] | Read Temparature from Sensor via ESP32
| | ${rc}                       | ${output} =     | Run and Return RC and Output | ${APPLICATION} read_temparature
| | Should Be Equal As Integers | ${rc}           | 0
| | [Return]                    | ${output}

| *** Keywords ***              |
| Read Pressure                 | [Documentation] | Read Pressure from Sensor via ESP32
| | ${rc}                       | ${output} =     | Run and Return RC and Output | ${APPLICATION} read_pressure
| | Should Be Equal As Integers | ${rc}           | 0
| | [Return]                    | ${output}


| *** Keywords ***              |
| Read Humidity                 | [Documentation] | Read Humidity from Sensor via ESP32
| | ${rc}                       | ${output} =     | Run and Return RC and Output | ${APPLICATION} read_humidity
| | Should Be Equal As Integers | ${rc}           | 0
| | [Return]                    | ${output}


