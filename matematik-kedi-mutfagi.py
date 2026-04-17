#!/usr/bin/env python3
"""
🐱 Kedi Mutfağı - Elif Miray için Matematik Oyunu
8 yaş + için eğlenceli toplama/çıkarma/çarpma/bölme
"""

import random

# 🎨 Kediler
KEDILER = [
    ("🐱", "Şef Pofuduk", "Şef kedi"),
    ("😺", "Mırnav", "Neşeli kedi"),
    ("😼", "Patron Kedi", "Müşteri"),
    ("😻", "Boncuk", "Küçük kedi"),
    ("😽", "Prenses", "Nazlı kedi"),
    ("😾", "Korkak Kedi", "Korkak ama tatlı"),
    ("😸", "Büyük Kedi", "Bilge kedi"),
    ("😿", "Üzgün Kedi", "Hayal kırıklığı"),
]

YEMEKLER = [
    "🍕 pizza", "🍝 makarna", "🍔 burger", 
    "🌮 taco", "🍣 sushi", "🧁 kurabiye",
    "🥣 çorba", "🥞 wafle", "🍦 dondurma",
    "🥪 sandviç", "🍟 patates", "🍜 erişte"
]

class MatematikKediOyunu:
    def __init__(self):
        self.puan = 0
        self.seviye = 1
        self.toplam_soru = 0
        self.dogru = 0
        
    def giris(self):
        print("""
🐱 🌮 KEDİ MUTFAĞI 🌮 🐱
=========================
      
   _\|/_   Hoş geldin!   _\|/_
  (O O)              (O O) 
   | |    Şef Pofuduk  | |
  _| |_              _| |_
     
""")
        print("😺: Merhaba Elif Miray! 🐱")
        print("    Restoranımızı açıyoruz!")
        print("    Her doğru cevapta yemek pişireceğiz!")
        print("    + - × ÷ hepsini öğreneceğiz!")
        print()
        
    def soru_uret(self, seviye):
        """Her seviye için soru üret"""
        
        if seviye == 1:
            islemler = ["+"]
        elif seviye == 2:
            islemler = ["+", "+"]
        elif seviye == 3:
            islemler = ["+", "-"]
        elif seviye == 4:
            islemler = ["+", "-", "×"]
        elif seviye == 5:
            islemler = ["×", "×", "×", "-"]
        else:
            islemler = ["×", "÷", "×", "÷", "-", "+"]
        
        islem = random.choice(islemler)
        
        if islem == "+":
            a = random.randint(1, 10 * seviye)
            b = random.randint(1, 10 * seviye)
            return a, b, "+", a + b, "toplama"
        
        elif islem == "-":
            a = random.randint(10, 20 * seviye)
            b = random.randint(1, a)
            return a, b, "-", a - b, "çıkarma"
        
        elif islem == "×":
            if seviye <= 4:
                a = random.choice([2, 3, 5, 10])
                b = random.randint(1, 5)
            else:
                a = random.randint(2, min(9, seviye))
                b = random.randint(1, min(10, seviye + 3))
            return a, b, "×", a * b, "çarpma"
        
        elif islem == "÷":
            b = random.randint(2, min(9, seviye + 1))
            cvp = random.randint(1, min(10, seviye + 2))
            a = b * cvp
            return a, b, "÷", cvp, "bölme"
    
    def oyun_dongusu(self):
        self.giris()
        
        for tur in range(1, 16):
            print(f"\n{'='*45}")
            print(f"🏆 TUR {tur} | Puan: {self.puan} | Seviye: {self.seviye}")
            print('='*45)
            
            kedi_emoji, kedi_adi, kedi_aciklama = random.choice(KEDILER)
            yemek = random.choice(YEMEKLER)
            
            print(f"\n{kedi_emoji} {kedi_adi}: '{yemek}' istiyorum! 🍴")
            
            a, b, islem, cvp, islem_adi = self.soru_uret(self.seviye)
            
            if islem == "+":
                soru = f"{a} + {b} = ?"
            elif islem == "-":
                soru = f"{a} - {b} = ?"
            elif islem == "×":
                soru = f"{a} × {b} = ?"
            else:
                soru = f"{a} ÷ {b} = ?"
            
            print(f"\n📝 Soru ({islem_adi}): {soru}")
            self.toplam_soru += 1
            
            try:
                kullanici_cvp = int(input("\n👉 Cevabın: "))
            except ValueError:
                print("😵 Sayı girmelisin!")
                kullanici_cvp = None
            
            if kullanici_cvp == cvp:
                self.puan += 10 * self.seviye
                self.dogru += 1
                print(f"\n🎉 DOĞRU! 🎉")
                print(f"😺 {kedi_adi}: 'Aaam! Lezzetli!' dedi.")
                print(f"   +{10 * self.seviye} puan!")
                
                if self.puan >= self.seviye * 80:
                    self.seviye += 1
                    print(f"\n🚀 SEVİYE ATLADIN! Seviye {self.seviye}")
                    if self.seviye == 3:
                        print("   🆕 Yeni: ÇIKARMA (-)")
                    elif self.seviye == 4:
                        print("   🆕 Yeni: ÇARPMA (×)")
                    elif self.seviye == 6:
                        print("   🆕 Yeni: BÖLME (÷)")
            else:
                print(f"\n😢 Yanlış... Doğru: {cvp}")
                print(f"😾 {kedi_adi}: 'Bir daha dene!' dedi.")
        
        print(f"""
        
{'='*50}
🎊 OYUN BİTTİ! 🎊
{'='*50}
📊 Doğru: {self.dogru}/{self.toplam_soru}
   🏆 Puan: {self.puan}
   📈 Seviye: {self.seviye}

🐱🌮 Şef Pofuduk:
   'Aferin Elif Miray! 👋'
""")

if __name__ == "__main__":
    oyun = MatematikKediOyunu()
    oyun.oyun_dongusu()