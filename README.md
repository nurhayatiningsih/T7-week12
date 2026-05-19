# T7-week12

# Tugas 6 - Visualisasi Data Dashboard PySide6

Nama: Nurhayati Ningsih
NIM : F1D02410085
Kelas: C

# Penjelasan 
Aplikasi ini dibuat untuk menampilkan data penjualan supermarket dalam bentuk dashboard. Data yang berisi ribuan transaksi tersebut divisualisasikan menjadi bentuk tabel, ringkasan angka, serta grafik interaktif yang dapat disaring berdasarkan kategori tertentu. Program dibuat menggunakan PySide6 untuk antarmukanya, Pandas untuk pengolahan datanya, dan Matplotlib untuk menggambar grafiknya.
Data yang digunakan berasal dari dataset nyata Kaggle yaitu Supermarket Sales Dataset, yang bisa diakses pada tautan berikut:https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales
Karena dataset asli memiliki format yang sedikit berbeda, program secara otomatis menyesuaikan nama kolom dan menangani beberapa perbedaan format agar data bisa diproses dengan baik. Berikut adalah penjelasan mengenai kolom-kolom utama yang dipakai dalam dashboard ini:

| Kolom         | Keterangan                                                    | 
| :--- | :---: | 
| invoice_id    | Kode identitas unik untuk setiap transaksi                    | 
| branch        | Kode cabang toko tempat transaksi terjadi (A, B, atau C)      | 
| city          | Nama kota lokasi cabang toko                                  | 
| customer_type | Status jenis pelanggan, baik Member maupun Normal             | 
| gender        | Jenis kelamin pelanggan                                       | 
| product_line  | Kategori dari produk yang dibeli                              | 
| unit_price    | Harga satuan dari barang yang dibeli dalam dolar              | 
| quantity      | Jumlah unit barang yang dibeli dalam satu transaksi           | 
| total         | Total keseluruhan biaya yang harus dibayar termasuk pajak     | 
| date          | Tanggal saat transaksi tersebut dilakukan                     | 
| payment       | Metode yang dipilih pelanggan untuk melakukan pembayaran      | 
| rating        | Nilai penilaian yang diberikan pelanggan setelah bertransaksi | 

Di dalam dashboard ini tersedia lima kartu ringkasan di bagian atas yang menampilkan informasi seperti total pendapatan, jumlah transaksi, hingga rata-rata rating. Data mentahnya sendiri ditampilkan secara lengkap pada tabel menggunakan QTableWidget. Untuk bagian grafik, program menyediakan lima pilihan tampilan yang bisa diganti melalui dropdown, mulai dari grafik batang horizontal, pie chart, grafik garis tren harian, hingga grafik batang terkelompok. Pengguna juga dapat menyaring data yang ditampilkan melalui lima filter berbeda seperti cabang toko, kota, tipe pelanggan, kategori produk, dan metode pembayaran. Setiap perubahan pada filter akan langsung memperbarui tabel, grafik, dan angka ringkasan secara bersamaan. Program juga dilengkapi dengan pesan konfirmasi menggunakan QMessageBox pada saat aksi penting seperti mereset filter, memuat ulang data, mengekspor grafik, hingga menutup aplikasi.

