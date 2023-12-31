# -*- coding: utf-8 -*-
"""Submission1MLTerapan_Febby.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWnj37AgAJnTP-KEvRSBBOl0OXR7QVY-

## PREDICTIVE ANALYTIC - Proyek 1
* Nama : Febby Ariyanti Herdiana

## Importing Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import zipfile
import os
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
# %matplotlib inline

!pip install -q kaggle

from google.colab import files
files.upload()

!mkdir ~/.kaggle
!cp kaggle.json ~/.kaggle/

"""## Data Loading"""

!kaggle datasets download -d fedesoriano/heart-failure-prediction

"""## Ekstrak Data"""

local_zip = '/content/heart-failure-prediction.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content')
zip_ref.close()

"""Data Exploration"""

df = pd.read_csv('/content/heart.csv')
df

df.info()

df.drop(columns=['Sex','ChestPainType', 'RestingECG', 'ExerciseAngina','ST_Slope', 'Oldpeak', 'HeartDisease', 'FastingBS'], inplace=True)

df.describe()

"""### Mengecek Missing Value"""

df.isnull().sum()

"""Dari output isnull().sum() terlihat bahwa setiap fitur tidak memiliki nilai NULL maupun NAN sehingga sekarang kita bisa lanjutkan ke tahapan selanjutnya yaitu menangani outliers.

### Menangani Outliers
* Pada kasus ini kita akan mendeteksi outliers dengan teknis visualisasi data atau boxplot. Kemudian kita akan menangani outliers dengan metode IQR.

Sekaran kita akan melakukan visualisasi pada fitur numerik.

1. Fitur Age
"""

sns.boxplot(x=df['Age'])

"""2. Fitur RestingBP"""

sns.boxplot(x=df['RestingBP'])

"""3. Fitur Cholesterol"""

sns.boxplot(x=df['Cholesterol'])

"""4. Fitur MaxHR"""

sns.boxplot(x=df['MaxHR']) (Target)

"""pada beberapa fitur numerik di atas terdapat outliers kecuali di fitur Age. Kita akan menggunakan metode IQR untuk mengidentifikasi outlier yang berada di luar Q1 dan Q3. Nilai apa pun yang berada di luar batas ini dianggap sebagai outlier.
Menggunakan persamaan berikut:

* Batas bawah = Q1 - 1.5 * IQR
* Batas atas = Q3 + 1.5 * IQR
"""

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

print(f"Sebelum proses menghilangkan outlier, ukuran dataset adalah {df.shape}")
# Proses menghilangkan outlier
df = df[
    ~((df < batas_bawah) | (df > batas_atas)).any(axis=1)
]

# Cek ukuran dataset setelah kita hilangkan outlier
print(f"Setelah proses menghilangkan outlier, ukuran dataset adalah {df.shape}")

"""Banyak outlier yang dibersihkan sebanyak 918 - 715 = 203 (baris atau sampel). Kita akan cek kembali dengan boxplot setelah membersihkan outlier."""

for fitur in df.keys():
  sns.boxplot(x=df[fitur])
  plt.show()

"""Dari hasil deteksi ulang diatas dapat dilihat bahwa outlier sudah berkurang setelah proses pembersihan.

### Univariate Analysis

Analisa Fitur Numerik
"""

sns.set(style="ticks", color_codes=True)
df.hist(bins=50, figsize=(15, 12))
plt.show()

"""### Multivariate Analysis

Hubungan antara Fitur Numerik
* Untuk mengamati hubungan antara fitur numerik, kita akan menggunakan fungsi pairplot().
"""

sns.set(style="ticks", color_codes=True)
sns.pairplot(df,
             kind="reg",
             markers="+",
             diag_kind='kde',
             plot_kws={'line_kws': {'color':'red'},
                       'scatter_kws': {'alpha': 0.5}})

"""Pada pola sebaran data grafik pairplot di atas, terlihat fitur Age, RestingBP dan Cholesterol memiliki korelasi kuat (negatif / berkebalikan) dengan fitur MaxHR (target). Untuk mengevaluasi skor korelasinya, kita akan gunakan fungsi corr() sebagai berikut"""

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""Koefisien korelasi berkisar antara -1 dan +1. Semakin dekat nilainya ke 1 atau -1, maka korelasinya semakin kuat. Sedangkan, semakin dekat nilainya ke 0 maka korelasinya semakin lemah.

## Data Preparation

Train Test Split

