import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END


# Load the dataset
df = pd.read_csv('cryptonews.csv')

# Preprocessing: Drop rows with missing text data
df = df.dropna(subset=['text'])

# Keyword extraction using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
X = vectorizer.fit_transform(df['text'])

# Article Categorization using KMeans (Reduced to 1 group)
num_clusters = 1
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['category'] = kmeans.fit_predict(X)

# Create a dictionary for keyword groups (using the top 10 most important words)
terms = vectorizer.get_feature_names_out()
importance_scores = X.sum(axis=0).A1  # Sum TF-IDF scores for each word across all articles
sorted_indices = importance_scores.argsort()[::-1]  # Sort words by importance

# Get the top 10 words
top_10_words = []
for i in sorted_indices:
    word = terms[i]
    if word not in top_10_words:  # Ensure the word is unique
        top_10_words.append(word)

# Make sure there are only 10 unique words
top_10_words = top_10_words[:10]
# Search function to find relevant articles based on user input
def search_articles(query):
    query_vec = vectorizer.transform([query])  # Convert query into vector
    cosine_similarities = cosine_similarity(query_vec, X)  # Get similarity of query with all articles
    similarities = cosine_similarities.flatten()  # Flatten the array
    sorted_indices = similarities.argsort()[::-1]  # Sort articles by most relevant
    
    # Get top 5 most relevant articles with title, date, url, and short description
    result = df.iloc[sorted_indices[:5]]
    articles_info = []
    for idx, row in result.iterrows():
        article = {
            'title': row['title'],
            'date': row['date'],
            'url': row['url'],
            'description': row['text'][:200] + '...'  # Short description (first 200 chars)
        }
        articles_info.append(article)
    return articles_info



# Tkinter GUI
class CryptoNewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto News Search System")
        
        # Labels
        self.keyword_group_label = Label(root, text="Top 10 Important Words for Search")
        self.keyword_group_label.pack()
        
        # Display top 10 words
        self.keyword_groups_text = Text(root, height=10, width=60)
        self.keyword_groups_text.insert(END, ', '.join(top_10_words))
        self.keyword_groups_text.config(state='disabled')
        self.keyword_groups_text.pack()

        # Search input field
        self.search_label = Label(root, text="Enter search phrase:")
        self.search_label.pack()

        self.search_entry = Entry(root, width=50)
        self.search_entry.pack()

        # Search result display area
        self.search_results_text = Text(root, height=10, width=60)
        self.search_results_text.pack()

        # Search button
        self.search_button = Button(root, text="Search", command=self.handle_search)
        self.search_button.pack()

    def handle_search(self):
        query = self.search_entry.get()
        if query:
            results = search_articles(query)
            self.display_search_results(results)

    def display_search_results(self, results):
        self.search_results_text.config(state='normal')
        self.search_results_text.delete(1.0, END)
        for article in results:
            self.search_results_text.insert(END, f"Title: {article['title']}\n")
            self.search_results_text.insert(END, f"Date: {article['date']}\n")
            self.search_results_text.insert(END, f"URL: {article['url']}\n")
            self.search_results_text.insert(END, f"Description: {article['description']}\n\n")
        self.search_results_text.config(state='disabled')



# Run the application
if __name__ == "__main__":
    root = Tk()
    app = CryptoNewsApp(root)
    root.mainloop()
