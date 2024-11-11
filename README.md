
Song Recommendation System Using Lyrics Similarity

Project Overview

This project is a content-based song recommendation system that suggests songs with similar lyrics. Using Natural Language Processing (NLP) and machine learning techniques, the system calculates the similarity between songs based on their lyrical content, enabling users to discover songs with similar themes.

Features

Preprocessing: Converts lyrics to lowercase, removes special characters, tokenizes, and stems each word.
TF-IDF Transformation: Transforms lyrics into a TF-IDF matrix to capture word importance.
Cosine Similarity: Calculates cosine similarity between songs to find those with closely matching lyrical content.
Recommendation: Given a song title, the system provides the top 5 lyrically similar songs.
Tools and Libraries
Python: For scripting and data handling.
Pandas: Manages and processes data in the DataFrame.
nltk: For tokenization and stemming.
scikit-learn: For TF-IDF vectorization and cosine similarity calculations.
pickle: Saves precomputed data for efficient access.
Project Structure
spotify_millsongdata.csv: Dataset file containing song lyrics and metadata.
similarity.pkl: Pickled file containing the precomputed cosine similarity matrix for the lyrics.
df.pkl: Pickled DataFrame with song data and preprocessed lyrics.