Pada kasus ini kita akan menggunakan proporsi pembagian sebesar 90:10 dengan fungsi train_test_split dari sklearn.
"""

from sklearn.model_selection import train_test_split
 
X = df.drop(["MaxHR"], axis =1)
y = df["MaxHR"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

# Cek hasil pembagian dataset
print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""## Standarisasi
Proses standarisasi bertujuan untuk membuat fitur data menjadi bentuk yang lebih mudah diolah oleh algoritma. Kita akan menggunakan teknik StandarScaler dari library Scikitlearn.

StandardScaler melakukan proses standarisasi fitur dengan mengurangkan mean kemudian membaginya dengan standar deviasi untuk menggeser distribusi. StandarScaler menghasilkan distribusi deviasi sama dengan 1 dan mean sama dengan 0.
"""

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.keys())
display(X_train_scaled.describe().round(4))

"""### Non Linear Scaling"""

X_train_scaled_temp = X_train_scaled.copy()
list_name_ori_fitur = X_train_scaled_temp.keys()

# Standardize=false karena sudah dilakukan standarisasi sebelumnya
yj_scaler = PowerTransformer(method='yeo-johnson', standardize=False)
yj_df = pd.DataFrame(
    yj_scaler.fit_transform(X_train_scaled_temp),
    columns=list_name_ori_fitur)

for fitur in list_name_ori_fitur:
  X_train_scaled['YJ_' + fitur] = yj_df[fitur]

"""Cek histogram untuk distribusi data pada setiap fitur setelah dilakukan non-linear scaling dengan metode Yeo-Johnson."""

sns.set(style="ticks", color_codes=True)
for fitur in list_name_ori_fitur:
  X_train_scaled[[fitur,"YJ_" + fitur]].hist(bins=50, figsize=(10, 3))
plt.show()

"""Selanjutnya kita drop Age, Cholesterol, RestingBP karena sudah tergantikan dengan YJ_Age, YJ_Cholesterol, YJ_RestingBP yang lebih mendekati distribusi normal"""

X_train_scaled.drop(['Age', 'Cholesterol', 'RestingBP'], axis=1, inplace=True)
display(X_train_scaled.head())

sns.set(style="ticks", color_codes=True)
sns.pairplot(X_train_scaled[['YJ_Age', 'YJ_Cholesterol', 'YJ_RestingBP']],
             kind="reg",
             markers="+",
             diag_kind='kde',
             plot_kws={'line_kws': {'color':'red'},
                       'scatter_kws': {'alpha': 0.5}})

"""## Transformasi Data Uji
Selanjutnya kita perlu melakukan proses transformasi data terhadap data uji dengan scaler dari proses standarisasi, yj_scaler dari proses non-linear scaling (metode yeo-johnson) dan proses pca untuk digunakan pada proses evaluasi model. Biasanya proses ini dilakukan setelah proses training model, namun kita lakukan sekarang dengan tujuan supaya dapat digunakan untuk mencari nilai k optimum pada model KNN (bagian selanjutnya).
"""

# Scaling terhadap proses standarisasi pada data uji
X_test_standardize = scaler.transform(X_test)

# Scaling terhadap proses non-linear scaling (metode yeo-johnson) pada data uji
# dan menyimpan kembali dalam format DataFrame
X_test_scaled = pd.DataFrame(
    yj_scaler.transform(X_test_standardize),
    columns=["YJ_" + fitur for fitur in list_name_ori_fitur])

# Cek hasil scaling
display(X_test_scaled)

"""## Model Development
Dengan menggunakan 3 algoritma untuk kasus regresi ini, dan selanjutnya mengevaluasi performa masing-masing algoritma dan menentukan mana yang dapat memberikan hasil prediksi terbaik. Tiga Algoritma tersebut yaitu :
1.  K-Nearest Neighbor ( Memiliki kelebihan yaitu mudah dipahami dan digunakan sedangkan kekurangannya kika dihadapkan pada jumlah fitur atau dimensi yang besar rawan terjadi bias)
2. Random Forest ( Kelebihannya menggunakan teknik Bagging yang berusaha melawan overfitting dengan berjalan secara paralel. Sedangkan kekurangannya ada pada kompleksitas algoritma Random Forest yang membutuhkan waktu relatif lebih lama dan daya komputasi yang lebih tinggi)
3. Boosting Algorithm ( Kelebihan algoritma Boosting adalah menggunakan teknik Boosting yang berusaha menurunkan bias dengan berjalan secara sekuensial (memperbaiki model di tiap tahapnya). Sedangkan kekurangannya hampir sama dengan algoritma Random Forest dari segi kompleksitas komputasi yang menjadikan waktu pelatihan relatif lebih lama, selain itu noisy dan outliers sangat berpengaruh dalam algoritma ini)

Untuk langkah pertama, kita akan siapkan DataFrame baru untuk menampung nilai metrik (MSE - Mean Squared Error) pada setiap model / algoritma. Hal ini berguna untuk melakukan analisa perbandingan antar model.
"""

