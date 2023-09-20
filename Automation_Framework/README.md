###################################################################################
This project is created for IOT Automation testing using Robot Automation Framework.
As part of this project, planning to create accelators for WiFi/BLE protocol tesing 
on any type of product.
###################################################################################

Prerequisite :

1. Install robot automation framework using pip. Make sure pip is already installed.

pip install robotframework

###################################################################################

Project Sturcture :

Automation_Framework/

./Automation_Framework:
README.md  ble_host.py  data/  requirements.txt  test/  wifi_host.py

./Automation_Framework/data:
BLE/  WiFi/

./Automation_Framework/data/BLE:
ble_test.resource

./Automation_Framework/data/WiFi:
wifi_test.resource

./Automation_Framework/test:
BLE/  WiFi/  log.html  output.xml  report.html

./Automation_Framework/test/BLE:
ble_test_cases.robot

./Automation_Framework/test/WiFi:
wifi_test_cases.robot

###################################################################################

Test Report Generation Procedure :

syntax : robot <path of test cases, .robot extension> 

                    or
        python -m robot <path of test cases, .robot extension>

robot test/*/*.robot ====> It will run test cases under test/ folder. Test folder again has WiFi and BLE sub folders where test cases are available.

