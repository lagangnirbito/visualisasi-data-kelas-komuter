import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#Proses read data excel ke library panda, dan ubah nama beberapa kolom
data_commuter_excel_read = pd.read_excel('data_commuter.xlsx')
df_data_commuter = pd.DataFrame(data_commuter_excel_read)
df_data_commuter.rename(columns={'A.1':'Kelamin','A.2':'Umur','A.3':'Pernikahan','A.4':'Pendidikan','A.5':'Agama','A.6':'Pekerjaan','B.1':'Keterjangkauan Harga Rumah','B.2':'Kemampuan Membeli Rumah', 'C.1':'Jumlah Anggota Keluarga Yang Bekerja', 'C.2':'Jumlah Anggota Keluarga Tidak Bekerja', 'C.3':'Total Anggota Keluarga', 'C.4':'Rasio Ketergantungan', 'D.1':'Pendapatan Sebagai Komuter Besar', 'D.2':'Pendapatan Sebagai Komuter Sepadan', 'D.3':'Waktu Kerja Sebanding Dengan Pendapatan', 'D.4':'Pendapatan Perbulan', 'D.5':'Pendapatan Perbulan (Dollar)'},inplace=True)


#Grafik sederhana Mayoritas
plt.figure()
grafik_kelamin = df_data_commuter['Kelamin'].value_counts().plot(kind='bar')
grafik_kelamin.set_xlabel('Kelamin')
grafik_kelamin.set_ylabel('Frekuensi')
grafik_kelamin.set_title('Jenis Kelamin Komuter')
grafik_kelamin.set_xticklabels(['Pria', 'Wanita'], rotation=0)

grafik_pernikahan = df_data_commuter['Pernikahan'].value_counts().plot(kind='bar')
grafik_pernikahan.set_xlabel('Status Pernikahan')
grafik_pernikahan.set_ylabel('Frekuensi')
grafik_pernikahan.set_title('Status Pernikahan Komuter')
grafik_pernikahan.set_xticklabels(['Menikah', 'Lajang',  'Duda', 'Janda'], rotation=0)

plt.figure()
grafik_kepuasan = df_data_commuter['Kepuasan Hidup'].value_counts().plot(kind='pie',autopct='%1.1f%%')
grafik_kepuasan.set_title('Kepuasan Hidup Komuter')
grafik_kepuasan.yaxis.set_visible(False)


#grafik kepuasan (?)
dataframe_kelamin_kepuasan = df_data_commuter[['Kepuasan Hidup', 'Kelamin']]


#Mencari Jumlah Kelamin dan Umur
Data_Kolom_Kelamin = (df_data_commuter['Kelamin'].tolist())
Data_Kolom_Kelamin_Detil = []
for i in Data_Kolom_Kelamin:
    if i == 1:
        Data_Kolom_Kelamin_Detil.append('Pria')
    elif i == 2:
        Data_Kolom_Kelamin_Detil.append('Wanita')
    else:
        Data_Kolom_Kelamin_Detil.append((i))
Data_Kolom_Umur = (df_data_commuter['Umur'])
Data_Kolom_Umur_Detil = []
for i in Data_Kolom_Umur:
    if i >0:
        Data_Kolom_Umur_Detil.append(i)
    else:
        Data_Kolom_Umur_Detil.append(i)

#Membuat Pengelompokan Dict Pria:[Umur] dan Wanita:[Umur]
Kelamin_Umur = {}
for i in range(len(Data_Kolom_Kelamin_Detil)):
    if Data_Kolom_Kelamin_Detil[i] not in Kelamin_Umur:
        Kelamin_Umur[Data_Kolom_Kelamin_Detil[i]] = [Data_Kolom_Umur_Detil[i]]
    Kelamin_Umur[Data_Kolom_Kelamin_Detil[i]].append(Data_Kolom_Umur_Detil[i])

