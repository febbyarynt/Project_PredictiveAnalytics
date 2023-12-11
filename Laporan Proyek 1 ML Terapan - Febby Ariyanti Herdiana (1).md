# Proyek 1 Predictive Analytics - Febby Ariyanti Herdiana

## Domain Proyek
![](https://raw.githubusercontent.com/febbyarynt/assets/4d604b149e3df0c0d34514dad135f58f8a3981db/heart%20failure.jpeg)

Jantung adalah organ yang mempunyai peranan penting dalam kelangsungan hidup manusia karena fungsinya untuk mendistribusikan darah dari paru-paru ke seluruh bagian tubuh, yang dimana darah tersebut mengandung banyak sekali oksigen sehingga dapat membantu proses metabolisme di dalam tubuh manusia. Maka dari itu, organ jantung perlu dilindungi, dirawat, dan dijaga kondisinya untuk mencegah kerusakan pada jantung yang mengakibatkan penyakit gagal jantung.

Penderita penyakit cardiovascular (CVD) adalah gangguan pada jantung atau penyakit
jantung koroner di seluruh dunia terus mengalami peningkatan dan menjadi penyakit yang paling mematikan. Sistem perawatan kesehatan di seluruh dunia mengalamai mengalami kesulitan karena kurangnya keahlian staf medis dalam menentukan dan memprediksi penyakit ini. Salah satu cara efektif dalam mengidentifikasi dan memprediksi penyakit jantung adalah dengan memanfaatkan algoritma machine learning. Machine learning mempu mengatas kerumitan dalam mendiagnosis penyakit jantung dengan model prediksi. 

Prediksi dini penyakit gagal jantung dari riwayat kesehatan merupakan hal yang penting agar kita dapat melakukan pencegahan sebelumnya. Prediksi ini dapat diperoleh dengan memanfaatkan teknologi machine learning untuk menemukan pengetahuan baru dari data dasar sehingga menemukan pola yang valid, berguna, dan mudah dipelajari. Solusi yang ditawarkan adalah dengan memanfaatkan *machine learning* dengan metode regresi  yang dapat memprediksi kemungkinan seseorang mengidap penyakit gagal jantung dengan mempertimbangkan banyak faktor yang nantinya dapat dikembangkan menjadi suatu aplikasi yang dapat membantu masyarakat memprediksi kesehatannya dan terus menerapkan pola hidup lebih sehat.

## Business Understanding


### Problem Statements

- Masyarakat dan petugas kesehatan membutuhkan model terbaik untuk melakukan prediksi terhadap penderita yang beresiko terkena penyakit jantung dari beberapa data yang ada sehingga berguna menjadi pedoman dalam meningkatkan efisiensi dalam tenaga kesehatan yang berdampak pada statistik kesehatan masyarakat.

### Goals

- Membangun model terbaik untuk melakukan prediksi penyakit jantung yang berguna bagi seorang yang berpotensi mengidap penyakit jantung agar dapat melakukan pencegahan sedini mungkin.

### Solution Statements
- Menawarkan solusi sistem prediksi dengan metode regresi. Untuk mendapatkan solusi terbaik, akan digunakan tiga model yang berbeda (KNN, RandomForest, Boosting) dengan *hyperparameter tuning*. Selain itu, untuk mengukur kinerja model digunakan metrik *Mean Squared Error* (MSE) dimana model terbaik nantinya harus memperoleh nilai MSE terkecil dari dataset uji.
- Adapun Dua Metrik yang digunakan adalah :
Akurasi = merupakan acuan terhadap hasil prediksi,berasal dari sklearn dengan formula Accuracy/score.
Mean Squared Error (MSE) = merupakan acuan terhadap pengurangan nilai aktual ,berasal dari sklearn dengan nama MSE.

## Data Understanding

Berdasarkan sumber dataset: [Heart Failure Prediction Dataset](https://www.kaggle.com/fedesoriano/heart-failure-prediction) diperoleh informasi:  
**Abstrak**: Dataset terdiri dari 1190 data point (baris) yang dikumpulkan dari beberapa negara diantaranya:
Cleveland: 303 observations
Hungarian: 294 observations
Switzerland: 123 observations
Long Beach VA: 200 observations
Stalog (Heart) Data Set: 270 observations

Tabel 1. Informasi Dataset

|       | Description |
| ----------- | ----------- |
| Data Set Characteristics | Multivariate |
| Attribute Characteristics | Real |
| Associated Tasks | Regression |
| Number of Instances | 918 |
| Number of Attributes | 4 |
| Missing Values? | N/A |
| Area | Computer |

### Variabel-variabel pada *Heart Failure Prediction* Dataset adalah sebagai berikut:
Age: umur dari pasien [tahun]
Sex: jenis kelamin pasien [M: Pria, F: Wanita]
ChestPainType: tipe sakit pada dada [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
RestingBP: tekanan darah pasien [mm Hg]
Cholesterol: kolesterol serum [mm/dl]
FastingBS: gula darah puasa [1: jika FastingBS > 120 mg/dl, 0: lainnya]
MaxHR: denyut jantung maksimum [Numeric value between 60 and 202]
Oldpeak: oldpeak = ST [Numeric value measured in depression]
ST_Slope: kemiringan latihan puncak segment [Up: upsloping, Flat: flat, Down: downsloping]
HeartDisease: output class [1: heart disease, 0: Normal]

### Menangani Missing Value
Untuk mendeteksi *missing value* digunakan fungsi `isnull().sum()` dan diperoleh:  
Tabel 2. Hasil Deteksi *Missing Value*
|Fitur | Jumlah *Missing Value*|
|:---:|:---:|
|Age | 0|
|Cholesterol | 0|
|RestingBP  |  0|
|MaxHR  |  0|

Dari Tabel 2. terlihat bahwa setiap fitur tidak memiliki *Missing Value* (NULL maupun NAN) sehingga dapat dilanjutkan ke tahapan selanjutnya yaitu menangani *outliers*.
### Menangani Outliers
Pada kasus ini, untuk mendeteksi *outliers* digunakan teknis visualisasi data (boxplot). Kemudian untuk menangani *outliers* digunakan metode IQR.  

Seltman dalam “Experimental Design and Analysis” [[2]](https://www.stat.cmu.edu/~hseltman/309/Book/Book.pdf) menyatakan bahwa outliers yang diidentifikasi oleh boxplot (disebut juga “boxplot outliers”) didefinisikan sebagai data yang nilainya 1.5 IQR di atas Q3 atau 1.5 IQR di bawah Q1.

Berikut persamaannya:
```
Batas bawah = Q1 - 1.5 * IQR
Batas atas = Q3 + 1.5 * IQR
```
Tabel 3. Visualisasi Boxplot Sebelum dan Sesudah Dikenakan Metode IQR.

| Cek Outlier Pada Fitur | Setelah Dikenakan Metode IQR |
|:---:|:---:|
| Fitur Age (Before)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/Fitur%20Age.png) | Fitur Age (After)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/After%20age.png) |
| Fitur RestingBP (Before)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/Fitur%20RestingBP.png) | Fitur RestingBP (After)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/after%20Restingbp.png) |
| Fitur Cholesterol (Before)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/Fitur%20Cholesterol.png) | Fitur Cholesterol (After)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/After%20Cholesterol.png) |
| Fitur MaxHR (Before)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/Fitur%20MaxHR.png) | Fitur MaxHR (After)![](https://raw.githubusercontent.com/febbyarynt/assets/58340e6a2afc31b911755316b6b31f1f88426c3f/After%20MaxHR.png) |


Dari hasil deteksi ulang *outlier* dengan boxplot di Tabel 3 di atas, didapat bahwa *outlier* sudah berkurang pada tiap fitur setelah dibersihkan seperti pada Tabel 4. berikut.

Tabel 4. Perbandingan Jumlah Data Sebelum dan Setelah Dibersihkan dari Outlier

| Jumlah Data Sebelum Dibersihkan | Jumlah Data Setelah Dibersihkan |
|:---:|:---:|
| 918 | 715 |

### Univariate Analysis
Selanjutnya, akan dilakukan proses analisis data dengan teknik Univariate EDA. Pada kasus ini semua fiturnya adalah fitur numerik dan tidak ada fitur kategorikal. Sehingga hanya perlu dilakukan analisa terhadap fitur numerik, sebagai berikut:
#### Analisa Fitur Numerik
Untuk melihat distribusi data pada tiap fitur akan digunakan visualisasi dengan histogram sebagai berikut:

![](https://raw.githubusercontent.com/febbyarynt/assets/3d809a914c07f847e9917053fcf973b5d2a02c23/Analisa%20fitur%20numerik.png)

Gambar 1. Histogram Pada Setiap Fitur

Karena beberapa fitur belum terdistribusi normal hal ini akan berimplikasi pada model, maka untuk selanjutnya perlu dilakukan transformasi data (*non-linear scaling*). Namun, sebelum itu akan dicek terlebih dahulu hubungan antara fitur numerik tersebut.

### Multivariate Analysis

#### Hubungan antara Fitur Numerik
Untuk mengamati hubungan antara fitur numerik, akan digunakan fungsi `pairplot()`, dengan *output* sebagai berikut:

![](https://raw.githubusercontent.com/febbyarynt/assets/3d809a914c07f847e9917053fcf973b5d2a02c23/multivariate%20analysis.png)

Gambar 2. Visualisasi Hubungan antara Fitur Numerik dengan pairplot()

Pada pola sebaran data grafik pairplot di atas, terlihat fitur Age, RestingBP dan Cholesterol memiliki korelasi kuat (negatif / berkebalikan) dengan fitur MaxHR (target).

#### Korelasi antara Fitur Numerik
Untuk mengevaluasi skor korelasi hubungan antara fitur numerik, akan digunakan fungsi `corr()` dengan *output* sebagai berikut.

![](https://raw.githubusercontent.com/febbyarynt/assets/3d809a914c07f847e9917053fcf973b5d2a02c23/correlation%20matrix.png)

Gambar 3. Korelasi antara Fitur Numerik

Koefisien korelasi berkisar antara -1 dan +1. Semakin dekat nilainya ke 1 atau -1, maka korelasinya semakin kuat. Sedangkan, semakin dekat nilainya ke 0 maka korelasinya semakin lemah.

Dari Gambar 3. di atas, fitur `Age` dan `RestingBP` memiliki korelasi yang kuat (mendekati -1, dibawah -0.85) dengan fitur target `MaxHR`. Sementara itu, fitur `Cholesterol` mempunyai korelasi yang rendah dengan fitur target `MaxHR`.

## Data Preparation

### Train Test Split
Dataset akan dibagi menjadi data latih (*train*) dan data uji (*test*). Tujuan langkah ini sebelum proses lainnya adalah agar tidak mengotori data uji dengan informasi yang didapat dari data latih. Contoh pada proses standarisasi dimana jika belum di bagi menjadi data latih dan uji, maka keduanya akan terkena transformasi data yang menggunakan informasi (*mean* dan *standard deviation*) dari gabungan data latih dan uji. Hal ini berpotensi menimbulkan kebocoran data (*data leakage*). Oleh karena itu langkah awal sebelum melakukan tranformasi data adalah membagi dataset terlebih dahulu [[3]](https://learning.oreilly.com/library/view/hands-on-predictive-analytics/9781789138719/).

Pada kasus ini akan menggunakan proporsi pembagian sebesar 90:10 dengan fungsi `train_test_split` dari sklearn dengan *output* sebagai berikut.

Tabel 5. Jumlah Data Latih dan Uji

| Jumlah Data Latih | Jumlah Data Uji | Jumlah Total Data |
|:---:|:---:|:---:|
| 643 | 72 | 715 |

### Standarisasi
Proses standarisasi bertujuan untuk membuat fitur data menjadi bentuk yang lebih mudah diolah oleh algoritma. Pada kasus ini akan digunakan metode `StandarScaler()` dari *library* Scikitlearn.

StandardScaler melakukan proses standarisasi fitur dengan mengurangkan *mean* kemudian membaginya dengan standar deviasi untuk menggeser distribusi. StandarScaler menghasilkan distribusi deviasi sama dengan 1 dan *mean* sama dengan 0.

Berikut *output* yang dihasilkan dari metode StandardScaler dengan menggunakan fungsi `describe()`:

Tabel 6. Hasil Proses Standarisasi Pada Setiap Fitur Pada Data Latih

| |Age | RestingBP | Cholesterol |
|:---:|---:|---:|---:|
| count | 643.0000 | 643.0000 | 643.0000|
| mean |-0.0000 | -0.0000 | 0.0000 |
| std | 1.0008 | 1.0008 | 1.0008 |
| min | -2.5792 | -2.5511 | -3.0561 |
| 25% | -0.7060 | -0.7346 | -0.6503 |
| 50% | 0.1266 | -0.0859 | -0.0981 |
| 75% | 0.6469 | 0.5629 | 0.6315 |
| max | 2.5201 | 2.5092 | 3.2937 |

### Non-Linear Scaling
Terkait hasil visualisasi histogram setiap fitur sebelumnya, terdapat beberapa fitur yang belum terdistribusi normal. Sehingga dapat dilakukan proses *non-linear scaling*. Pada kasus ini, proses *non-linear scaling* akan menggunakan metode `Yeo-Johnson` karena dapat menangani data negatif setelah proses standarisasi sebelumnya.

Mengingat fitur `MaxHR` adalah target fitur, maka akan dikecualikan dalam proses ini agar distribusinya tetap dipertahankan sesuai data aslinya.

Berikut visualisasi dengan histogram untuk distribusi data pada setiap fitur setelah dilakukan *non-linear scaling* dengan metode `Yeo-Johnson`.

![](https://raw.githubusercontent.com/febbyarynt/assets/2a4737c3d6ae904997b76dcca24f8f1dd37d17d9/SCALE%20AGE.png)

Gambar 4. Histogram Fitur Age Sebelum (Kiri) dan Sesudah (Kanan) Dikenakan Metode Yeo-Johnson

![](https://raw.githubusercontent.com/febbyarynt/assets/2a4737c3d6ae904997b76dcca24f8f1dd37d17d9/SCALE%20RESTINGBP.png)

Gambar 5. Histogram Fitur RestingBP Sebelum (Kiri) dan Sesudah (Kanan) Dikenakan Metode Yeo-Johnson

![](https://raw.githubusercontent.com/febbyarynt/assets/b8726dcea94729ce2e57a9e772f1e40cfbdb75ee/SCALE%20CHOLESTEROL.png)

Gambar 6. Histogram Fitur Cholesterol Sebelum (Kiri) dan Sesudah (Kanan) Dikenakan Metode Yeo-Johnson


Selanjutnya dilakukan *drop* pada fitur Age, RestingBP, Cholesterol karena sudah tergantikan dengan YJ_Age, YJ_RestingBP, YJ_Cholesterol yang lebih mendekati distribusi normal. Berikut contoh 5 teratas dari data latih dengan fungsi `head()` untuk mengecek hasil *drop* fitur.

Tabel 7. Tampilan 5 Teratas dari Data Latih Setelah Dilakukan *Drop*

| | YJ_Age | YJ_RestingBP | YJ_Cholesterol |
|:---:|---:|---:|---:|
| 0 | 1.090936 | 1.155298 | -0.342871 |
| 1 | -0.287288 | -0.086245	 | -0.138987 |
| 2	| -0.081367 | -1.317209 | -0.199607 |
| 3	| -0.081367 | 0.548715 | -3.139484 |
| 4	| 0.127054 | -0.418297 | 0.624043 |


### Transformasi Data Uji
Sebelumnya, telah dilakukan proses transformasi data (standarisasi dan *non-linear scaling*) pada data latih untuk menghindari kebocoran data. Sekarang, setelah data latih ditransformasikan secara independen dan diamankan ke dalam variable `X_train_scaled`, selanjutnya perlu melakukan proses transformasi data terhadap data uji dengan `scaler` dari proses standarisasi, `yj_scaler` dari proses *non-linear scaling* (metode `yeo-johnson`) dan proses pca untuk digunakan pada proses evaluasi model.

Biasanya proses ini dilakukan setelah proses *training* model, namun akan dilakukan sekarang dengan tujuan supaya dapat digunakan untuk mencari nilai k optimum pada model KNN (bagian selanjutnya).

Tabel 10. Tampilan Data Uji Setelah Proses Transformasi Data
| | YJ_Age | YJ_RestingBP | YJ_Cholesterol |
|:---:|---:|---:|---:|
| 0 | -1.290533 | -0.086245 | 0.768722 |
| 1 | 0.022513 | 0.424439 | -0.118889 |
| 2 | 1.309520 | 0.235717 | 0.271086 |
| 3 | -1.191754 | 0.235717 | -0.764601 |
| 4 | 0.765720 | -0.0862457 | 0.252090 |
| ... | ... | ... | ... |
| 67 | -1.487266 | 0.424439	 | -1.380644 |
| 68 | 0.550908 | -0.086245 | 0.440066 |
| 69 | 1.200062 | -0.758673 | 0.117742 |
| 70 | -0.287288 | 2.316302 | -0.636302 |
| 71 | -0.793545 | -1.459144 | 0.458633 |

## Model Development
Pada tahapan ini akan menggunakan tiga algoritma untuk regresi. Dan akan dilakukan evaluasi performa masing-masing algoritma dan menetukan di akhir algoritma mana yang memberikan hasil prediksi paling baik. Ketiga algoritma yang akan digunakan, antara lain:
1. K-Nearest Neighbor

    K-Nearest Neighbor atau KKN memiliki kelebihan diantaranya mudah dipahami dan digunakan sedangkan kekurangannya yaitu jika dihadapkan pada jumlah fitur atau dimensi yang besar maka akan rawan terjadi bias.

2. Random Forest

    Random Forest memiliki kelebihan yaitu menggunakan teknik Bagging yang berusaha melawan *overfitting* dengan berjalan secara paralel. Sedangkan kekurangannya ada pada kompleksitas algoritma Random Forest yang membutuhkan waktu relatif lebih lama dan daya komputasi yang lebih tinggi. 

3. Boosting Algorithm

    Boosting Algorithm memiliki kelebihan yaitu menggunakan teknik Boosting yang berusaha menurunkan bias dengan berjalan secara sekuensial atau bertahap. Dan kekurangannya dari segi kompleksitas komputasi yang menjadikan waktu pelatihan relatif lebih lama, selain itu *noisy* dan *outliers* sangat mempengaruhi algoritma ini.

Langkah pertama membuat DataFrame baru `df_models` untuk menampung nilai metrik pada setiap model / algoritma. Hal ini berguna untuk melakukan analisa perbandingan antar model. Metrik yang digunakan untuk mengevaluasi model adalah (MSE - *Mean Squared Error*).

### Model K-Nearest Neighbor
KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih k tetangga terdekat. Pemilihan nilai k sangat penting dan berpengaruh terhadap performa model. Jika memilih k yang terlalu rendah, maka akan menghasilkan model yang *overfitting* dan hasil prediksinya memiliki varians tinggi. Sedangkan jika memilih k yang terlalu tinggi, maka model yang dihasilkan akan *underfitting* dan prediksinya memiliki bias yang tinggi [[4]](https://learning.oreilly.com/library/view/machine-learning-with/9781617296574/).

Oleh karena itu, perlu mencoba beberapa nilai k yang berbeda dari 1 sampai 20 kemudian dibandingkan mana yang menghasilkan nilai metrik model ( memakai *mean squared error*) terbaik. Selain itu, akan digunakan metrik ukuran jarak secara default (*Minkowski Distance*) pada `KNeighborsRegressor` dari library sklearn.

Tabel 11. Perbandingan Nilai K terhadap Nilai MSE
| K | MSE |
|:---:|:---|
| 1 | 805.2361111111111 |
| 2 | 821.3090277777778 |
| 3 | 709.4182098765433 |
| 4 | 663.4262152777778 |
| 5 | 648.811111111111 |
| 6 | 602.4282407407406 |
| 7 | 616.7352607709751 |
| 8 | 587.9147135416666 |
| 9 | 559.3713991769548 |
| 10 | 526.7788888888889 |
| 11 | 524.0421258034894 |
| 12 | 535.6108217592592 |
| 13 | 515.7409598948061 |
| 14 | 510.66567460317464 |
| 15 | 514.2585802469135 |
| 16 | 508.27577039930554 |
| 17 | 501.6978085351788 |
| 18 | 499.8245027434841 |
| 19 | 494.0378962757771 |
| 20 | 490.9088888888889 |

Jika divisualisasikan dengan fungsi `plot()` diperoleh:

![](https://raw.githubusercontent.com/febbyarynt/assets/2010358c3780f73c220901a95aec6cc745cda17e/visualisasi%20nilai%20k.png)

Gambar 9. Visualisasi Nilai K terhadap MSE

### Random Forest
Random forest adalah algoritma jenis *supervised learning* yang termasuk dalam kategori *ensemble* (group) learning. Pada model *ensemble*, setiap model harus membuat prediksi secara independen atau masing-masing. Kemudian, prediksi dari setiap model *ensemble* ini digabungkan untuk membuat prediksi akhirnya. Jenis metode *ensemble* yang digunakan pada Random Forest adalah teknik *Bagging*. Metode ini bekerja dengan membuat *subset* dari data train yang independen. Beberapa model awal (*base model / weak model*) dibuat untuk dijalankan secara paralel dan independen satu sama lain dengan subset data *train* yang independen. Hasil prediksi setiap model kemudian dikombinasikan untuk menentukan hasil prediksi final.

Untuk pengimplementasiannya menggunakan `RandomForestRegressor` dari *library* scikit-learn dengan `base_estimator` defaultnya yaitu `DecisionTreeRegressor` dan parameter-parameter (*hyperparameter*) yang digunakan antara lain:
- `n_estimator`: jumlah *trees* (pohon) di *forest*.
- `max_depth`:  kedalaman atau panjang pohon. Merupakan ukuran seberapa banyak pohon dapat membelah (*splitting*) untuk membagi setiap node ke dalam jumlah pengamatan yang diinginkan.
- `random_state`: digunakan untuk mengontrol random *number generator* yang digunakan.
- `n_jobs`: jumlah *job* (pekerjaan) yang digunakan secara paralel. Ia merupakan komponen untuk mengontrol *thread* atau proses yang berjalan secara paralel. `n_jobs`=-1 artinya semua proses berjalan secara paralel.

Untuk menentukan nilai *hyperparameter* (`n_estimator` & `max_depth`) di atas, dilakukan *tuning* dengan `RandomizedSearchCV` (5 *folds* untuk setiap 10 kandidat sehingga total 50 proses *fitting*) dan hasilnya sebagai berikut:

Tabel 12. Hasil *Hyperparameter Tuning* model RandomizedSearchCV dengan Random Forest
|  | Daftar Nilai | Nilai Terbaik |
|---|---|---|
| n_estimators | 10, 20, 30, 40, 50, 60, 70, 80, 90 | 60 |
| max_depth | 4, 8, 16, 32 | 4 |
| MSE Data Latih | | 428.0130781825669 |
| MSE Data Uji | | 467.0699357641303 |


Berdasarkan Tabel 12. di atas diperoleh nilai MSE terbaik dalam jangkauan parameter (daftar nilai) yaitu 427.8 (dengan data *train*) dan 466.2 (dengan data *test*) dengan `n_estimators`: 60 dan `max_depth`: 4. Selanjutnya dipilih pengaturan parameter tersebut dan menyimpan nilai MSE nya (terhadap data latih, untuk data uji akan dilakukan pada proses evaluasi) kedalam `df_models` yang telah disiapkan sebelumnya.

### Boosting Algorithm
Algoritma Boosting bekerja dengan membangun model dari data *train*. Kemudian membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama. Model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan. Teknik ini bekerja secara sekuensial.

Pada kasus ini kita akan menggunakan metode Adaptive Boosting. Untuk implementasinya menggunakan `AdaBoostRegressor` dari library sklearn dengan `base_estimator` defaultnya yaitu `DecisionTreeRegressor` hampir sama dengan `RandomForestRegressor` bedanya menggunakan metode teknik Boosting.

Parameter-parameter (*hyperparameter*) yang digunakan pada algoritma ini antara lain:
* `n_estimator`: jumlah *estimator* dan ketika mencapai nilai jumlah tersebut algoritma Boosting akan dihentikan.
* `learning_rate`: bobot yang diterapkan pada setiap *regressor* di masing-masing iterasi Boosting.
* `random_state`: digunakan untuk mengontrol *random number generator* yang digunakan.

Untuk menentukan nilai *hyperparameter* (`n_estimator` & `learning_rate`) di atas, akan dilakukan *tuning* dengan `RandomizedSearchCV` (5 *folds* untuk setiap 10 kandidat sehingga total 50 proses *fitting*) dan hasilnya sebagai berikut:

Tabel 13. Hasil *Hyperparameter Tuning* model RandomizedSearchCV dengan AdaBoosting
|  | Daftar Nilai | Nilai Terbaik |
|---|---|---|
| n_estimators | 10, 20, 30, 40, 50, 60, 70, 80, 90 | 20 |
| learning_rate | 0.001, 0.01, 0.1, 0.2 | 0.1 |
| MSE Data Latih | | 468.4522180017724 |
| MSE Data Uji | | 485.6626808695716 |

Berdasarkan Tabel 13. di atas diperoleh nilai MSE terbaik dalam jangkauan parameter (daftar nilai) yaitu 468.4 (dengan data *train*) dan 485.6 (dengan data *test*) dengan `n_estimators`: 20 dan `learning_rate`: 0.2. Selanjutnya dipilih pengaturan parameter tersebut dan menyimpan nilai MSE nya (terhadap data latih, untuk data uji akan dilakukan pada proses evaluasi) kedalam `df_models` yang telah disiapkan sebelumnya.

### Model Terbaik berdasarkan Nilai MSE pada Data Latih
Pada tahap ini, hanya dibatasi pada data latih karena penggunaan data uji akan dilakukan pada proses evaluasi model. Berdasarkan DataFrame `df_models` diperoleh:

Tabel 14. Nilai MSE pada Setiap Model dengan Data Latih
| | KNN | RandomForest | Boosting |
|:---:|---:|---:|---:|
| Train MSE | 406.660932 | 429.85124 | 466.677767 |

Dari Tabel 14. di atas, perlu diperhatikan bahwa hasil MSE pada tabel sedikit berbeda dengan MSE hasil analisa proses *hyperparameter tuning* sebelumnya (khususnya pada Random Forest dan Boosting). Hal ini disebabkan model pada proses *hyperparameter tuning* menggunakan model *RandomizedSearchCV* berbeda dengan Tabel 14. yang menggunakan model Random Forest dan Boosting.

## Evaluation
Dari 3 model yang berbeda di atas, selanjutnya perlu mengevaluasi model-model tersebut menggunakan data uji dan metrik yang digunakan dalam kasus ini yaitu `mean_squared_error`. Hasil evaluasi kemudian disimpan ke dalam `df_models`.

![](https://www.gstatic.com/education/formulas2/472522532/en/mean_squared_error.svg)

Gambar 10. Formula MSE

Keterangan formula MSE pada gambar 10:
- MSE = *Mean Squared Error*
- n = banyaknya data point (baris)
- Y_i = nilai yang diobservasi (fitur target `PE`)
- Y^_i = hasil prediksi

Cara kerja metrik MSE adalah dengan menghitung selisih hasil prediksi dengan nilai fitur target (`PE`). Nilai selisih tersebut, disebut juga sebagai nilai eror yang kemudian di kuadratkan untuk menangani nilai selisih negatif, selanjutnya hasil pengkuadratan setiap nilai selisih dijumlahkan dan terakhir dibagi dengan banyak data point (n) untuk memperoleh nilai rata-ratanya. Rata-rata inilah yang disebut *Mean Squared Error* (MSE). Metrik MSE kerap digunakan untuk mengevaluasi model regresi seperti pada kasus ini.

Berdasarkan DataFrame `df_models` diperoleh:

Tabel 15. Nilai MSE pada Setiap Model dengan Data Uji

| | KNN | RandomForest | Boosting |
|:---:|---:|---:|---:|
| Test MSE | 616.735261 | 465.18759 | 472.990753 |

Untuk memudahkan, dilakukan plot hasil evaluasi model dengan *bar chart* sebagai berikut:

![](https://raw.githubusercontent.com/febbyarynt/assets/729d6eac67140dc7ca7aa3ff17b757b4fad1df20/plot%20evaluasi.png)

Gambar 11. Bar Chart Hasil Evaluasi Model dengan Data Latih dan Uji

Dari Gambar 10 dan 11 di atas, terlihat bahwa, model RandomForest memberikan nilai eror (MSE) yang paling kecil. Sedangkan model algoritma KNN memiliki eror yang paling besar. Sebelum memutuskan model terbaik untuk melakukan prediksi, perlu dilakukan uji prediksi menggunakan beberapa sampel acak (5) pada data uji dengan hasil sebagai berikut:

Tabel 16. Hasil Prediksi dari 5 Sampel Acak

| index_sample | y_true | prediksi_KNN | prediksi_RF | prediksi_Boosting |
|:---:|:---:|:---:|:---:|:---:|
| 38 | 169 | 138.000000	 | 133.076362 | 131.962963 |
| 51 | 120 | 150.428571 | 153.336714 | 154.040000 |
| 0 | 167 | 133.142857 | 148.861396	 | 150.538462 |
| 10 | 129 | 96.571429 | 121.724390 | 126.375000 |
| 22 | 115 | 117.142857 | 130.825632 | 131.711111 |

Dari Tabel 16. terlihat bahwa prediksi dengan Random Forest (RF) memberikan hasil yang paling mendekati. Untuk penentuan model terbaik akan disampaikan di bagian kesimpulan.

## Conclusion

Berdasarkan hasil evaluasi model di atas, dapat disimpulkan bahwa model terbaik untuk melakukan prediksi *Heart Failure* atau gagal jantung adalah model Random Forest. Dengan pengaturan parameter `n_estimators`: 60, `max_depth`: 4 diperoleh nilai metrik MSE sebesar 427.8 (pada data latih) dan 466.2 (pada data uji). Diharapkan dengan dibangunnya model ini dapat menjadi model yang efisiensi dalam memprediksi kegagalan jantung pada pasien.

## Daftar Referensi
[1] Purwono, P., Dewi, P., Wibisono, S. K., & Dewa, B. P. (2022). Model Prediksi Otomatis Jenis Penyakit Hipertensi dengan Pemanfaatan Algoritma Machine Learning Artificial Neural Network. Insect (Informatics and Security): Jurnal Teknik Informatika, 7(2), 82-90. 
[2] Seltman, Howard J. “Experimental Design and Analysis”. 2018. Tersedia: [tautan](https://www.stat.cmu.edu/~hseltman/309/Book/Book.pdf). Diakses pada Oktober 2022.  
[3] Fuentes, Alvaro. "Hands-on Predictive Analytics with Python". Packt Publishing. 2018. Page 129. Tersedia: [O'Reilly Media](https://learning.oreilly.com/library/view/hands-on-predictive-analytics/9781789138719/).  
[4] Rhys, Hefin. "Machine Learning with R, the Tidyverse, and MLR". Manning Publications. 2020. Page 286. Tersedia: [O'Reilly Media](https://learning.oreilly.com/library/view/machine-learning-with/9781617296574/).