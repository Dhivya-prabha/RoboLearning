*** Settings ***

Library     SeleniumLibrary
Library		RequestsLibrary
Library     Collections


*** Variables ***
${base_url}    https://reqres.in
${page_path}    $.page
${id_path}      $.id

*** Test Cases ***
Post Request
     Create Session    session1     ${base_url}       disable_warnings=1
     ${endpoint}       set variable       /api/users
     ${body}=      create dictionary    name=Dhivya     job=SW Engineer
     ${response}=      Post On Session  session1     ${endpoint}        data=${body}
     log to console        ${response.status_code}
     log to console        ${response.content}
     ${status_code}=       convert to string       ${response.status_code}
     should be equal       ${status_code}    201

     ${json_response}=    Convert to string    ${response.content}
     ${contents}=      Set Variable     ${json_response}        ${id_path}
     should not be empty        ${contents}