#Cek Jumlah, Umur minimum dan Maksimum
Jumlah_Komuter_Pria = len(Kelamin_Umur['Pria'])
Jumlah_Komuter_Wanita = len(Kelamin_Umur['Wanita'])
Kelamin_Umur_Urut = {key: sorted(value) for key, value in Kelamin_Umur.items()}
Umur_Minimum_Pria = Kelamin_Umur_Urut['Pria'][0]
Umur_Maksimum_Pria = Kelamin_Umur_Urut['Pria'][-1]
Umur_Minimum_Wanita = Kelamin_Umur_Urut['Wanita'][0]
Umur_Maksimum_Wanita = Kelamin_Umur_Urut['Wanita'][-1]
(' Umur Responden Pria Termuda: ', Umur_Minimum_Pria,'\n','Umur Responden Pria Tertua: ', Umur_Maksimum_Pria,'\n', 'Umur Responden Wanita Termuda: ',Umur_Minimum_Wanita,'\n', 'Umur Responden Wanita Tertua: ', Umur_Maksimum_Wanita)
Kelamin_Umur_Urut_Pria = [x for x in Kelamin_Umur_Urut['Pria']]
Kelamin_Umur_Urut_Wanita = [x for x in Kelamin_Umur_Urut['Wanita']]

#pembuatan grafik histogram
plt.figure()
plt.hist(Kelamin_Umur_Urut_Pria, bins=35, width= 0.5)
plt.title('Sebaran Umur Pengguna Komuter Kelompok Kelamin Pria\nTotal Responden: {} Orang'.format(Jumlah_Komuter_Pria))
plt.xlabel('Rentang Umur Responden: {} Tahun Hingga {} Tahun'.format(Umur_Minimum_Pria, Umur_Maksimum_Pria))
plt.ylabel('Frekuensi')
plt.figure()
plt.hist(Kelamin_Umur_Urut_Wanita, bins=35, width= 1)
plt.title('Sebaran Umur Pengguna Komuter Kelompok Kelamin Wanita\nTotal Responden: {} Orang'.format(Jumlah_Komuter_Wanita))
plt.xlabel('Rentang Umur Responden: {} Tahun Hingga {} Tahun'.format(Umur_Minimum_Wanita, Umur_Maksimum_Wanita))
plt.ylabel('Frekuensi')

#Membuat hubungan Pekerjaan, Kelamin dan Rasio Ketergantungan
Data_Kolom_Pekerjaan = df_data_commuter['Pekerjaan'].tolist()
Data_Kolom_Pekerjaan_Detil = []
for i in range(len(Data_Kolom_Pekerjaan)):
    if Data_Kolom_Pekerjaan[i] == 1:
        Data_Kolom_Pekerjaan_Detil.append('PNS')
    elif Data_Kolom_Pekerjaan[i] == 2:
        Data_Kolom_Pekerjaan_Detil.append('Polisi/Militer')
    elif Data_Kolom_Pekerjaan[i] == 3:
        Data_Kolom_Pekerjaan_Detil.append('Pegawai Swasta')
    elif Data_Kolom_Pekerjaan[i] == 4:
        Data_Kolom_Pekerjaan_Detil.append('Wirausaha')
    else:
        Data_Kolom_Pekerjaan_Detil.append('Lainnya')
data_commuter_excel_read2 = pd.read_excel('data_commuter.xlsx')
Data_Kolom_Rasio = df_data_commuter['Rasio Ketergantungan']
Data_Kolom_Rasio_Detil_Float = [float(x) for x in Data_Kolom_Rasio]

