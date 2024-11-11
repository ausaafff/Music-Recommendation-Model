# Importing Necessary Libraries
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Reading the file
df = pd.read_csv(r"D:\Ausaaf\ALLIMPORTS\spotify_millsongdata.csv")

# Limiting it to 30000 rows as my machine is not allowing more
df = df.sample(30000).drop('link', axis=1).reset_index(drop=True)

# Cleaning text column
df['text'] = df['text'].str.replace(r'\r\n', ' ', regex=True).str.lower()

nltk.download('punkt')

stemmer = PorterStemmer()

def tokenize_and_stem(text):
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return " ".join(stemmed_tokens)

df['text'] = df['text'].apply(lambda x: tokenize_and_stem(x))

tfidvector = TfidfVectorizer(analyzer='word', stop_words='english')

matrix = tfidvector.fit_transform(df['text'])

# Calculate cosine similarity between the songs
similarity = cosine_similarity(matrix)

# Function to recommend songs based on the cosine similarity of the lyrics
def recommender(song_name):
    try:
        idx = df[df['song'] == song_name].index[0]
    except IndexError:
        return {"error": "Song not found"} 
    
    distance = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    song = []
    for s_id in distance[1:5]:  # Top 5 recommendations (excluding the song itself)
        song.append(df.iloc[s_id[0]].song)
        
    return song

pickle.dump(similarity, open('similarity.pkl', 'wb'))
pickle.dump(df, open('df.pkl', 'wb'))


recommender('perfect')