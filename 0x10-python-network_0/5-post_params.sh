#!/bin/bash
#post json data
curl "$1" -sLX POST -H "'Content-Type':'application/json'" \
    -d "{'email':'hr@holbertonschool.com','subject':'I will always be here for PLD'}"