#Menggabungkan data Kelamin dengan Pekerjaan dan Rasio
Pekerjaan_Rasio_Zip =  zip(Data_Kolom_Pekerjaan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pekerjaan_Rasio_Zip_Zip = zip(Data_Kolom_Kelamin_Detil, Pekerjaan_Rasio_Zip)
Kelamin_Pekerjaan_Rasio_Dict = {}
for gender, data in Kelamin_Pekerjaan_Rasio_Zip_Zip:
    if gender in Kelamin_Pekerjaan_Rasio_Dict:
        Kelamin_Pekerjaan_Rasio_Dict[gender].append(data)
    else:
        Kelamin_Pekerjaan_Rasio_Dict[gender] = [data]
List_Kelamin_Pekerjaan_Rasio_Dict_Pria = Kelamin_Pekerjaan_Rasio_Dict['Pria']
List_Kelamin_Pekerjaan_Rasio_Dict_Wanita = Kelamin_Pekerjaan_Rasio_Dict['Wanita']
plt.figure()
x_Kelamin_Pekerjaan_Rasio_Pria = [t[0] for t in List_Kelamin_Pekerjaan_Rasio_Dict_Pria]
y_Kelamin_Pekerjaan_Rasio_Pria = [t[1] for t in List_Kelamin_Pekerjaan_Rasio_Dict_Pria]
x_Kelamin_Pekerjaan_Rasio_Wanita = [t[0] for t in List_Kelamin_Pekerjaan_Rasio_Dict_Wanita]
y_Kelamin_Pekerjaan_Rasio_Wanita = [t[1] for t in List_Kelamin_Pekerjaan_Rasio_Dict_Wanita]
ytick_positions = [i/5 for i in range(100)]
ytick_labels = [str(i) for i in ytick_positions]
plt.yticks(ytick_positions, ytick_labels)
plt.scatter(x_Kelamin_Pekerjaan_Rasio_Pria, y_Kelamin_Pekerjaan_Rasio_Pria, color='blue', label='Pria')
plt.scatter(x_Kelamin_Pekerjaan_Rasio_Wanita, y_Kelamin_Pekerjaan_Rasio_Wanita, color='orange', label='Wanita')
plt.legend()
plt.xlabel('Jenis Pekerjaan')
plt.ylabel('Rasio Ketergantungan')
plt.title('Grafik Kelamin, Pekerjaan dan Rasio Ketergantungan')


#menghitung rata-rata rasio ketergantungan tiap kelamin
Rasio_Pria = []
Rasio_Wanita = []
for x,y in List_Kelamin_Pekerjaan_Rasio_Dict_Pria:
    if y > -1:
        Rasio_Pria.append(y)
    else:
        pass
for x,y in List_Kelamin_Pekerjaan_Rasio_Dict_Wanita:
    if y > -1:
        Rasio_Wanita.append(y)
    else:
        pass





#Grafik Pendapatan, Rasio dengan Pekerjaan-Kelamin
Data_Kolom_Pekerjaan_Detil
Data_Kolom_Pekerjaan_Detil
Data_Kolom_Rasio_Detil_Float
Data_Kolom_Pendapatan = df_data_commuter['Pendapatan Perbulan']
Data_Kolom_Pendapatan_Detil = [x for x in Data_Kolom_Pendapatan]

# zip pekerjaan dengan pendapatan dan rasio, lalu dijadikan dictionary
Kelamin_Pekerjaan_Pendapatan_Rasio_Zip = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pekerjaan_Detil, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pekerjaan_Pendapatan_Rasio_Dict = {}
for kelamin, pekerjaan, pendapatan, rasio in Kelamin_Pekerjaan_Pendapatan_Rasio_Zip:
    if kelamin in Kelamin_Pekerjaan_Pendapatan_Rasio_Dict:
        Kelamin_Pekerjaan_Pendapatan_Rasio_Dict[kelamin].append((pekerjaan, pendapatan, rasio))
    else:
        Kelamin_Pekerjaan_Pendapatan_Rasio_Dict[kelamin] = [(pekerjaan, pendapatan, rasio)]
List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Pria = Kelamin_Pekerjaan_Pendapatan_Rasio_Dict['Pria']
List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Wanita = Kelamin_Pekerjaan_Pendapatan_Rasio_Dict ['Wanita']

#menghitung rata-rata pendapatan per kelamin
Pendapatan_Pria = [List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Pria[i][1] for i in range(len(List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Pria))]
Pendapatan_Wanita = [List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Wanita[i][1] for i in range(len(List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Wanita))]

#pembuatan Grafik Pekerjaan Pendapatan Rasio berdasarkan kelompok kelamin
#pria
List_Pria_Lainnya_Pendapatan_Rasio = []
List_Pria_PNS_Pendapatan_Rasio = []
List_Pria_PegawaiSwasta_Pendapatan_Rasio = []
List_Pria_PolisiMiliter_Pendapatan_Rasio = []
List_Pria_Wirausaha_Pendapatan_Rasio = []
for pekerjaan, pendapatan, rasio in List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Pria:
    if pekerjaan == 'Lainnya':
        List_Pria_Lainnya_Pendapatan_Rasio.append((pendapatan, rasio))
    elif pekerjaan == 'PNS':
        List_Pria_PNS_Pendapatan_Rasio.append((pendapatan, rasio))
    elif pekerjaan == 'Polisi/Militer':
        List_Pria_PolisiMiliter_Pendapatan_Rasio.append((pendapatan, rasio))
    elif pekerjaan == 'Pegawai Swasta':
        List_Pria_PegawaiSwasta_Pendapatan_Rasio.append((pendapatan, rasio))
    else:
        List_Pria_Wirausaha_Pendapatan_Rasio.append((pendapatan, rasio))

plt.figure()
x_Pria_Pns_Pendapatan_Rasio = [t[1] for t in List_Pria_PNS_Pendapatan_Rasio]
x_Pria_PegawaiSwasta_Pendapatan_Rasio = [t[1] for t in List_Pria_PegawaiSwasta_Pendapatan_Rasio]
x_Pria_PolisiMiliter_Pendapatan_Rasio = [t[1] for t in List_Pria_PolisiMiliter_Pendapatan_Rasio]
x_Pria_Lainnya_Pendapatan_Rasio = [t[1] for t in List_Pria_Lainnya_Pendapatan_Rasio]
x_Pria_Wirausaha_Pendapatan_Rasio = [t[1] for t in List_Pria_Wirausaha_Pendapatan_Rasio]
y_Pria_Pns_Pendapatan_Rasio = [t[0] for t in List_Pria_PNS_Pendapatan_Rasio]
y_Pria_PegawaiSwasta_Pendapatan_Rasio = [t[0] for t in List_Pria_PegawaiSwasta_Pendapatan_Rasio]
y_Pria_PolisiMiliter_Pendapatan_Rasio = [t[0] for t in List_Pria_PolisiMiliter_Pendapatan_Rasio]
y_Pria_Lainnya_Pendapatan_Rasio = [t[0] for t in List_Pria_Lainnya_Pendapatan_Rasio]
y_Pria_Wirausaha_Pendapatan_Rasio = [t[0] for t in List_Pria_Wirausaha_Pendapatan_Rasio]
plt.scatter(x_Pria_Wirausaha_Pendapatan_Rasio, y_Pria_Wirausaha_Pendapatan_Rasio, marker='o', color='red', label='Wirausaha')
plt.scatter(x_Pria_PolisiMiliter_Pendapatan_Rasio, y_Pria_PolisiMiliter_Pendapatan_Rasio, marker='v', color='orange', label='Polisi/Militer')
plt.scatter(x_Pria_PegawaiSwasta_Pendapatan_Rasio, y_Pria_PegawaiSwasta_Pendapatan_Rasio, marker='p', color='lightblue', label='Pegawai Swasta')
plt.scatter(x_Pria_Pns_Pendapatan_Rasio, y_Pria_Pns_Pendapatan_Rasio, color='lightgreen', marker='*', label='PNS')
plt.scatter(x_Pria_Lainnya_Pendapatan_Rasio, y_Pria_Lainnya_Pendapatan_Rasio, color='magenta', marker='+', label='Lainnya')
plt.legend()
xtick_positions = [i/2 for i in range(13)]
xtick_labels = [str(i) for i in xtick_positions]
plt.xticks(xtick_positions, xtick_labels)
ytick_positions = [i for i in range(500000, 11000000, 500000)]
ytick_labels = [str(i) for i in ytick_positions]
plt.yticks(ytick_positions, ytick_labels)
plt.ylabel('Besar Pendapatan (Rp)')
plt.xlabel('Rasio Ketergantungan')
plt.title('Grafik Pendapatan dan Rasio Ketergantungan Komuter Pria')

#wanita
List_Wanita_Lainnya_Pendapatan_Rasio = []
List_Wanita_PNS_Pendapatan_Rasio = []
List_Wanita_PegawaiSwasta_Pendapatan_Rasio = []
List_Wanita_Wirausaha_Pendapatan_Rasio = []
for pekerjaan, pendapatan, rasio in List_Kelamin_Pekerjaan_Pendapatan_Rasio_Dict_Wanita:
    if pekerjaan == 'Lainnya':
        List_Wanita_Lainnya_Pendapatan_Rasio.append((pendapatan, rasio))
    elif pekerjaan == 'PNS':
        List_Wanita_PNS_Pendapatan_Rasio.append((pendapatan, rasio))
    elif pekerjaan == 'Pegawai Swasta':
        List_Wanita_PegawaiSwasta_Pendapatan_Rasio.append((pendapatan, rasio))
    else:
        List_Wanita_Wirausaha_Pendapatan_Rasio.append((pendapatan, rasio))
plt.figure()
x_Wanita_Pns_Pendapatan_Rasio = [t[1] for t in List_Wanita_PNS_Pendapatan_Rasio]
x_Wanita_PegawaiSwasta_Pendapatan_Rasio = [t[1] for t in List_Wanita_PegawaiSwasta_Pendapatan_Rasio]
x_Wanita_Lainnya_Pendapatan_Rasio = [t[1] for t in List_Wanita_Lainnya_Pendapatan_Rasio]
x_Wanita_Wirausaha_Pendapatan_Rasio = [t[1] for t in List_Wanita_Wirausaha_Pendapatan_Rasio]
y_Wanita_Pns_Pendapatan_Rasio = [t[0] for t in List_Wanita_PNS_Pendapatan_Rasio]
y_Wanita_PegawaiSwasta_Pendapatan_Rasio = [t[0] for t in List_Wanita_PegawaiSwasta_Pendapatan_Rasio]
y_Wanita_Lainnya_Pendapatan_Rasio = [t[0] for t in List_Wanita_Lainnya_Pendapatan_Rasio]
y_Wanita_Wirausaha_Pendapatan_Rasio = [t[0] for t in List_Wanita_Wirausaha_Pendapatan_Rasio]
plt.scatter(x_Wanita_Wirausaha_Pendapatan_Rasio, y_Wanita_Wirausaha_Pendapatan_Rasio, marker='o', color='red', label='Wirausaha')
plt.scatter(x_Wanita_PegawaiSwasta_Pendapatan_Rasio, y_Wanita_PegawaiSwasta_Pendapatan_Rasio, marker='p', color='lightblue', label='Pegawai Swasta')
plt.scatter(x_Wanita_Pns_Pendapatan_Rasio, y_Wanita_Pns_Pendapatan_Rasio, color='lightgreen', marker='*', label='PNS')
plt.scatter(x_Wanita_Lainnya_Pendapatan_Rasio, y_Wanita_Lainnya_Pendapatan_Rasio, color='magenta', marker='+', label='Lainnya')
plt.legend()
xtick_positions = [i/2 for i in range(9)]
xtick_labels = [str(i) for i in xtick_positions]
plt.xticks(xtick_positions, xtick_labels)
ytick_positions = [i for i in range(500000, 8000000, 500000)]
ytick_labels = [str(i) for i in ytick_positions]
plt.yticks(ytick_positions, ytick_labels)
plt.ylabel('Besar Pendapatan (Rp)')
plt.xlabel('Rasio Ketergantungan')
plt.title('Grafik Pendapatan dan Rasio Ketergantungan Komuter Wanita')

#Membuat grafik perbandingan Status Pernikahan, Pendapatan, Rasio Ketergantungan, Kenyamanan untuk Tiap Kelamin
Data_Kolom_Pernikahan = [x for x in df_data_commuter['Pernikahan']]
Data_Kolom_Pernikahan_Detil=[]
for i in Data_Kolom_Pernikahan:
    if i == 1:
        Data_Kolom_Pernikahan_Detil.append('Menikah')
    elif i ==2:
        Data_Kolom_Pernikahan_Detil.append('Lajang')
    elif i == 3:
        Data_Kolom_Pernikahan_Detil.append('Duda')
    else:
        Data_Kolom_Pernikahan_Detil.append('Janda')
Data_Kolom_Kualitas_Hidup1 = [x for x in df_data_commuter['F.1']]
Data_Kolom_Kualitas_Hidup2 = [x for x in df_data_commuter['F.2']]
Data_Kolom_Kualitas_Hidup3 = [x for x in df_data_commuter['F.3']]
Data_Kolom_Kualitas_Hidup4 = [x for x in df_data_commuter['F.4']]
Data_Kolom_Kualitas_Hidup5 = [x for x in df_data_commuter['F.5']]
Data_Kolom_Kualitas_Hidup6 = [x for x in df_data_commuter['F.6']]
Data_Kolom_Kualitas_Hidup7 = [x for x in df_data_commuter['F.7']]
Data_Kolom_Kualitas_Hidup8 = [x for x in df_data_commuter['F.8']]

#pengelompokan berdasarkan kelamin
Kelamin_Pernikahan_Hidup1_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup1, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pernikahan_Hidup2_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup2, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pernikahan_Hidup3_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup3, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pernikahan_Hidup4_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup4, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pernikahan_Hidup5_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup5, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pernikahan_Hidup6_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup6, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pernikahan_Hidup7_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup7, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)
Kelamin_Pernikahan_Hidup8_Pendapatan_Rasio = zip(Data_Kolom_Kelamin_Detil, Data_Kolom_Pernikahan_Detil, Data_Kolom_Kualitas_Hidup8, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)

