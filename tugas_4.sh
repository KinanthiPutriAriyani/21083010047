#!/bin/bash

echo "----------PROGRAM PERULANGAN----------"

echo "input :"
read input

echo 
for ((angka=input; angka>0; angka=angka-2))
do
   echo $angka
done
