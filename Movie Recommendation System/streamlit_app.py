import streamlit as sl
import pickle
import pandas as pd
similarity = pickle.load(open("similarity.pkl", 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open("movie_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)
sl.title("Dipesh's Movie Recommendation System using Cosine Distance")

selected_movie_name = sl.selectbox(
    "Select a movie", movies['title'].values
)

# root = Tk()
# root.title("Welcome to Dipesh's Movie Recommendation System")
# root.geometry('1280x720')

# # adding a label to the root window
# lbl = Label(root, text="Movie Recommendation System?")
# lbl.grid()

# variable = StringVar()
# variable.set(movies['title'].values[0])  # default value

# w = OptionMenu(root, variable, *movies['title'].values)
# w.grid(column=0, row=5)
# # button widget with red color text
# # inside
# rm = recommend(variable.get())
# btn = Button(root, text="Recommend",
#              fg="red", command=rm)
# # set Button grid
# btn.grid(column=0, row=1)
# OPTIONS = [
#     "Jan",
#     "Feb",
#     "Mar"
# ]  # etc


# # Execute Tkinter
# root.mainloop()
if sl.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    sl.write("Movies you would like: ")
    for i in recommendations:
        sl.write(i)