Pria_Lajang_Hidup1_Pendapatan_Rasio = []
Pria_Menikah_Hidup1_Pendapatan_Rasio = []
Duda_Hidup1_Pendapatan_Rasio = []
Wanita_Lajang_Hidup1_Pendapatan_Rasio = []
Wanita_Menikah_Hidup1_Pendapatan_Rasio = []
Janda_Hidup1_Pendapatan_Rasio = []
for kelamin, pernikahan, hidup1, pendapatan, rasio in Kelamin_Pernikahan_Hidup1_Pendapatan_Rasio:
    if (kelamin, pernikahan) == ('Pria', 'Lajang'):
        Pria_Lajang_Hidup1_Pendapatan_Rasio.append((hidup1, pendapatan, rasio))
    elif (kelamin, pernikahan) == ('Wanita', 'Lajang'):
        Wanita_Lajang_Hidup1_Pendapatan_Rasio.append((hidup1, pendapatan, rasio))
    elif (kelamin, pernikahan) == ('Pria', 'Menikah'):
        Pria_Menikah_Hidup1_Pendapatan_Rasio.append((hidup1, pendapatan, rasio))
    elif (kelamin, pernikahan) == ('Wanita', 'Menikah'):
        Wanita_Menikah_Hidup1_Pendapatan_Rasio.append((hidup1, pendapatan, rasio))
    elif pernikahan == ('Pria', 'Duda'):
        Duda_Hidup1_Pendapatan_Rasio.append((hidup1, pendapatan, rasio))
    elif (kelamin, pernikahan) == ('Wanita', 'Janda'):
        Janda_Hidup1_Pendapatan_Rasio.append((hidup1, pendapatan, rasio))

