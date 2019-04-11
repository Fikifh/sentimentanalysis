import csv

siswa = [
    ('arslan', 'A', 90),
    ('bayu', 'B', 85),
    ('niko', 'A', 80),
    ('abdul', 'B', 90),
    ('dahlan', 'C', 70)
]

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('siswa.csv', 'w')
w = csv.writer(f)
w.writerow(('Nama','Kelas','Nilai'))

# menulis file csv
for s in siswa:
    w.writerow(s)

# menutup file csv
f.close()