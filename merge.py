import csv

with open ("movies.csv",encoding="utf-8")as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open ("final.csv","a+",encoding="utf-8")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

with open ("movie_links.csv",encoding="utf-8")as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_movies_links = data[1:] 

for movieItem in all_movies:
   
    posterFound = any(movieItem[8]in movie_link_item for movie_link_item in all_movies_links)
    print(posterFound)
    if posterFound:
        for movie_link_item in all_movies_links:
            if movieItem[8] == movie_link_item[0]:
                movieItem.append(movie_link_item[1])
                if len(movieItem) == 28:
                    with open ("final.csv","a+",encoding="utf-8") as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow(movieItem)