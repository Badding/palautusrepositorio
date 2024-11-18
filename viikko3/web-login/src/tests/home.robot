*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Starting Page

*** Test Cases ***
Click Login Link
    Click Link  Login
    Login Page Should Be Open

Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

*** Keywords ***
Register Page Should Be Open
    Title Should Be  Register

Reset Application And Go To Starting Page
    Reset Application
    Create User  kalle  kalle123
    Go To Starting Page