#Pengelompokkan berdasarkan hasil survey
Dict_Pria_Lajang_Hidup1_Pendapatan_Rasio = {}
for data in Pria_Lajang_Hidup1_Pendapatan_Rasio:
    x = data[0]
    y = data[1:]
    if x not in Dict_Pria_Lajang_Hidup1_Pendapatan_Rasio:
        Dict_Pria_Lajang_Hidup1_Pendapatan_Rasio[x]=[]
    Dict_Pria_Lajang_Hidup1_Pendapatan_Rasio[x].append(y)
Dict_Pria_Menikah_Hidup1_Pendapatan_Rasio = {}
for data in Pria_Menikah_Hidup1_Pendapatan_Rasio:
    x = data[0]
    y = data[1:]
    if x not in Dict_Pria_Menikah_Hidup1_Pendapatan_Rasio:
        Dict_Pria_Menikah_Hidup1_Pendapatan_Rasio[x]=[]
    Dict_Pria_Menikah_Hidup1_Pendapatan_Rasio[x].append(y)
Dict_Duda_Hidup1_Pendapatan_Rasio = {}
for data in Duda_Hidup1_Pendapatan_Rasio:
    x = data[0]
    y = data[1:]
    if x not in Dict_Duda_Hidup1_Pendapatan_Rasio:
        Dict_Duda_Hidup1_Pendapatan_Rasio[x]=[]
    Dict_Duda_Hidup1_Pendapatan_Rasio[x].append(y)
