from animal import animal

class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_gigi, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_gigi = jenis_gigi
        self.jenis_kulit = jenis_kulit
       
    def info_mamalia(self):
        super().info_animal(),
        print('Jenis Gigi \t\t\t :', self.jenis_gigi,
              '\nUkuran Tubuh \t\t\t :', self.jenis_kulit)
        
Mamalia = mamalia('Kucing', 'Ikan', 'Darat', 'Melahirkan', 'Bertaring','Berbulu')
Mamalia.info_mamalia()

print('================')
Mamalia2 = mamalia('Kelelawar', 'Buah', 'Gua', 'Melahirkan', 'Seri kecil dan taring besar','Berbulu')
Mamalia2.info_mamalia()

print('================')
Mamalia3 = mamalia('Gajah', 'Tumbuh-tumbuhan', 'Darat', 'Melahirkan', 'Gading, taring, dan geraham','Sedikit berbulu')
Mamalia3.info_mamalia()