# Siapkan dataframe untuk analisis model
df_models = pd.DataFrame(index=['Train MSE', 'Test MSE'], 
                      columns=['KNN', 'RandomForest', 'Boosting'])

"""### Model K-Nearest Neighbor"""

list_mse = []
for k in range(1, 21):
  knn = KNeighborsRegressor(n_neighbors=k)
  knn.fit(X_train_scaled, y_train)
  y_prediction = knn.predict(X_test_scaled)
  test_mse = mean_squared_error(y_test, y_prediction)
  list_mse.append(test_mse)
  print(f"Nilai MSE untuk k = {k} adalah : {test_mse}")

pd.DataFrame(list_mse, index=range(1, 21)).plot(
    xlabel="K",
    ylabel="MSE",
    legend=False,
    xticks=range(1,21), 
    figsize=(12,4),
    title='Visualisasi Nilai K terhadap MSE')

KNN = KNeighborsRegressor(n_neighbors=7)
KNN.fit(X_train_scaled, y_train)
df_models.loc['Train MSE', 'KNN'] = mean_squared_error(
    y_pred=KNN.predict(X_train_scaled),
    y_true=y_train)

"""### Random Forest

Kita akan *menggunakan* RandomForestRegressor dari library scikit-learn dengan base_estimator defaultnya yaitu DecisionTreeRegressor dan parameter-parameter (hyperparameter) yang digunakan antara lain:

* n_estimator: jumlah trees (pohon) di forest.
* max_depth: kedalaman atau panjang pohon. Ia merupakan ukuran seberapa banyak pohon dapat membelah (splitting) untuk membagi setiap node ke dalam jumlah pengamatan yang diinginkan.
random_state: digunakan untuk mengontrol random number generator yang digunakan.
* n_jobs: jumlah job (pekerjaan) yang digunakan secara paralel. Ia merupakan komponen untuk mengontrol thread atau proses yang berjalan secara paralel.n_jobs=-1 artinya semua proses berjalan secara paralel.


Untuk menentukan nilai hyperparameter (n_estimator & max_depth) di atas, kita akan melakukan tuning dengan RandomizedSearchCV.
"""

params_rf = {
    "n_estimators": np.arange(10, 100, 10), # kelipatan 10 mulai dari 10 sampai 90
    "max_depth": [4, 8, 16, 32]
}

# Randomized search model
rs_model = RandomizedSearchCV(
    RandomForestRegressor(n_jobs=-1, random_state=123),
    param_distributions=params_rf,
    # Ref: https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
    scoring='neg_mean_squared_error', # Negatif dari nilai MSE
    verbose=3
)

rs_model.fit(X_train_scaled, y_train)

"""Mengecek hasil tuning hyperparameter dan nilai metrik MSE."""

print("Hasil tuning hyperparameter", rs_model.best_params_)

print("Nilai MSE model RandomSearchCV_RF dengan data latih", mean_squared_error(
    y_pred=rs_model.predict(X_train_scaled),
    y_true=y_train))
print("Nilai MSE model RandomSearchCV_RF dengan data uji", mean_squared_error(
    y_pred=rs_model.predict(X_test_scaled),
    y_true=y_test))

"""Dari hasil output di atas diperoleh nilai MSE terbaik dalam jangkauan parameter params_rf yaitu 427.8 (dengan data train) dan 466.2 (dengan data test) dengan n_estimators: 60 dan max_depth: 4. Selanjutnya kita akan menggunakan pengaturan parameter tersebut dan menyimpan nilai MSE nya kedalam df_models yang telah kita siapkan sebelumnya."""

RF = RandomForestRegressor(n_estimators=60, max_depth=4)
RF.fit(X_train_scaled, y_train)

df_models.loc['Train MSE', 'RandomForest'] = mean_squared_error(
    y_pred=RF.predict(X_train_scaled),
    y_true=y_train)

"""### Boosting Algorithm

Pada kasus ini kita akan menggunakan metode Adaptive Boosting. Untuk implementasinya kita menggunakan AdaBoostRegressor dari library sklearn dengan base_estimator defaultnya yaitu DecisionTreeRegressor hampir sama dengan RandomForestRegressor bedanya menggunakan metode teknik Boosting.

Parameter-parameter (hyperparameter) yang digunakan pada algoritma ini antara lain:

* n_estimator: jumlah estimator dan ketika mencapai nilai jumlah tersebut algoritma Boosting akan dihentikan.
* learning_rate: bobot yang diterapkan pada setiap regressor di masing-masing iterasi Boosting.
* random_state: digunakan untuk mengontrol random number generator yang digunakan.

Untuk menentukan nilai hyperparameter (n_estimator & learning_rate) di atas, kita akan melakukan tuning dengan RandomizedSearchCV.
"""

