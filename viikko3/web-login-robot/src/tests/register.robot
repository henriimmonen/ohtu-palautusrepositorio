*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  mikko
    Set Both Passwords  mikko123
    Submit Registering
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  Al
    Set Both Passwords  yankovic1
    Submit Registering
    Register Should Fail With Message  Username not suitable

Register With Valid Username And Too Short Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  Ali
    Set Both Passwords  leinio
    Submit Registering
    Register Should Fail With Message  Password not suitable

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Register Page Should Be Open
    Set Username  Ali
    Set Password  leinio11
    Input Password  password_confirmation  leinio12
    Submit Registering
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Go To Register Page
    Set Username  Ali
    Set Both Passwords  leinio123
    Submit Registering
    Go To Login Page
    Login Page Should Be Open
    Set Username  Ali
    Set Password  leinio123
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Go To Register Page
    Set Username  Al
    Set Both Passwords  yankovic1
    Submit Registering
    Go To Login Page
    Set Username  Al
    Set Password  yankovic1
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Registering
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Both Passwords
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}