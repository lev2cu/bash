#!/bin/bash

cat $1 | awk '{s+=$1}END{print s}'