Dict_Wanita_Lajang_Hidup1_Pendapatan_Rasio = {}
for data in Wanita_Lajang_Hidup1_Pendapatan_Rasio:
    x = data[0]
    y = data[1:]
    if x not in Dict_Wanita_Lajang_Hidup1_Pendapatan_Rasio:
        Dict_Wanita_Lajang_Hidup1_Pendapatan_Rasio[x]=[]
    Dict_Wanita_Lajang_Hidup1_Pendapatan_Rasio[x].append(y)
Dict_Wanita_Menikah_Hidup1_Pendapatan_Rasio = {}
for data in Wanita_Menikah_Hidup1_Pendapatan_Rasio:
    x = data[0]
    y = data[1:]
    if x not in Dict_Wanita_Menikah_Hidup1_Pendapatan_Rasio:
        Dict_Wanita_Menikah_Hidup1_Pendapatan_Rasio[x]=[]
    Dict_Wanita_Menikah_Hidup1_Pendapatan_Rasio[x].append(y)
Dict_Janda_Hidup1_Pendapatan_Rasio = {}
for data in Janda_Hidup1_Pendapatan_Rasio:
    x = data[0]
    y = data[1:]
    if x not in Dict_Janda_Hidup1_Pendapatan_Rasio:
        Dict_Janda_Hidup1_Pendapatan_Rasio[x]=[]
    Dict_Janda_Hidup1_Pendapatan_Rasio[x].append(y)
