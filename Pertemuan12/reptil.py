from animal import animal

class reptil(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bergerak, kebiasaan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bergerak = bergerak
        self.kebiasaan = kebiasaan
       
    def info_reptil(self):
        super().info_animal(),
        print('Cara Bergerak \t\t\t :', self.bergerak,
              '\nKebiasaan \t\t\t :', self.kebiasaan)
        
Reptil = reptil('Kura-kura', 'Tumbuhan', 'Darat dan air tawar', 'Bertelur', 'Menggunakan kaki','Pemangsa pasif')
Reptil.info_reptil()

print('================')
Reptil2 = reptil('Ular', 'Mamalia kecil, burung, atau reptil', 'Dua alam', 'Bertelur', 'Merayap','Pemangsa aktif')
Reptil2.info_reptil()

print('================')
Reptil3 = reptil('Iguana', 'Daun, bunga, dan buah', 'Hutan tropis dan semak', 'Bertelur', 'Menggunakan kaki','Pemangsa pasif')
Reptil3.info_reptil()