# PROJECT-5-Machine-Learning-Movei-Recomendation-System

#### **1. Introduction**  
A **movie recommendation system** is an application of machine learning that suggests movies based on a user's input. The goal is to enhance user experience by recommending relevant movies based on similarities in genres, cast, crew, keywords, and storyline. The system uses **Natural Language Processing (NLP)** and **cosine similarity** to identify movies similar to the given input.

---

#### **2. Dataset Description**  
The system utilizes the **TMDB 5000 Movies Dataset**, which contains metadata about thousands of movies. It consists of two CSV files:  
- `tmdb_5000_movies.csv`: Contains movie-related information such as `movie_id`, `title`, `overview`, `genres`, `keywords`, and more.  
- `tmdb_5000_credits.csv`: Includes cast and crew details for each movie.

Both datasets are merged based on the **title** column to create a unified dataset.

---

#### **3. Data Preprocessing**  
Before building the recommendation model, the data undergoes preprocessing to clean and structure it properly:

1. **Handling Missing and Duplicate Values**  
   - Missing values in crucial columns (`overview`, `genres`, `keywords`, etc.) are dropped.
   - Duplicate records are removed to avoid redundancy.

2. **Feature Extraction and Transformation**  
   - **Genres & Keywords:** Extracted from JSON format and converted into a list of words.  
   - **Cast:** Only the top 3 actors are considered for better representation.  
   - **Crew:** Only the **director** is extracted as it plays a key role in movie recommendations.  
   - **Overview (Plot Summary):** Converted into a list of words to be used for text processing.

3. **Text Cleaning and Formatting**  
   - Spaces between words are removed (e.g., `"Science Fiction"` → `"ScienceFiction"`) to avoid multi-word terms being split.  
   - Stop words (common words like "the", "and", "of") are removed to focus on important terms.  
   - **Tokenization:** Overview text is split into words for further processing.

4. **Creating a Unified Feature (`tags`)**  
   - A **single feature** (`tags`) is created by combining `overview`, `genres`, `keywords`, `cast`, and `crew`.  
   - Example:  
     ```
     ["action", "adventure", "hero", "war", "BradPitt", "ChristopherNolan"]
     ```
   - This feature represents the **movie's essence** and is used for similarity calculations.

---

#### **4. Feature Engineering using NLP (Text Processing)**  
Since the `tags` column consists of textual data, **Natural Language Processing (NLP)** techniques are applied:

1. **Stemming using Porter Stemmer**  
   - Words are reduced to their root form (e.g., `"loving" → "love"`, `"fighting" → "fight"`) to maintain consistency.
   - This helps in improving the similarity calculation by treating similar words as the same.

2. **Vectorization using CountVectorizer**  
   - The `tags` column is converted into **numerical feature vectors** using the **Bag-of-Words (BoW) model**.  
   - `CountVectorizer` is used to create a matrix where each movie is represented as a vector of **top 5000 frequent words** (excluding stop words).  

---

#### **5. Similarity Calculation using Cosine Similarity**  
Once all movies are converted into numerical vectors, **cosine similarity** is used to measure the similarity between two movies:

- **Cosine Similarity Formula:**  
  \[
  \text{similarity} = \frac{A \cdot B}{||A|| \times ||B||}
  \]
- It calculates the **angle between two movie vectors**. A **smaller angle** means **higher similarity**.
- This technique helps identify the top 5 most similar movies for a given input.

Example:  
If a user searches for `"Spectre"`, the model finds movies with the closest feature representation and recommends similar ones.

---

#### **6. Movie Recommendation Function**  
The function takes a **movie title** as input, finds its vector representation, and compares it with all other movies using cosine similarity. It returns the **top 5 most similar movies**.

- The **recommend function**:  
  - Finds the **index** of the input movie.  
  - Retrieves similarity scores for all movies.  
  - Sorts movies by similarity scores (excluding itself).  
  - Returns the top 5 most similar movies.

Example:  
For `"John Carter"`, the function might return:  
1. Avatar  
2. Star Wars  
3. Guardians of the Galaxy  
4. The Martian  
5. Interstellar  

---

#### **7. Deploying the Model using Gradio**  
To make the system **interactive**, a **Gradio web interface** is built. **Gradio** is a Python library that allows users to interact with machine learning models through a user-friendly web app.

1. **Fetching Movie Posters**  
   - Uses the **TMDB API** to get high-quality movie posters for recommended movies.  
   - If no poster is available, a placeholder image is used.

2. **Building the UI with Gradio Blocks**  
   - **Input Box**: Users enter a movie name.  
   - **Recommend Button**: Triggers the recommendation function.  
   - **Gallery**: Displays the top 5 recommended movies with posters.

3. **Launching the Web App**  
   - The app is **hosted locally** and can also be shared using **Gradio's sharing feature**.  
   - Users can access the recommendation system via a simple interface.

---

#### **8. Conclusion**  
The **movie recommendation system** efficiently suggests similar movies based on genres, keywords, cast, crew, and overview. It leverages **NLP, cosine similarity, and machine learning techniques** to analyze and compare movies. The **Gradio interface** makes it accessible for users by providing a simple web-based recommendation tool. Future improvements can include **collaborative filtering** (user-based recommendations) and **deep learning models** to enhance accuracy.

