#!/bin/bash

#a comment
echo "Test`ttest" # "`" is an escape characture

#all the traditional stuff with redirection apply
ls | grep ".sh"
ls | grep ".sh" > test.txt
cat < test.txt
rm ./test.txt

