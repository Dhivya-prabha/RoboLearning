*** Settings ***

Library     SeleniumLibrary
Library		RequestsLibrary
Library     Collections


*** Variables ***
${base_url}    https://reqres.in


*** Test Cases ***
Get Request
      Create Session    session1     ${base_url}       disable_warnings=1
      ${endpoint}       set variable       /api/users?page=2
      ${response}=      GET On Session  session1     ${endpoint}
      log to console        ${response.headers}
      log to console        ${response.status_code}
      log to console        ${response.content}
      #log                   ${response.content}

#      Validations
      ${status_code}=       convert to string       ${response.status_code}
      should be equal       ${status_code}    200
#
#      ${json_response}=    Convert to String    ${response}
#      ${contents}=      Set Variable     ${json_response}
#      ${contents}=      convert to string       ${contents}
#      #${contents}       Remove String Using Regexp      ${contents}     ['\\[\\],]
#
#      ${headerValue}=       get from dictionary     ${response.headers}     Content-Type
#      should be equal       ${headerValue}      application/json; charset=utf-8
