Project description : 
step 1: searching for  a music dataset
cleaning, preprocessing making the EDA of the dataset Spotify_Songs.csv
taking the columns needed for the recommendation system and make a new dataset final_data.csv
calculating the similratity between the songs of the dataset (similiraity of the genre and the subgenre ..)
calculating the similarity  after vectorizing the data.
make the recommendion function that is based of the similarity (sorted top 4 similar) 
pickling the similarity metric with pickle
step 2: making the flask API 
requesting data from the final_dataset.csv (track_name) and call the recommend function in order to get the top 4 songs most similar 
requesting urls and posters of the recommended songs from spotify API (spotify for developers, spotifpy) with the help of ID CLIENT ...
step 3: making the template
html template is done with its css style
calling for the recommend function with ajax request to the flask endpoint to get the recommended songs displayed in the template using javascript (while clicking on the button recommend)
(the recommend songs gonna be displayed with their names urls to spotify and posters)  
