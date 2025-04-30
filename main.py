import tkinter as tk
from tkinter import ttk, messagebox
from kitap import Kitap
from kutuphane import Kutuphane
from uye import Uye

class KutuphaneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kütüphane Yönetim Sistemi")
        self.root.geometry("900x650")
        
        self.kutuphane = Kutuphane()
        
        # Ana sekme kontrolü
        self.tab_control = ttk.Notebook(root)
        
        # Sekmeleri oluştur
        self.tab_kitap = ttk.Frame(self.tab_control)
        self.tab_uye = ttk.Frame(self.tab_control)
        self.tab_odunc = ttk.Frame(self.tab_control)
        self.tab_rapor = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab_kitap, text='Kitap İşlemleri')
        self.tab_control.add(self.tab_uye, text='Üye İşlemleri')
        self.tab_control.add(self.tab_odunc, text='Ödünç İşlemleri')
        self.tab_control.add(self.tab_rapor, text='Raporlar')
        
        self.tab_control.pack(expand=1, fill="both")
        
        # Kitap İşlemleri Sekmesi
        self.setup_kitap_tab()
        
        # Üye İşlemleri Sekmesi
        self.setup_uye_tab()
        
        # Ödünç İşlemleri Sekmesi
        self.setup_odunc_tab()
        
        # Raporlar Sekmesi
        self.setup_rapor_tab()
    
    def setup_kitap_tab(self):
        # Kitap Ekleme Bölümü
        frame_kitap_ekle = ttk.LabelFrame(self.tab_kitap, text="Kitap İşlemleri", padding=10)
        frame_kitap_ekle.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(frame_kitap_ekle, text="Kitap ID:").grid(row=0, column=0, sticky="w")
        self.entry_kitap_id = ttk.Entry(frame_kitap_ekle)
        self.entry_kitap_id.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_kitap_ekle, text="Kitap Adı:").grid(row=1, column=0, sticky="w")
        self.entry_kitap_ad = ttk.Entry(frame_kitap_ekle)
        self.entry_kitap_ad.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(frame_kitap_ekle, text="Yazar:").grid(row=2, column=0, sticky="w")
        self.entry_kitap_yazar = ttk.Entry(frame_kitap_ekle)
        self.entry_kitap_yazar.grid(row=2, column=1, padx=5, pady=2)
        
        button_frame = ttk.Frame(frame_kitap_ekle)
        button_frame.grid(row=3, column=0, columnspan=2, pady=5)
        
        ttk.Button(button_frame, text="Kitap Ekle", command=self.kitap_ekle).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Kitap Sil", command=self.kitap_sil).pack(side="left", padx=5)
        
        # Kitap Listesi Bölümü
        frame_kitap_liste = ttk.LabelFrame(self.tab_kitap, text="Kitap Listesi", padding=10)
        frame_kitap_liste.pack(fill="both", expand=True, padx=5, pady=5)
        
        columns = ("id", "ad", "yazar", "durum")
        self.kitap_tree = ttk.Treeview(frame_kitap_liste, columns=columns, show="headings")
        
        self.kitap_tree.heading("id", text="ID")
        self.kitap_tree.heading("ad", text="Kitap Adı")
        self.kitap_tree.heading("yazar", text="Yazar")
        self.kitap_tree.heading("durum", text="Durum")
        
        self.kitap_tree.column("id", width=50)
        self.kitap_tree.column("ad", width=200)
        self.kitap_tree.column("yazar", width=150)
        self.kitap_tree.column("durum", width=100)
        
        scrollbar = ttk.Scrollbar(frame_kitap_liste, orient="vertical", command=self.kitap_tree.yview)
        self.kitap_tree.configure(yscrollcommand=scrollbar.set)
        
        self.kitap_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Treeview'a çift tıklama olayı ekle
        self.kitap_tree.bind("<Double-1>", self.kitap_secildi)
        
        self.kitap_listele()
    
    def setup_uye_tab(self):
        # Üye Ekleme Bölümü
        frame_uye_ekle = ttk.LabelFrame(self.tab_uye, text="Üye İşlemleri", padding=10)
        frame_uye_ekle.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(frame_uye_ekle, text="Üye ID:").grid(row=0, column=0, sticky="w")
        self.entry_uye_id = ttk.Entry(frame_uye_ekle)
        self.entry_uye_id.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_uye_ekle, text="Ad:").grid(row=1, column=0, sticky="w")
        self.entry_uye_ad = ttk.Entry(frame_uye_ekle)
        self.entry_uye_ad.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(frame_uye_ekle, text="Soyad:").grid(row=2, column=0, sticky="w")
        self.entry_uye_soyad = ttk.Entry(frame_uye_ekle)
        self.entry_uye_soyad.grid(row=2, column=1, padx=5, pady=2)
        
        button_frame = ttk.Frame(frame_uye_ekle)
        button_frame.grid(row=3, column=0, columnspan=2, pady=5)
        
        ttk.Button(button_frame, text="Üye Ekle", command=self.uye_ekle).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Üye Sil", command=self.uye_sil).pack(side="left", padx=5)
        
        # Üye Listesi Bölümü
        frame_uye_liste = ttk.LabelFrame(self.tab_uye, text="Üye Listesi", padding=10)
        frame_uye_liste.pack(fill="both", expand=True, padx=5, pady=5)
        
        columns = ("id", "ad", "soyad", "odunc_kitaplar")
        self.uye_tree = ttk.Treeview(frame_uye_liste, columns=columns, show="headings")
        
        self.uye_tree.heading("id", text="ID")
        self.uye_tree.heading("ad", text="Ad")
        self.uye_tree.heading("soyad", text="Soyad")
        self.uye_tree.heading("odunc_kitaplar", text="Ödünç Kitaplar")
        
        self.uye_tree.column("id", width=50)
        self.uye_tree.column("ad", width=100)
        self.uye_tree.column("soyad", width=100)
        self.uye_tree.column("odunc_kitaplar", width=200)
        
        scrollbar = ttk.Scrollbar(frame_uye_liste, orient="vertical", command=self.uye_tree.yview)
        self.uye_tree.configure(yscrollcommand=scrollbar.set)
        
        self.uye_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Treeview'a çift tıklama olayı ekle
        self.uye_tree.bind("<Double-1>", self.uye_secildi)
        
        self.uye_listele()
    
    def setup_odunc_tab(self):
        # Ödünç Verme Bölümü
        frame_odunc_ver = ttk.LabelFrame(self.tab_odunc, text="Kitap Ödünç Ver", padding=10)
        frame_odunc_ver.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(frame_odunc_ver, text="Kitap ID:").grid(row=0, column=0, sticky="w")
        self.entry_odunc_kitap_id = ttk.Entry(frame_odunc_ver)
        self.entry_odunc_kitap_id.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_odunc_ver, text="Üye ID:").grid(row=1, column=0, sticky="w")
        self.entry_odunc_uye_id = ttk.Entry(frame_odunc_ver)
        self.entry_odunc_uye_id.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(frame_odunc_ver, text="Kitap Ödünç Ver", command=self.kitap_odunc_ver).grid(row=2, column=1, pady=5)
        
        # İade Alma Bölümü
        frame_iade_al = ttk.LabelFrame(self.tab_odunc, text="Kitap İade Al", padding=10)
        frame_iade_al.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(frame_iade_al, text="Kitap ID:").grid(row=0, column=0, sticky="w")
        self.entry_iade_kitap_id = ttk.Entry(frame_iade_al)
        self.entry_iade_kitap_id.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_iade_al, text="Üye ID:").grid(row=1, column=0, sticky="w")
        self.entry_iade_uye_id = ttk.Entry(frame_iade_al)
        self.entry_iade_uye_id.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(frame_iade_al, text="Kitap İade Al", command=self.kitap_iade_al).grid(row=2, column=1, pady=5)
        
        # Ödünç Listesi Bölümü
        frame_odunc_liste = ttk.LabelFrame(self.tab_odunc, text="Ödünç Kayıtları", padding=10)
        frame_odunc_liste.pack(fill="both", expand=True, padx=5, pady=5)
        
        columns = ("kitap_id", "uye_id")
        self.odunc_tree = ttk.Treeview(frame_odunc_liste, columns=columns, show="headings")
        
        self.odunc_tree.heading("kitap_id", text="Kitap ID")
        self.odunc_tree.heading("uye_id", text="Üye ID")
        
        scrollbar = ttk.Scrollbar(frame_odunc_liste, orient="vertical", command=self.odunc_tree.yview)
        self.odunc_tree.configure(yscrollcommand=scrollbar.set)
        
        self.odunc_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.odunc_listele()
    
    def setup_rapor_tab(self):
        # Rapor Bölümü
        frame_rapor = ttk.LabelFrame(self.tab_rapor, text="Kütüphane Raporu", padding=10)
        frame_rapor.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.rapor_text = tk.Text(frame_rapor, height=10, wrap="word")
        scrollbar = ttk.Scrollbar(frame_rapor, orient="vertical", command=self.rapor_text.yview)
        self.rapor_text.configure(yscrollcommand=scrollbar.set)
        
        self.rapor_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        ttk.Button(frame_rapor, text="Raporu Güncelle", command=self.rapor_goster).pack(pady=5)
        
        self.rapor_goster()
    
    def kitap_secildi(self, event):
        selected_item = self.kitap_tree.focus()
        if selected_item:
            item_data = self.kitap_tree.item(selected_item)
            kitap_id = item_data['values'][0]
            self.entry_kitap_id.delete(0, tk.END)
            self.entry_kitap_id.insert(0, kitap_id)
    
    def uye_secildi(self, event):
        selected_item = self.uye_tree.focus()
        if selected_item:
            item_data = self.uye_tree.item(selected_item)
            uye_id = item_data['values'][0]
            self.entry_uye_id.delete(0, tk.END)
            self.entry_uye_id.insert(0, uye_id)
    
    def kitap_ekle(self):
        try:
            kitap_id = int(self.entry_kitap_id.get())
            kitap_ad = self.entry_kitap_ad.get()
            kitap_yazar = self.entry_kitap_yazar.get()
            
            if not kitap_ad or not kitap_yazar:
                messagebox.showerror("Hata", "Kitap adı ve yazar bilgileri boş olamaz!")
                return
            
            if self.kutuphane.kitap_ekle(Kitap(kitap_id, kitap_ad, kitap_yazar)):
                messagebox.showinfo("Başarılı", "Kitap başarıyla eklendi!")
                self.entry_kitap_id.delete(0, tk.END)
                self.entry_kitap_ad.delete(0, tk.END)
                self.entry_kitap_yazar.delete(0, tk.END)
                self.kitap_listele()
            else:
                messagebox.showerror("Hata", "Bu ID'de kitap zaten var!")
        except ValueError:
            messagebox.showerror("Hata", "Kitap ID sayı olmalıdır!")
    
    def kitap_sil(self):
        try:
            kitap_id = int(self.entry_kitap_id.get())
            
            if kitap_id in self.kutuphane.kitaplar:
                # Kitap ödünçte mi kontrol et
                if kitap_id in self.kutuphane.odunc_islem.odunc_kayitlari:
                    messagebox.showerror("Hata", "Bu kitap ödünçte olduğu için silinemez!")
                    return
                
                del self.kutuphane.kitaplar[kitap_id]
                messagebox.showinfo("Başarılı", "Kitap başarıyla silindi!")
                self.entry_kitap_id.delete(0, tk.END)
                self.entry_kitap_ad.delete(0, tk.END)
                self.entry_kitap_yazar.delete(0, tk.END)
                self.kitap_listele()
                self.odunc_listele()
            else:
                messagebox.showerror("Hata", "Bu ID'de kitap bulunamadı!")
        except ValueError:
            messagebox.showerror("Hata", "Kitap ID sayı olmalıdır!")
    
    def uye_ekle(self):
        try:
            uye_id = int(self.entry_uye_id.get())
            uye_ad = self.entry_uye_ad.get()
            uye_soyad = self.entry_uye_soyad.get()
            
            if not uye_ad or not uye_soyad:
                messagebox.showerror("Hata", "Ad ve soyad bilgileri boş olamaz!")
                return
            
            if self.kutuphane.uye_ekle(Uye(uye_id, uye_ad, uye_soyad)):
                messagebox.showinfo("Başarılı", "Üye başarıyla eklendi!")
                self.entry_uye_id.delete(0, tk.END)
                self.entry_uye_ad.delete(0, tk.END)
                self.entry_uye_soyad.delete(0, tk.END)
                self.uye_listele()
            else:
                messagebox.showerror("Hata", "Bu ID'de üye zaten var!")
        except ValueError:
            messagebox.showerror("Hata", "Üye ID sayı olmalıdır!")
    
    def uye_sil(self):
        try:
            uye_id = int(self.entry_uye_id.get())
            
            if uye_id in self.kutuphane.uyeler:
                # Üyenin ödünç kitapları var mı kontrol et
                if self.kutuphane.uyeler[uye_id].odunc_kitaplar:
                    messagebox.showerror("Hata", "Bu üyenin ödünç kitapları olduğu için silinemez!")
                    return
                
                del self.kutuphane.uyeler[uye_id]
                messagebox.showinfo("Başarılı", "Üye başarıyla silindi!")
                self.entry_uye_id.delete(0, tk.END)
                self.entry_uye_ad.delete(0, tk.END)
                self.entry_uye_soyad.delete(0, tk.END)
                self.uye_listele()
            else:
                messagebox.showerror("Hata", "Bu ID'de üye bulunamadı!")
        except ValueError:
            messagebox.showerror("Hata", "Üye ID sayı olmalıdır!")
    
    def kitap_odunc_ver(self):
        try:
            kitap_id = int(self.entry_odunc_kitap_id.get())
            uye_id = int(self.entry_odunc_uye_id.get())
            
            if kitap_id in self.kutuphane.kitaplar and uye_id in self.kutuphane.uyeler:
                if self.kutuphane.odunc_islem.odunc_ver(self.kutuphane.kitaplar[kitap_id], self.kutuphane.uyeler[uye_id]):
                    messagebox.showinfo("Başarılı", "Kitap ödünç verildi!")
                    self.entry_odunc_kitap_id.delete(0, tk.END)
                    self.entry_odunc_uye_id.delete(0, tk.END)
                    self.kitap_listele()
                    self.uye_listele()
                    self.odunc_listele()
                else:
                    messagebox.showerror("Hata", "Kitap zaten ödünçte!")
            else:
                messagebox.showerror("Hata", "Geçersiz kitap veya üye ID!")
        except ValueError:
            messagebox.showerror("Hata", "Kitap ID ve Üye ID sayı olmalıdır!")
    
    def kitap_iade_al(self):
        try:
            kitap_id = int(self.entry_iade_kitap_id.get())
            uye_id = int(self.entry_iade_uye_id.get())
            
            if kitap_id in self.kutuphane.kitaplar and uye_id in self.kutuphane.uyeler:
                if self.kutuphane.odunc_islem.iade_al(self.kutuphane.kitaplar[kitap_id], self.kutuphane.uyeler[uye_id]):
                    messagebox.showinfo("Başarılı", "Kitap iade alındı!")
                    self.entry_iade_kitap_id.delete(0, tk.END)
                    self.entry_iade_uye_id.delete(0, tk.END)
                    self.kitap_listele()
                    self.uye_listele()
                    self.odunc_listele()
                else:
                    messagebox.showerror("Hata", "Bu üye bu kitabı ödünç almamış!")
            else:
                messagebox.showerror("Hata", "Geçersiz kitap veya üye ID!")
        except ValueError:
            messagebox.showerror("Hata", "Kitap ID ve Üye ID sayı olmalıdır!")
    
    def kitap_listele(self):
        # Treeview'ı temizle
        for item in self.kitap_tree.get_children():
            self.kitap_tree.delete(item)
        
        # Kitapları ekle
        for kitap in self.kutuphane.kitaplar.values():
            self.kitap_tree.insert("", "end", values=(kitap.id, kitap.ad, kitap.yazar, kitap.durum))
    
    def uye_listele(self):
        # Treeview'ı temizle
        for item in self.uye_tree.get_children():
            self.uye_tree.delete(item)
        
        # Üyeleri ekle
        for uye in self.kutuphane.uyeler.values():
            odunc_kitaplar = ", ".join(map(str, uye.odunc_kitaplar)) if uye.odunc_kitaplar else "Yok"
            self.uye_tree.insert("", "end", values=(uye.id, uye.ad, uye.soyad, odunc_kitaplar))
    
    def odunc_listele(self):
        # Treeview'ı temizle
        for item in self.odunc_tree.get_children():
            self.odunc_tree.delete(item)
        
        # Ödünç kayıtlarını ekle
        for kitap_id, uye_id in self.kutuphane.odunc_islem.odunc_kayitlari.items():
            self.odunc_tree.insert("", "end", values=(kitap_id, uye_id))
    
    def rapor_goster(self):
        self.rapor_text.delete(1.0, tk.END)
        self.rapor_text.insert(tk.END, f"Toplam Kitap: {len(self.kutuphane.kitaplar)}\n")
        self.rapor_text.insert(tk.END, f"Toplam Üye: {len(self.kutuphane.uyeler)}\n")
        self.rapor_text.insert(tk.END, f"Ödünçteki Kitaplar: {len(self.kutuphane.odunc_islem.odunc_kayitlari)}\n\n")
        
        # Ödünçteki kitapların detayları
        self.rapor_text.insert(tk.END, "Ödünçteki Kitaplar:\n")
        for kitap_id, uye_id in self.kutuphane.odunc_islem.odunc_kayitlari.items():
            kitap = self.kutuphane.kitaplar[kitap_id]
            uye = self.kutuphane.uyeler[uye_id]
            self.rapor_text.insert(tk.END, f"- {kitap.ad} (ID: {kitap.id}) -> {uye.ad} {uye.soyad} (ID: {uye.id})\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = KutuphaneApp(root)
    root.mainloop()