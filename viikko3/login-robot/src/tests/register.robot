*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Check User  Mikko  makkis999

Register With Already Taken Username And Valid Password
    Input Credentials  Mikko  maisteri11
    Input New Command
    Output Should Contain  User with username Mikko already exists

Register With Too Short Username And Valid Password
    Input Credentials  Al  yankovic1
    Input New Command
    Output Should Contain  Username not suitable

Register With Valid Username And Too Short Password
    Input Credentials  Pekka  pouta
    Input New Command
    Output Should Contain  Password not suitable

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kimmo  vehvilainen
    Input New Command
    Output Should Contain  Password not suitable

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  Mikko  makkis999
