# -*- coding: utf-8 -*-
"""Submission_2_Dicoding_MLT_Bayu_F_Movies_Recommendation_System (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kd2BB-LTeiEYAkCjb6FBl7sKZF9bFmg7

# **Sistem Rekomendasi Film - Bayu Firmansyah**

# **Project Overview**
Industri perfilman di luar negeri dan di Indonesia mengalami pertumbuhan yang signifikan dalam beberapa tahun terakhir, dengan semakin banyaknya produksi film dan penonton yang semakin banyak. Di Indonesia total penonton film Indonesia di bioskop mencapai 54 juta, angka ini mengalami kenaikan dibandingkan tahun 2019 sebelum masa pandemi sebanyak 51,9 juta penonton. Pada masa pandemi jumlah penonton turun drastis yakni menjadi 12,8 juta pada 2020 dan menjadi 4,5 juta pada 2021[[2]](https://mediaindonesia.com/humaniora/548410/penonton-film-indonesia-di-bioskop-pada-2022-mencapai-54-juta-orang).
Dengan jumlah produksi film yang semakin banyak saat ini mengakibatkan peningkatan pilihan film yang tersedia bagi penonton, namun pada saat yang sama membuat mereka kesulitan untuk menemukan film yang sesuai dengan selera dan preferensi mereka. Mencari film memerlukan waktu, dan terkadang film yang dipilih tidak sesuai harapan, sehingga menyebabkan pemborosan waktu.

Perkembangan teknologi kecerdasan buatan dan algoritma pembelajaran mesin memungkinkan analisis data yang kompleks dan pengolahan besar-besaran informasi untuk menghasilkan rekomendasi yang akurat dan relevan.
Sistem rekomendasi merupakan program atau sistem penyaringan informasi yang menjadi solusi dalam masalah kelebihan informasi dengan cara menyaring sebagian informasi penting dari banyaknya informasi yang ada dan bersifat dinamis sesuai dengan preferensi, minat, atau perilaku pengguna terhadap suatu barang. Sistem rekomendasi dirancang untuk memahami dan memprediksi preferensi pengguna berdasarkan perilaku pengguna[[4]](https://ieeexplore.ieee.org/document/8821893).

Penerapan sistem rekomendasi untuk memberikan rekomendasi film akan mempermudah pencarian film tertentu dari banyak kumpulan film sesuai dengan preferensi pengguna. Ini memudahkan penonton untuk menemukan film yang mereka sukai tanpa harus menghabiskan waktu untuk mencari secara manual. Selain itu, sistem rekomendasi film juga dapat membantu meningkatkan kepuasan pengguna dan penjualan film yang akan menguntungkan pemilik *platform*.

Sistem rekomendasi telah implementasi untuk merekomendasikan film pada *platform* seperti *Netflix, Amazon Prime Video*, dan *Apple TV*. Penelitian terkait telah dilakukan sebelumnya beberapa diantaranya yaitu pada penelitian Sharma, P. dan Yadav, L. Y. (2020). dengan judul *Movie Recommendation System Using Item Based Collaborative Filtering*[[3]](https://ssrn.com/abstract=3672412). Pada penelitian lain Bei-Bei Cui. (2017). melakukan penelitian dengan topik serupa dengan judul *Design and Implementation of Movie Recommendation System Based on Knn Collaborative Filtering Algorithm*, artikel ini merancang dan mengimplementasikan prototipe sistem rekomendasi film berdasarkan algoritma KNN, algoritma penyaringan kolaboratif, dan teknologi sistem rekomendasi algoritma[[1]](https://doi.org/10.1051/itmconf/20171204008).

Pada proyek ini akan mengembangkan sistem rekomendasi film untuk membantu mempersempit pilihan film bagi calon penonton, meningkatkan pengalaman menonton, dan memperkenalkan penonton pada film-film yang mungkin tidak akan mereka temukan secara mandiri. Dengan analisis data dan algoritma cerdas, sistem ini dapat memberikan rekomendasi yang semakin tepat sesuai dengan preferensi setiap individu, menciptakan pengalaman menonton yang lebih menyenangkan dan memuaskan.

# **Business Understanding**

Perusahaan *platform streaming* dan layanan film  mengumpulkan data tentang perilaku penonton, seperti film yang mereka tonton, frekuensi menonton, dan penilaian yang diberikan. Data ini sangat berharga bagi penyedia layanan untuk menganalisis tren preferensi dan kecenderungan penonton, sehingga mereka dapat memahami pasar dan meningkatkan penawaran layanan mereka. Dengan data *platform streaming* dapat menawarkan rekomendasi film berdasarkan kemiripan karakteristik film seperti genre atau rekomendasi film berdasarkan kemiripan penilaian penggunanya. Bagi *platform streaming* dan layanan film lainnya, sistem rekomendasi merupakan alat strategis untuk meningkatkan retensi pelanggan. Dengan memberikan rekomendasi film yang akurat, *platform* dapat membuat penonton tetap tertarik dan terlibat, sehingga mereka lebih cenderung untuk tetap berlangganan dan menggunakan *platform* tersebut secara berkelanjutan.

## Problem Statement
- Bagaimana cara membangun sistem rekomendasi berdasarkan genre film ?
- Bagaimana cara membangun sistem rekomendasi berdasarkan *rating* pengguna terhadap film ?

## Goals
- Membuat  sistem rekomendasi berdasarkan genre film.
- Membuat sistem rekomendasi berdasarkan *rating* pengguna terhadap film.

## Solution Statement
Untuk mencapai tujuan tersebut, sistem akan menerapkan pendekatan solusi menggunakan metode *content-based filtering* dan *collaborative filtering*.

- *Content-based Filtering*:

  Teknik *Content-Based Filtering* adalah metode dalam sistem rekomendasi yang berfokus pada analisis dan perbandingan fitur dari item yang ingin direkomendasikan dengan profil pengguna.
Dalam *content-based filtering* setiap item memiliki representasi fitur yang menggambarkan kontennya. Pada proyek ini akan dibuat sistem rekomendasi film berdasarkan genre film yang dijadikan sebagai atribut untuk menggambarkan film tersebut.
Teknik ini tidak memerlukan data dari pengguna lain, selain itu, content-based filtering dapat memberikan rekomendasi untuk item yang baru atau tidak populer, asalkan memiliki informasi yang cukup tentang konten item tersebut.

- *Collaborative Filtering*:
  Teknik *collaborative filtering* adalah metode yang berfokus pada penggunaan informasi kolaboratif dari berbagai pengguna untuk memberikan rekomendasi kepada pengguna lain. Dalam teknik ini, rekomendasi dibuat berdasarkan pola kesamaan antara preferensi atau perilaku pengguna dalam mengonsumsi item. Konsep dasar dari *collaborative filtering* adalah bahwa jika dua atau lebih pengguna memiliki preferensi yang mirip dalam item tertentu, maka kemungkinan besar mereka juga akan memiliki preferensi yang mirip dalam item lainnya.
  Teknik *collaborative filtering* dapat menemukan pola preferensi yang kompleks dan tidak terduga dari berbagai pengguna, serta metode ini tidak memerlukan informasi konten dari item, sehingga lebih fleksibel dalam merekomendasikan item baru atau yang tidak dikenal.

# **Data Understanding**

Dataset yang digunakan dalam proyek ini merupakan data informasi film dan *rating* dari pengguna dari *MovieLens*. Data informasi film yang digunakan adalah [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) dan data *rating* pengguna yang digunakan adalah [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=ratings_small.csv). Dua file yang akan digunakan yaitu `tmdb_5000_movies.csv` dan `rating_small.csv`

Variabel pada file `tmdb_5000_movies.csv` adalah sebagai berikut.
* `budget`: Biaya pembuatan film
* `genres`: Genre-genre pada suatu film
* `homepage`: halaman pembuka web suatu film
* `id`: Identitas unik untuk film pada MovieLens
* `keywords`: Kata kunci yang berkaitan dengan suatu film
* `original_language`: bahasa asli pembuatan suatu film
* `original_title`: Judul asli film
* `overview`: Sinopsis dari suatu film
* `popularity`: Angka popularitas
* `production_companies`: Perusahaan yang memproduksi suatu film
* `production_countries`: Negara yang memproduksi suatu film
* `release_date`: Tanggal rilis suatu film
* `revenue`: Total pendapatan yang dihasilkan
* `runtime`: Durasi suatu film
* `spoken_languages`: bahasa yang digunakan dalam film
* `status`: Status perilisan film
* `tagline`: Tagline suatu film
* `title`: Judul film
* `vote_average`: Rata-rata vote pengguna pada suatu film
* `vote_count`: Jumlah vote pengguna pada suatu film

Variabel pada file `rating_small.csv` adalah sebagai berikut.
* `userId`: Identitas unik untuk pengguna yang memberikan rating
* `movieId`: Identitas unik untuk film pada MovieLens yang diberikan rating oleh pengguna
* `rating`: Rating yang diberikan oleh pengguna pada skala 5
* `timestamp`: Waktu pengguna memberikan rating pada film

**Import main lib**
"""

