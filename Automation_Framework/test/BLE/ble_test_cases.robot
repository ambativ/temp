| *** Settings ***   |
| Documentation      | Test the DUT connection with host and its functionality in BLE mode
| Library            | OperatingSystem
| Library            | Process
| Library            | BuiltIn
| Resource           | ../../data/BLE/ble_test.resource


| *** Test Cases ***            |                 |
| Read Humidity                 | [Documentation] | Read Humidity from DUT
| | ${output} =                 | Read Humidity
| | Should Be Equal As Integers | ${output}       | 101

| Read Temparature              | [Documentation] | Read Temparature from DUT
| | ${output} =                 | Read Temparature
| | Should Be Equal As Integers | ${output}       | 101

| Read Pressure                 | [Documentation] | Read Pressure from DUT
| | ${output} =                 | Read Pressure
| | Should Be Equal As Integers | ${output}       | 101



