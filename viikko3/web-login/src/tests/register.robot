*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  simo
    Set Password  simo1234
    Set Password2  simo1234
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  arttu1234
    Submit Register
    Register Should Fail with Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  keijo
    Set Password  k
    Set Password2  k
    Submit Register
    Register Should Fail with Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  heikki
    Set Password  aaaaaaaa
    Set Password2  aaaaaaaa
    Submit Register
    Register Should Fail with Message  Password must not contain only letters a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  jussi
    Set Password  jussi1234
    Set Password2  jussi1235
    Submit Register
    Register Should Fail with Message  Passwords must match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle4321
    Set Password2  kalle4321
    Submit Register
    Register Should Fail with Message  Username already exists

Login After Successful Registration
    Set Username  mortti
    Set Password  mortti1234
    Set Password2  mortti1234
    Submit Register
    Submit Continue
    Submit Logout
    Go To Login Page
    Set Username  mortti
    Set Password  mortti1234
    Click Button  Login
    Main Page Should Be Open
    
Login After Failed Registration
    Go To Login Page
    #Too Short Username And Valid Password
    Set Username  a
    Set Password  arttu1234
    Click Button  Login
    Login Page Should Be Open

    #Valid Username And Too Short Password
    Set Username  keijo
    Set Password  k
    Click Button  Login
    Login Page Should Be Open

    #Valid Username And Invalid Password
    Set Username  heikki
    Set Password  aaaaaaaa
    Click Button  Login
    Login Page Should Be Open

    #Nonmatching Password And Password Confirmation
    Set Username  jussi
    Set Password  jussi1234
    Click Button  Login
    Login Page Should Be Open

    #Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle4321
    Click Button  Login
    Login Page Should Be Open

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail with Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Submit Logout
    Click Button  Logout

Submit Continue
    Click Link  Continue to main page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password2
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