plt.figure()
tanda = {5:'$Ss$', 4:'$S$', 3:'$N$', 2:'$T$', 1:'$St$'}
for key, value in Dict_Pria_Lajang_Hidup1_Pendapatan_Rasio.items():
    x = [isi[0] for isi in value]
    y = [isi[1] for isi in value]
    plt.scatter(x,y, marker=tanda.get(key, 'x'), label='Pria-Lajang')
for key, value in Dict_Pria_Menikah_Hidup1_Pendapatan_Rasio.items():
    x = [isi[0] for isi in value]
    y = [isi[1] for isi in value]
    plt.scatter(x,y, marker=tanda.get(key, 'x'), label='Pria-Menikah')
for key, value in Dict_Duda_Hidup1_Pendapatan_Rasio.items():
    x = [isi[0] for isi in value]
    y = [isi[1] for isi in value]
    plt.scatter(x,y, marker=tanda.get(key, 'x'), label='Janda')
ytick_positions = [i/2 for i in range(13)]
ytick_labels = [str(i) for i in ytick_positions]
plt.yticks(ytick_positions, ytick_labels)
xtick_positions = [i for i in range(500000, 11500000, 500000)]
xtick_labels = [str(i) for i in xtick_positions]
plt.xticks(xtick_positions, xtick_labels, fontsize=6.5)
plt.title("Hidup akan lebih baik bila tidak menjadi komuter untuk bekerja?")
plt.legend(title='Status')
plt.xlabel('Besar Pendapatan')
plt.ylabel('Rasio Ketergantungan')