# Commented out IPython magic to ensure Python compatibility.
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow import keras
from tensorflow.keras import layers
from ast import literal_eval

# %matplotlib inline
sns.set_palette('Set1')
sns.set()
warnings.filterwarnings('ignore')

"""**Load data movies dan ratings**"""

df_movies = pd.read_csv("/content/drive/MyDrive/Restore/tmdb_5000_movies.csv")
df_ratings = pd.read_csv("/content/drive/MyDrive/Restore/ratings_small.csv")

"""**Movies Data**

Melihat 5 data awal movies
"""

df_movies.head()

"""Melihat movies dataframe info"""

df_movies.info()

"""Melihat deskripsi data movies"""

df_movies.describe()

print('Jumlah Movies ID: ', len(df_movies.id.unique()))

"""**Data ratings**

Melihat 5 data awal ratings
"""

df_ratings.head()

"""Melihat ratings dataframe info"""

df_ratings.info()

"""Melihat deskripsi data ratings"""

df_ratings.describe()

print('Jumlah User ID: ', len(df_ratings.userId.unique()))
print('Jumlah Movies ID: ', len(df_ratings.movieId.unique()))
print('Jumlah Data rating: ', len(df_ratings))

"""# **Data Preparation**

## **Data Preparing Content-Based Filtering**

Cek missing value pada data movies dan ratings
"""

