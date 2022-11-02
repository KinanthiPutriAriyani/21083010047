#!/bin/bash

# Mendeklarasikan fungsi
panjang() {
    echo "Masukkan Panjang  :"
    read panjang
    lebar
}
lebar() {
    echo "Masukkan Lebar :"
    read lebar
    let kali=$panjang*$lebar
    echo "Luas Persegi : $kali"
}
panjang    