plt.figure()
for key, value in Dict_Wanita_Lajang_Hidup1_Pendapatan_Rasio.items():
    x = [isi[0] for isi in value]
    y = [isi[1] for isi in value]
    plt.scatter(x,y, marker=tanda.get(key, 'x'), label='Wanita-Lajang')
for key, value in Dict_Wanita_Menikah_Hidup1_Pendapatan_Rasio.items():
    x = [isi[0] for isi in value]
    y = [isi[1] for isi in value]
    plt.scatter(x,y, marker=tanda.get(key, 'x'), label='Wanita-Menikah')
for key, value in Dict_Janda_Hidup1_Pendapatan_Rasio.items():
    x = [isi[0] for isi in value]
    y = [isi[1] for isi in value]
    plt.scatter(x,y, marker=tanda.get(key, 'x'), label='Janda')
ytick_positions = [i/2 for i in range(9)]
ytick_labels = [str(i) for i in ytick_positions]
plt.yticks(ytick_positions, ytick_labels)
xtick_positions = [i for i in range(500000, 8000000, 500000)]
xtick_labels = [str(i) for i in xtick_positions]
plt.xticks(xtick_positions, xtick_labels, fontsize=6.5)
plt.title("Hidup akan lebih baik bila tidak menjadi komuter untuk bekerja?")
plt.legend(title='Status')
plt.xlabel('Besar Pendapatan')
plt.ylabel('Rasio Ketergantungan')


#Pengirisan simpulan hidup:Sangat Puas 10.2%
Data_Kolom_Kelamin_Detil
Data_Kolom_Pendapatan_Detil
Data_Kolom_Rasio_Detil_Float
Data_Kolom_Simpulan_Kualitas_Hidup = [x for x in df_data_commuter['Kepuasan Hidup']]

List_Kepuasan_Kelamin_Pendapatan_Rasio_Zip = zip(Data_Kolom_Simpulan_Kualitas_Hidup, Data_Kolom_Kelamin_Detil, Data_Kolom_Pendapatan_Detil, Data_Kolom_Rasio_Detil_Float)

Sangat_Puas_Pria = []
Sangat_Puas_Wanita = []
for kepuasan, kelamin, pendapatan, rasio in List_Kepuasan_Kelamin_Pendapatan_Rasio_Zip:
    if kepuasan == 'Sangat Puas' and kelamin == 'Pria':
        Sangat_Puas_Pria.append((pendapatan, rasio))
    elif kepuasan == 'Sangat Puas' and kelamin == 'Wanita':
        Sangat_Puas_Wanita.append((pendapatan, rasio))
    else:
        pass

plt.figure()
x_Sangat_Puas_Pria = [t[0] for t in Sangat_Puas_Pria]
y_Sangat_Puas_Pria = [t[1] for t in Sangat_Puas_Pria]
xtick_positions = [i for i in range(0, 7000000, 500000)]
xtick_labels = [str(i) for i in xtick_positions]
plt.title("Sebaran Komuter Pria dengan Simpulan Kualitas Hidup 'Sangat Puas',\nTotal: {} Orang".format((len(Sangat_Puas_Pria))))
plt.xticks(xtick_positions, xtick_labels)
plt.scatter(x_Sangat_Puas_Pria, y_Sangat_Puas_Pria)

plt.figure()
x_Sangat_Puas_Wanita = [t[0] for t in Sangat_Puas_Wanita]
y_Sangat_Puas_Wanita = [t[1] for t in Sangat_Puas_Wanita]
xtick_positions = [i for i in range(0, 4000000, 500000)]
xtick_labels = [str(i) for i in xtick_positions]
plt.title("Sebaran Komuter Wanita dengan Simpulan Kualitas Hidup 'Sangat Puas'\nTotal: {} Orang".format((len(Sangat_Puas_Wanita))))
plt.xticks(xtick_positions, xtick_labels)
plt.scatter(x_Sangat_Puas_Wanita, y_Sangat_Puas_Wanita)

plt.show()