df_movies.isna().sum()

df_ratings.isna().sum()

"""Mengubah nama kolom 'id' menjadi 'movieId', dan membuat dataframe baru dengan kolom id, judul, dan genre film"""

df_movies.rename(columns = {'id':'movieId'}, inplace = True)
df1_movies = df_movies[['movieId', 'title', 'genres']]

"""Mengevaluasi data 'genres' yang berbentuk string menjadi *dictionary*"""

df1_movies['genres'] = df1_movies['genres'].apply(literal_eval)

"""mengubah data 'genres' menjadi bentuk list"""

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        if len(names) > 4:
            names = names[:4]
        return names
    return []

df1_movies['genres'] = df1_movies['genres'].apply(get_list)

df1_movies.head()

"""mengubah data 'genres' menjadi huruf kecil dan menghilangkan spasi antar kata dalam satu jenis genre"""

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:

        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

df1_movies['genres'] = df1_movies['genres'].apply(clean_data)
df1_movies.head()

"""Membuat kolom baru yang  merupakan sebuah string berisi semua genre film metadata yang akan dimasukkan ke vektorizer."""

def create_g(x):
    return ' ' + ' '.join(x['genres'])
df1_movies['genre'] = df1_movies.apply(create_g, axis=1)

"""## **Exploratory Data Analysis.**

membuat grafik genre terpopuler
"""

