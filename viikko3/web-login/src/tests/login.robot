*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle1234
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  kalleFail
    Set Password  kalle1234
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

Registration Should Fail
    Page Should Contain  Username must be at least 3 characters