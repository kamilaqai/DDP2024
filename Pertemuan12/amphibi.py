from animal import animal

#setiap class child itu memiliki 2 properti dan method  
class amphibi(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print('Jenis Air \t\t\t :', self.jenis_air,
              '\nBernapas \t\t\t :', self.bernapas)
        
Amphibi = amphibi('Katak', 'Serangga', 'Dua alam', 'Bertelur', 'Tawar','Kulit dan paru-paru')
Amphibi.info_amphibi()

print('========')
Amphibi2 = amphibi('Salamander', 'Serangga', 'Dua alam', 'Bertelur', 'Tawar','Kombinasi kulit, paru-paru, dan insang')
Amphibi2.info_amphibi()

print('======')
Amphibi3 = amphibi('Buaya', 'Daging', 'Dua alam', 'Bertelur', 'Payau dan Tawar','Kulit dan paru-paru')
Amphibi3.info_amphibi()


