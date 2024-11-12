*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    #Go to Registration Form
    Set Username  tiina
    Set Password  tiina1234
    Set Password Confirmation  tiina1234
    Submit Registration Form
    Registration Should Succeed
    #Log Out

Register With Too Short Username And Valid Password
    #Go to Registration Form
    Set Username  sa
    Set Password  sanna1234
    Set Password Confirmation  sanna1234
    Submit Registration Form
    Registration Should Fail Username
    #Log Out

Register With Valid Username And Too Short Password
    #Go to Registration Form
    Set Username  sanna
    Set Password  sanna12
    Set Password Confirmation  sanna12
    Submit Registration Form
    Registration Should Fail Password

Register With Valid Username And Invalid Password
    #Go to Registration Form
    Set Username  sanna
    Set Password  sannasanna
    Set Password Confirmation  sannasanna
    Submit Registration Form
    Registration Should Fail Password

Register With Nonmatching Password And Password Confirmation
    #Go to Registration Form
    Set Username  sanna
    Set Password  sanna1234
    Set Password Confirmation  sanna5678
    Submit Registration Form
    Registration Should Fail Confirmation

Register With Username That Is Already In Use
    #Go to Registration Form
    Set Username  jenna
    Set Password  jenna1234
    Set Password Confirmation  jenna1234
    Submit Registration Form
    Log Out
    Go to Registration Form
    Set Username  jenna
    Set Password  jenna1234
    Set Password Confirmation  jenna1234
    Registration Should Fail InUse


Login After Successful Registration
    # create valid user
    #Go to Registration Form
    Set Username  riikka
    Set Password  riikka1234
    Set Password Confirmation  riikka1234
    Submit Registration Form
    Registration Should Succeed
    Log Out

    # Log in with the same credentials after logout
    Set Username  riikka
    Set Password  riikka1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    # create faulty user
    #Go to Registration Form
    Set Username  ri
    Set Password  riikka1234
    Set Password Confirmation  riikka1234
    Submit Registration Form
    Registration Should Fail Username

    # Log in with the same credentials
    Go to Login 
    Set Username  ri
    Set Password  riikka234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Login Page
    Reset Application
    Create User  kalle  kalle1234
    Go To Login Page

Log Out
    Click Link    Continue to main page
    Click Button  Logout

Go to Registration Form
    Click Link  Register

Go to Login
    Click Link  Login

Submit Registration Form
    Click Button  Register

Registration Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Registration Should Fail Username
    Page Should Contain  Username must be at least 3 characters

Registration Should Fail Password
    Page Should Contain  Password must be at least 8 characters

Registration Should Fail Confirmation
    Page Should Contain  Password and confirmation do not match

Registration Should Fail InUse
    Page Should Not Contain  Welcome to Ohtu Application!

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Login Page
    Go to Registration Form