*** Settings ***

Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  https://demo.nopcommerce.com/
${title}    nopCommerce demo store

*** Test Cases ***
Google
    #Create Webdriver   chrome executable_path="D:/PyPractice/chromedriver/chromedriver.exe"
    Open Browser         ${url}      ${browser}
    SeleniumLibrary.Maximize Browser Window
    LoginPage
    #close browser
    Title Should Be     ${title}

*** Keywords ***
LoginPage
    click element       xpath://a[@class='ico-login']
    ${"email"}      set variable    id:Email
    Element Should Be Visible    ${"email"}
    input text      id:Email      divya2red@gmail.com
    input text      id:Password      India@123
    click element       xpath://button[@class='button-1 login-button']