gen = df1_movies.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
gen.name = 'genre'
pop_gen = pd.DataFrame(gen.value_counts()).reset_index()[0:10]
pop_gen.columns = ['genre', 'movies']

plt.figure(figsize=(8,5))
sns.barplot(data=pop_gen,y="genre",x="movies")
plt.title('Genre dengan Jumlah Film Terbanyak', pad=20)
plt.ylabel('Jenis Genre')
plt.xlabel('Jumlah Film')
plt.show()

"""membuat grafik distribusi rating"""

rates = df_ratings['rating'].value_counts().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=rates,y="rating",x="index")
plt.title('Ratings', pad=20)
plt.xlabel('rating')
plt.ylabel('jumlah')
plt.show()

"""## **Data Preparing Collaborative Filtering**

Menggabungkan movies dan ratings dan menghilangkan kolom 'genre'
"""

df2_movies = df1_movies.merge(df_ratings, on='movieId', how='inner').drop("genre", axis=1)
df2_movies

"""Melakukan *encoding*  kolom userId dan movieId, mengubah data preferensi menjadi bentuk numerik atau representasi vektor"""

user_ids = df2_movies['userId'].unique().tolist()
print('list userID: ', user_ids)

user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

movies_ids = df2_movies['movieId'].unique().tolist()
movies_to_movies_encoded = {x: i for i, x in enumerate(movies_ids)}
movies_encoded_to_movies = {i: x for i, x in enumerate(movies_ids)}

df2_movies['user'] = df2_movies['userId'].map(user_to_user_encoded)
df2_movies['movie'] = df2_movies['movieId'].map(movies_to_movies_encoded)

"""Melakukan normalisasi  nilai rating"""

num_users = len(user_to_user_encoded)
print(num_users)

num_movies = len(movies_encoded_to_movies)
print(num_movies)

df2_movies['rating'] = df2_movies['rating'].values.astype(np.float32)

min_rating = min(df2_movies['rating'])
max_rating = max(df2_movies['rating'])

print('Number of User: {}, Number of movies: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_movies, min_rating, max_rating
))

"""Mengacak urutan data"""

df = df2_movies.sample(frac=1, random_state=42)
df

"""Train-Test Split untuk validasi model dengan 80% data training dan 20% data testing"""

