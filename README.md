# Music Recommendation System Based on Similar Lyrics

## Overview  
This project is a **Music Recommendation System** that suggests songs based on the similarity of their lyrics. Using **Natural Language Processing (NLP)** techniques, the system preprocesses lyrics, calculates similarity using **TF-IDF (Term Frequency-Inverse Document Frequency)**, and recommends songs based on **cosine similarity**.

## Key Features  

- **Text Preprocessing:**  
  - Cleans lyrics by removing special characters and converting text to lowercase.  
  - Tokenization and stemming are applied to reduce words to their root forms.  

- **TF-IDF Vectorization:**  
  - Converts lyrics into numerical vectors using TF-IDF, which captures the importance of words in the entire dataset.  

- **Cosine Similarity Calculation:**  
  - Measures similarity between songs using **cosine similarity**, which calculates the cosine of the angle between two vectors in a multi-dimensional space.  

- **Song Recommendation:**  
  - Recommends the **top 5 most similar songs** based on the lyrics of a given song.  

- **Efficient Storage:**  
  - The **similarity matrix** and **preprocessed data** are saved using `pickle` for quick loading and reuse.  

## Dataset  

The dataset used in this project is **spotify_millsongdata.csv**, which contains the following columns:  

| Column Name | Description |  
|-------------|------------|  
| `song` | The name of the song |  
| `artist` | The artist of the song |  
| `text` | The lyrics of the song |  
| `link` | A link to the song (dropped in this project) |  

Due to computational constraints, the dataset was limited to **30,000 rows**.  

## Workflow  

### 1. Data Loading  
- The dataset is loaded using `pandas`.  
- The `link` column is dropped, and the dataset is sampled to **30,000 rows**.  

### 2. Text Cleaning  
- Removes special characters like `\r\n`.  
- Converts text to **lowercase**.  

### 3. Tokenization and Stemming  
- Lyrics are tokenized into individual words.  
- Words are **stemmed** using the **Porter Stemmer** to reduce them to their root forms.  

### 4. TF-IDF Vectorization  
- The cleaned and stemmed lyrics are transformed into **TF-IDF vectors**.  

### 5. Cosine Similarity Calculation  
- Computes the **cosine similarity matrix** to measure the similarity between songs.  

### 6. Song Recommendation  
- Implements a function **`recommender(song_name)`** that returns the **top 5 most similar songs** based on the input song.  
