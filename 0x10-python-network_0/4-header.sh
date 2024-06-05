#!/bin/bash
# sending request with custom header
curl "$1" -sL -H "X-School-User-Id:98"
