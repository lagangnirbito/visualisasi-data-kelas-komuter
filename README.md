# Kata Pengantar

Repository ini dibuat sebagai awal saya mempelajari bahasa pemrograman Python. Pelajaran ini saya dapatkan dengan mengikuti program Pro Academy Digitalent yang diselenggarakan oleh KOMINFO & CISCO. Berawal dari ini saya melanjutkan perjalanan saya untuk mempelajari DBMS, SQL hingga PostgreSQL hingga visualisasi data menggunakan Tableau dan Grafana.

Repository ini juga dibuat sebagai rekaman dan catatan saya dalam menjalani petualangan ini. Semoga juga bisa memberikan manfaat bagi yang melihat dan membutuhkan.

Repository ini berisikan EDA dan Visualisasi data yang saya ambil dari kaggle.com mengenai kepuasan hidup para komuter atau mereka yang menggunakan commuter transportation untuk pergi bekerja.

# Sumber Data

Data yang digunakan

```bash
curl -L -O https://www.kaggle.com/datasets/rezkyyayang/kepuasanhidupkomuter/download?datasetVersionNumber=1
```

# Tipe Data

Karena data ini ditujukan untuk mengetahui tingkat kepuasan hidup, maka tipe data yang ada pada dataset tersebut didominasi tipe data kategorik-ordinal, seperti contoh pada kolom "Status Pernikahan", "Tingkat Pendidikan", "Rumah" serta kolom "Kepuasan Hidup"


# Library yang digunakan

Library yang digunakan pada proses visualisasi kali ini adalah Numpy, Pandas dan Matplotlib.


```python
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
```

# Hasil Visualisasi
Disini saya melakukan eksplorasi, visualisasi dan analisa pada:
 - Sebaran umur pada pengguna komuter pada kelompok kelamin Wanita dan Pria
 - Sebaran status pernikahan pengguna komuter
 - Sebaran Kelompok Wanita dan Pria pada variabel "Rasio Ketergantungan" dan "Jenis Pekerjaan"
 - Sebaran "Jenis Pekerjaan" dan "Pendapatan" pada kelompok kelamin Wanita dan Pria
 - Respon "Hidup lebih baik bila tidak menggunakan komuter saat bekerja" dengan variabel "Besar Pendapatan dan "Rasio Ketergantungan" pada kelompok Pria Lajang dan Pria Menikah
 - Respon "Hidup lebih baik bila tidak menggunakan komuter saat bekerja" dengan variabel "Besar Pendapatan dan "Rasio Ketergantungan" pada kelompok Wanita Lajang dan Wanita Menikah
 - Jumlah dan Sebaran Responden yang menjawab kualitas hidup "Sangat Puas" dengan variabel "Besar Pendapatan" dan "Rasio Ketergantungan" pada kelompok Wanita dan Kelompok Pria
 - Sebaran respon kepuasan hidup

# Kekurangan

Proses analisa dan visualisasi masih bisa dikembangkan lagi, baik dari aspek statistik maupun ketajaman eksplorasi.