from animal import animal

class carnivora(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kec_lari, jumlah_kaki):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.kec_lari = kec_lari
        self.jumlah_kaki = jumlah_kaki
       
    def info_carnivora(self):
        super().info_animal(),
        print('Kecepatan Lari \t\t\t :', self.kec_lari,
              '\nJumlah kaki \t\t\t :', self.jumlah_kaki)
        
Carnivora = carnivora('Burung Elang', 'Ikan', 'darat daerah dekat perairan dan udara', 'Bertelur', 'Kencang','Dua')
Carnivora.info_carnivora()

print('================')
Carnivora2 = carnivora('Harimau', 'Rusa', 'Darat', 'Melahirkan', 'Kencang','Empat')
Carnivora2.info_carnivora()

print('================')
Carnivora3 = carnivora('Komodo', 'Babi hutan', 'Darat', 'Bertelur', 'Pelan','Empat')
Carnivora3.info_carnivora()