*** Settings ***
Documentation     Check arithmetic operations


Library           easy_math.py



*** Variables ***



*** Test Cases ***

T1: Adding two integers
        ${result}=  easy_math.Calculate  ${20}  ${15}  +
        Should Be Equal As Integers  ${result}  ${35}

T2: Subtracting two integers
        ${result}=  easy_math.Calculate  ${20}  ${15}  -
        Should Be Equal As Integers  ${result}  ${5}

T3: Multiplying two integers
        ${result}=  easy_math.Calculate  ${6}  ${7}  *
        Should Be Equal As Integers  ${result}  ${42}

T4: Dividing two integers
        ${result}=  easy_math.Calculate  ${42}  ${7}  /
        Should Be Equal As Integers  ${result}  ${6}