kontak = {'Ari':'081267888', 'Dina' : '087677776'}
print ( "| Nama   | Nomor Telepon |" )
print ( 21 * "=" )
print ( " # Ari  | " , kontak ['Ari']) 
print ( " # Dina | " , kontak ['Dina'])
print ( 21 * "=" )

print ( "Tampilkan kontaknya Ari" )
print ( " Nama | Nomor Telepon " )
print ( " Ari  | " , kontak ["Ari"])

print ( "\nTambah kontak baru dengan nama Riko, nomor 087654544" )
kontak ["Riko"] = "087654544"
print ( " Nama | Nomor Telepon " )
print ( " Riko | " , kontak ["Riko"])

print ("\nUbah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = "088999776"
print ( " Nama | Nomor Telepon " )
print ( " Dina | " ,kontak ['Dina'])

print ( "\nTampilkan semua nama" )
print (kontak.keys())

print ( "\nTampilkan semua Nomor" )
print ( kontak.values())

print ( "\nTampilkan daftar nama dan nomornya" )
print ( " Nama | Nomor Telepon " )
print (21*"=")
for a in kontak:
      print(a, ' |', kontak[a])

print ( "\nHapus kontak Dina" )
del kontak["Dina"]
print ( kontak.items ())  