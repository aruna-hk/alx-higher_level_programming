#!/bin/bash
# sending request with custom header
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
