class PersegiPanjang:
    def __init__(self, panjang, Lebar):
        self.panjang = panjang
        self.lebar = Lebar

    def keliling(self):
        return 2* (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, Panjang {self.panjang} cm, dan lebar {self.lebar} cm"


try:
    panjang_input = int(input("Masukan Panjang (cm):"))
    lebar_input = int(input("Masukan Lebar (cm):")) 

    pp = PersegiPanjang(panjang_input, lebar_input)
    print("Keliling:", pp.keliling(), "cm")
    print("Luas:", pp.luas(), "cm^2")

except ValueError:
    print("Input harus berupaangka.")
    