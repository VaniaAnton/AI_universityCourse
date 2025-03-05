# Crypto News Search System

This project provides an **AI-driven search algorithm** to categorize and search cryptocurrency news articles from a CSV file. The system uses machine learning algorithms to categorize articles and allows users to input search queries to retrieve the most relevant articles.

---

## Features

1. **AI-driven Search Algorithm**:
   - **Data Preprocessing**: Handles missing data and prepares text for keyword extraction.
   - **Keyword Extraction**: Uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to extract important keywords from the articles.
   - **Article Categorization**: Classifies articles into 5 predefined groups using **KMeans clustering**.

2. **Search Function**:
   - Users can input a search phrase, and the system will retrieve the most relevant articles based on **cosine similarity** between the search query and article content.

3. **User Interface**:
   - A simple graphical interface built with **tkinter** allows users to input search queries and display relevant articles. The interface also shows keyword groups and their corresponding dataset elements.

---

## Requirements

To run this project, you need to install the following libraries:

- **pandas**: For reading and handling CSV files.
- **scikit-learn**: For machine learning algorithms like **TF-IDF vectorization** and **KMeans clustering**.
- **numpy**: For numerical operations.
- **tkinter**: For the graphical user interface (GUI).

### Installation

You can install the necessary libraries with the following commands:

```bash
pip install pandas
pip install scikit-learn
pip install numpy
```
For tkinter, it should already be installed with Python(On macos and windows), but if you're on Linux, you can install it using:
```bash
sudo apt-get install python3-tk
```
---

## How to Run

1. Clone or download this repository to your local machine.
2. Ensure the cryptonews.csv file is placed in the same directory as the Python script.
3. Run the script using Python:
  ```bash
  python crypto_news_search.py
```
This will launch a graphical user interface (GUI) where you can:
- View keyword groups and their corresponding dataset elements.
- Input a search phrase to retrieve relevant articles based on your query.

## Explanation of the System

### AI-driven Search Algorithm:
- **Data Preprocessing**: Missing text data is dropped from the dataset.
- **Keyword Extraction**: TF-IDF is applied to the articles to identify key terms.
- **Article Categorization**: Articles are grouped into 5 categories using KMeans clustering.
- **Article Search**: The system calculates cosine similarity between the user’s input and the article content to find the most relevant results.

### User Interface:
- A simple **Tkinter-based UI** allows users to interact with the system, input search queries, and see the results. Keyword groups and article categories are also displayed.

---

## Example of Use

1. Open the application.
2. Enter a search phrase (e.g., **"Bitcoin price increase"**).
3. The system will display the most relevant articles related to your search.

---

## Conclusion

This project provides an efficient way to categorize and search cryptocurrency news articles using **machine learning** and **natural language processing** techniques. The **user-friendly interface** enhances accessibility and usability for end-users.
