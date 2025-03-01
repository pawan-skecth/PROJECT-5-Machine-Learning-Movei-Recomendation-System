!pip install gradio
import gradio as gr
import requests

# TMDB API Key - replace with your valid API key
API_KEY = "your_tmdb_api_key_here"

# Function to fetch movie posters from TMDB API
def fetch_poster(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/500x750?text=No+Image+Available"

# Trained recommendation model logic
def recommend_function(movie):
    # Replace this logic with your actual implementation
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []
    for i in movies_list:
        recommendations.append(new_df.iloc[i[0]].title)
    return recommendations

# Gradio Interface Function
def recommend_movies_ui(movie_name):
    # Get recommendations from the trained model
    recommendations = recommend_function(movie_name)
    # Fetch posters for recommended movies
    posters = [fetch_poster(movie) for movie in recommendations]
    # Combine titles and posters
    results = [(poster, movie) for poster, movie in zip(posters, recommendations)]
    return results

# Define Gradio Interface
with gr.Blocks() as movie_recommendation_app:
    gr.Markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>")
    with gr.Row():
        with gr.Column():
            movie_name_input = gr.Textbox(label="Enter a Movie Name", placeholder="E.g., The Matrix")
            recommend_button = gr.Button("Recommend")
        with gr.Column():
            output_gallery = gr.Gallery(label="Recommended Movies")

    recommend_button.click(
        recommend_movies_ui,
        inputs=[movie_name_input],
        outputs=[output_gallery]
    )

# Launch the Gradio app
movie_recommendation_app.launch(share=True)