x = df[['user', 'movie']].values
y = df['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""# **Modelling**

## **Content-Based Filtering**

Melakukan vektorisasi dengan TF-IDF untuk menemukan representasi fitur penting dari setiap genre dan melakukan transformasi pada data kategori ke dalam bentuk matriks.
"""

from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer()
count_matrix = count.fit_transform(df1_movies['genre'])

count_matrix.shape

"""Mengubah data sebelumnya yang berbentuk sparse matrix menjadi dense matrix"""

count_matrix.todense()

"""Melakukan perhitungan tingkat kemiripan menggunakan metode cosine similarity"""

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(count_matrix, count_matrix)
cosine_sim

"""Mereset index data movies"""

df1_movies = df1_movies.reset_index()
indices = pd.Series(df1_movies.index, index=df1_movies['title'])

"""Membuat fungsi untuk mendapatkan rekomendasi film"""

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    mov = df1_movies.iloc[movie_indices].reset_index(drop=True)
    recommendations = pd.DataFrame({'movie_title': mov.title, 'genre': mov.genres, 'Similarity': pd.DataFrame(sim_scores)[1]})

    return recommendations

df1_movies.iloc[16]

"""**Recommendation Result Content-Based Filtering**

Melihat top-N rekomendasi fil The Avengers
"""

get_recommendations('The Avengers', cosine_sim)

"""## **Collaborative filtering**

Membuat class model neural network RecommenderNet menggunakan Keras untuk sistem rekomendasi
"""

class RecommenderNet(tf.keras.Model):

    def __init__(self, num_users, num_movies, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.num_users = num_users
        self.num_movies = num_movies
        self.embedding_size = embedding_size
        self.user_embedding = layers.Embedding(
            num_users,
            embedding_size,
            embeddings_initializer='he_normal',
            embeddings_regularizer=keras.regularizers.l2(1e-6),
        )
        self.user_bias = layers.Embedding(num_users, 1)
        self.movie_embedding = layers.Embedding(
            num_movies,
            embedding_size,
            embeddings_initializer='he_normal',
            embeddings_regularizer=keras.regularizers.l2(1e-6),
        )
        self.movie_bias = layers.Embedding(num_movies, 1)

    def call(self, inputs):
        user_vector = self.user_embedding(inputs[:, 0])
        user_bias = self.user_bias(inputs[:, 0])
        movie_vector = self.movie_embedding(inputs[:, 1])
        movie_bias = self.movie_bias(inputs[:, 1])

        dot_user_movie = tf.tensordot(user_vector, movie_vector, 2)
        x = dot_user_movie + user_bias + movie_bias
        return tf.nn.sigmoid(x)

"""# **Evaluation**

Melakukan kompilasi model untuk mempersiapkan model agar siap digunakan untuk proses training dan evaluasi menggunakan Binary Crossentropy, Adam, RMSE
"""

model = RecommenderNet(num_users, num_movies, 50)

model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Melakukan proses training data pada mode"""

history = model.fit(x = x_train, y = y_train, batch_size = 8, epochs = 100, validation_data = (x_val, y_val))

"""Melakukan visualisasi pada hasil training"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""**Recommendation Result Collaborative filtering**

Memperoleh film yang belum ditonton oleh user tertentu berdasarkan data rating yang ada.
"""

movies_df = df2_movies.drop_duplicates('movieId')
df = df2_movies

user_id = df.userId.sample(1).iloc[0]
movies_visited_by_user = df[df.userId == user_id]

movies_not_visited = movies_df[~movies_df['movieId'].isin(movies_visited_by_user.movieId.values)]['movieId']
movies_not_visited = list(
    set(movies_not_visited)
    .intersection(set(movies_to_movies_encoded.keys()))
)
movies_not_visited = [[movies_to_movies_encoded.get(x)] for x in movies_not_visited]
user_encoder = user_to_user_encoded.get(user_id)
user_movies_array = np.hstack(
    ([[user_encoder]] * len(movies_not_visited), movies_not_visited)
)

"""Melakukan prediksi rekomendasi film kepada user yang dipilih secara acak."""

ratings = model.predict(user_movies_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movies_ids = [
    movies_encoded_to_movies.get(movies_not_visited[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('movies with high ratings from user')
print('----' * 8)

top_movies_user = (
    movies_visited_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .movieId.values
)

movies_df_rows = movies_df[movies_df['movieId'].isin(top_movies_user)]
for row in movies_df_rows.itertuples():
    print(row.title,':', row.genres)

print('----' * 8)
print('Top 10 movies recommendation')
print('----' * 8)

recommended_movies = movies_df[movies_df['movieId'].isin(recommended_movies_ids)]
for row in recommended_movies.itertuples():
    print(row.title,':', row.genres)

"""# **Kesimpulan**

Berdasarkan hasil pembahasan diatas, dapat disimpulkan bahwa pada proyek ini, sistem rekomendasi film dengan pendekatan *content-based filtering* menggunakan vektorisasi TF-IDF dan metode penilaian kemiripan *cosine similarity* dapat diberikan rekomendasi film yang sesuai dan relevan berdasarkan genrenya. Sistem rekomendasi film dengan pendekatan *collaborative filtering* berdasarkan rating pengguna terhadap film yang sudah pernah ditonton menggunakan RecommenderNet, *binary crossentropy* untuk menghitung *loss function*, dan  Adam (*Adaptive Moment Estimation*) sebagai *optimizer* menghasilkan *root mean squared error* (RMSE) sebesar 0.2039 pada data testing.
Pengembangan selanjutnya dapat dilakukan dengan menggunakan beberapa fitur sekaligus untuk pendekatan *content-based filtering* atau dengan sistem *hybrid* menggabungkan pendekatan *content-based filtering* dan *collaborative filtering*.

"""