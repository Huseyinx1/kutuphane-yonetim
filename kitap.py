class Kitap:
    def __init__(self, id, ad, yazar):
        self.id = id
        self.ad = ad
        self.yazar = yazar
        self.durum = "Mevcut"
    
    def bilgileri_goster(self):
        return f"ID: {self.id} | Ad: {self.ad} | Yazar: {self.yazar} | Durum: {self.durum}"