params_ab = {
    "n_estimators": np.arange(10, 100, 10), # kelipatan 10 mulai dari 10 sampai 90
    "learning_rate": [0.001, 0.01, 0.1, 0.2]
}

# Randomized search model
rs_model_ab = RandomizedSearchCV(
    AdaBoostRegressor(random_state=123),
    param_distributions=params_ab,
    # Ref: https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
    scoring='neg_mean_squared_error', # Negatif dari nilai MSE
    verbose=3
)

rs_model_ab.fit(X_train_scaled, y_train)

"""Mengecek hasil tuning hyperparameter dan nilai metrik MSE"""

print("Hasil tuning hyperparameter", rs_model_ab.best_params_)

# AB = AdaBoosting
print("Nilai MSE model RandomSearchCV_AB dengan data latih", mean_squared_error(
    y_pred=rs_model_ab.predict(X_train_scaled),
    y_true=y_train))
print("Nilai MSE model RandomSearchCV_AB dengan data uji", mean_squared_error(
    y_pred=rs_model_ab.predict(X_test_scaled),
    y_true=y_test))

"""Dari hasil output di atas diperoleh nilai MSE terbaik dalam jangkauan parameter params_ab yaitu 468.4 (dengan data train) dan 485.6 (dengan data test) dengan n_estimators: 20 dan learning_rate: 0.1. Selanjutnya kita akan menggunakan pengaturan parameter tersebut dan menyimpan nilai MSE nya kedalam df_models yang telah kita siapkan sebelumnya."""

boosting = AdaBoostRegressor(n_estimators=20, learning_rate=0.1)
boosting.fit(X_train_scaled, y_train)

df_models.loc['Train MSE', 'Boosting'] = mean_squared_error(
    y_pred=boosting.predict(X_train_scaled),
    y_true=y_train)

"""### Evaluasi Model

Dari proses sebelumnya, kita telah membuat tiga model yang berbeda dan juga telah melatihnya. Selanjutnya kita perlu mengevaluasi model-model tersebut menggunakan data uji dan metrik yang digunakan dalam kasus ini yaitu mean_squared_error. Hasil evaluasi kemudian kita simpan ke dalam df_models.
"""

for name, model in {'KNN': KNN, 'RandomForest': RF, 'Boosting': boosting}.items():
  df_models.loc['Test MSE', name] = mean_squared_error(
      y_pred=model.predict(X_test_scaled),
      y_true=y_test)
  
# Mengecek evaluasi model
display(df_models)

"""Plot hasil evaluasi model dengan bar chart."""

fig, ax = plt.subplots()
df_models.T.sort_values(by='Test MSE', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Dari gambar di atas, terlihat bahwa, model RandomForest memberikan nilai eror (MSE) yang paling kecil. Sebelum memutuskan model terbaik untuk melakukan prediksi. Mari kita coba uji prediksi menggunakan beberapa sampel acak (5) pada data uji."""

dict_result = {
    'index_sample': [],
    'y_true': [],
    'prediksi_KNN': [],
    'prediksi_RF': [],
    'prediksi_Boosting': []
}

X_sample = X_test_scaled.sample(5)
dict_result['index_sample'] = X_sample.index.values
dict_result['y_true'] = [y_test.iloc[idx] for idx in dict_result['index_sample']]

for name, model in {'KNN': KNN, 'RF': RF, 'Boosting': boosting}.items():
  dict_result['prediksi_' + name] = model.predict(X_sample)

display(pd.DataFrame(dict_result).set_index('index_sample'))

"""Terlihat bahwa prediksi dengan Random Forest (RF) memberikan hasil yang paling mendekati.

### Kesimpulan

Berdasarkan hasil evaluasi model di atas, dapat disimpulkan bahwa model terbaik untuk melakukan prediksi adalah model 
Random Forest. Dengan parameter 'n_estimators':60, 'maxdepth:'4 diperoleh nilai metrik MSE sebesar 427.8 (pada data latih) dan 466.2 (pada data uji).

### Daftar Referensi

* [1] Rhys, Hefin. "Machine Learning with R, the Tidyverse, and MLR". Manning Publications. 2020. Tersedia: O'Reilly Media.
* [2] Fuentes, Alvaro. "Hands-on Predictive Analytics with Python". Packt Publishing. 2018. Tersedia: O'Reilly Media.
* [3] Seltman, Howard J. “Experimental Design and Analysis”.
"""