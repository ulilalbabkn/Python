# Algoritma dan pemrogramman. Tugas Pertemuan 3
# Ulil Albab Kamal Nugraha (220535606377)
greeting = input("").strip().lower()
if greeting == "hello" or greeting == "hello, newman":
    print("$0")
elif greeting.startswith('h'):
    print("$20")
else:
    print("$100")