echo "----------SOAL LATIHAN ARITMATIKA----------"

echo "nilai a :"
read a
echo "nilai b :"
read b

echo "Berapakah hasil dari a+b ?"

let penjumlahan=a+b
echo "a + b = $penjumlahan" 


# menggunakan percabangan
sleep 1.5
echo "---------Lanjut Yuk!!----------"

echo "Operasi Aritmatika"
echo "1. Penjumlahan"
echo "2. Pengurangan"
echo "3. Perkalian"
echo "4. Pembagian"
echo "Pilih 1-4"
read pilih

case "$pilih" in
     "1")
     echo "=== Operasi Penjumlahan ==="
     echo "Masukkan nilai a :"
     read a
     echo "Masukkan nilai b :"
     read b
     let hasil=$a+$b
     echo "a + b = $hasil"
     ;;
     "2")
     echo "=== Operasi Pengurangan ==="
     echo "Masukkan nilai a :"
     read a
     echo "Masukkan nilai b :"
     read b
     let hasil=$a-$b
     echo "a - b = $hasil"
     ;;
     "3")
     echo "=== Operasi Perkalian ==="
     echo "Masukkan nilai a :"
     read a
     echo "Masukkan nilai b :"
     read b
     let hasil=$a*$b
     echo "a * b = $hasil"
     ;;
     "4")
     echo "=== Operasi Pembagian ==="
     echo "Masukkan nilai a :"
     read a
     echo "Masukkan nilai b :"
     read b
     let hasil=$a/$b
     echo "a / b = $hasil"
     ;;
esac