# Hasil Screenshot
1. Tampilan Awal Aplikasi
![alt text](<Screenshot/Tampilan Awal.png>)
Pada tampilan awal, aplikasi langsung memuat seluruh data tanpa ada filter yang diterapkan. Bagian paling atas menampilkan lima kartu ringkasan yang merangkum informasi utama seperti total pendapatan, jumlah transaksi, hingga rata-rata rating. Di bawahnya terdapat panel kontrol yang kondisinya masih default "Semua". Visualisasi pertama yang muncul adalah grafik batang horizontal (Bar Chart) yang membandingkan total penjualan di setiap kategori produk. Sementara itu, bagian bawah layar diisi oleh tabel data mentah yang menampilkan detail transaksi secara lengkap.
2. Tampilan Tipe Pie Chart
![alt text](<Screenshot/Tampilan Tipe Pie Chart.png>)
Pada tampilan ini, jika mengubah pilihan tipe chart pada dropdown menjadi "Pie Chart". Grafik yang muncul menggambarkan proporsi atau distribusi penjualan berdasarkan cabang toko. Dari visualisasi tersebut terlihat jelas perbandingan presentase kontribusi tiap cabang terhadap total penjualan keseluruhan, dengan keterangan lengkap yang tertulis di samping tiap potongan pie. Angka-angka pada kartu ringkasan di atas tetap menyesuaikan dengan data yang sedang ditampilkan.
3. Tampilan Tipe Line Chart
![alt text](<Screenshot/Tampilan Tipe Line Chart.png>)
Pada tampilan ini, tipe chart diganti ke bentuk grafik garis (Line Chart). Visualisasi ini secara spesifik menunjukkan pola atau tren total penjualan dari hari ke hari selama periode tertentu. Dengan adanya garis yang menghubungkan titik-titik data, pengguna bisa dengan mudah melihat fluktuasi naik turunnya penjualan harian, termasuk mencari tahu kapan penjualan mencapai puncak atau mengalami penurunan.
4. Tampilan Tipe Grouped Bar
![alt text](<Screenshot/Tampilan Tipe Bar Chart_Metode Pembayaran.png>)
Untuk tampilan berikutnya, bisa diubah pilihan ke "Grouped Bar — Cabang & Tipe Pelanggan". Jenis grafik ini menampilkan batang yang tersusun berdampingan di setiap cabang toko. Warna yang berbeda pada batang tersebut mewakili status pelanggan, apakah itu Member atau Normal. Susunan seperti ini memudahkan pengguna untuk melihat perbandingan pendapatan dari dua kategori sekaligus di dalam satu area grafik yang sama, tanpa harus membuat dua grafik terpisah.
5. Tampilan Tipe Bar Chart_Metode Pembayaran
![alt text](<Screenshot/Tampilan Tipe Bar Chart_Metode Pembayaran.png>)
Pada tampilan ini, jika memilih tipe grafik "Bar Chart — Metode Pembayaran". Visualisasi yang ditampilkan berupa grafik batang vertikal yang merangkum total pendapatan berdasarkan cara pelanggan melakukan pembayaran. Dari tinggi batang yang ada, terlihat perbedaan jumlah uang yang masuk dari masing-masing metode seperti Credit Card, Cash, dan Ewallet. Detail angka pastinya juga langsung tercantum di bagian atas setiap batang agar informasinya lebih mudah dibaca.
6. Tampilan Setelah Memilih Filter Kontrol 1
![alt text](<Screenshot/Tampilan Setelah Memilih Filter Kontrol 1.png>)
Pada tampilan ini, salah satu filter pada panel kontrol telah dipilih. Langsung setelahnya, seluruh isi dashboard berubah secara otomatis. Angka pada kartu ringkasan langsung berkurang karena menyesuaikan dengan data yang terfilter. Grafik batang juga hanya menampilkan kategori produk yang ada di dalam filter tersebut, dan tabel data di bagian bawah hanya memunculkan baris-baris yang memenuhi kriteria filter saja.
7. Tampilan Setelah Memilih Filter Kontrol 2
![alt text](<Screenshot/Tampilan Setelah Memilihi Filter Kontrol 2.png>)
Tampilan ini menunjukkan penggunaan filter yang berbeda dari sebelumnya. Terlihat bahwa pilihan filter baru menghasilkan kombinasi data yang berbeda pula. Grafik batang dengan cepat menggambar ulang batangnya untuk menampilkan data kategori yang relevan saja, begitu pula dengan isi tabel yang langsung berganti tanpa perlu me-refresh halaman.
8. Tampilan Setelah Memilih Filter Kontrol 3
![alt text](<Screenshot/Tampilan Setelah Memilihi Filter Kontrol 3.png>)
Pada tangkapan layar ini, filter diubah lagi ke kategori yang lain. Hal ini membuktikan bahwa fitur filter berjalan dengan sangat responsif. Setiap pergantian pilihan dropdown langsung memicu perhitungan ulang terhadap data yang ditampilkan, sehingga pengguna bisa dengan leluasa mengeksplorasi data dari berbagai sudut pandang hanya dengan mengklik pilihan filter.
9. Tampilan Setelah Memilih Filter dengan 100% Chart
![alt text](<Screenshot/Tampilan Setelah Memilihi Filter Kontrol dengan 100% Chart.png>)
Tampilan ini menunjukkan hasil filter yang sangat spesifik, di mana data yang tersisa hanya berasal dari satu cabang saja. Karena hanya ada satu cabang yang tersedia, pie chart yang ditampilkan menunjukkan persentase penuh 100% pada cabang tersebut. Hal ini menunjukkan bagaimana dashboard merespons kondisi data yang sangat sempit namun tetap akurat.
10. Tampilan Tidak Ada Data
![alt text](<Screenshot/Tampilan Jika Tidak Ada Data.png>)
Setelah memilih filter kontrol, akan ada beberapa data yang tidak ada.
11. Tampilan Ingin Ekspor Chart
![alt text](<Screenshot/Konfirmasi Ingin Export Chart ke PNG.png>)
Sebelum menyimpan, akan muncul konfirmasi benar ingin menyimpan chart atau tidak.
12. Tampilan Simpan Chart
![alt text](<Screenshot/Tampilan Simpan Chart.png>)
Pada tangkapan layar ini terlihat jendela dialog bawaan sistem ketika pengguna menekan tombol "Export Chart ke PNG". Dialog ini memungkinkan pengguna untuk menentukan lokasi penyimpanan dan nama file untuk gambar grafik yang sedang ditampilkan, sehingga hasil visualisasi bisa disimpan dan digunakan untuk keperluan pelaporan lainnya.
13. Tampilan Konfirmasi Berhasil Disimpan
![alt text](<Screenshot/Konfirmasi Chart Berhasil di Simpan.png>)
Setelah Menyimpan Chartnya sesuai yang diinginkan, maka akan muncul pesan berhasil disimpan.
14. Bukti Chart Sudah Tersimpan
![alt text](<Screenshot/Bukti Chart Sudah Tersimpan.png>)
Setelah berhasil disimpan, akan ada png yang tersimpan didalam folder sesuai tempay menyimpan sebelumnya.
15. Konfirmasi Refresh Data
![alt text](<Screenshot/Konfirmasi Refres Data.png>)
Saat klik refresh maka adan ada konfirmasi ingin memuat ulang datanya atau tidak.
16. Konfirmasi Reset Filter
![alt text](<Screenshot/Konfirmasi Reset Filter.png>)
Sama halnya dengan refresh, reset filter juga akan muncul pesan konfirmasi untuk memastikan benar di reset atau tidak
17. Tampilan Setelah di Reset
![alt text](<Screenshot/Tampilan Setelah di Reset.png>)
Jika saat pesan konfirmasi muncul dan tekan iya, maka data akan di reset.










