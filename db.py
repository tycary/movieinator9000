import pymongo
import re

DB_URL = "mongodb://localhost:27017"
DB_NAME = "Movienator9000"


def connect_db(): 
    """ 
    returns the connected DB as an object
    """
    client = pymongo.MongoClient("mongodb://localhost:27017")
    return client[DB_NAME] 


def search_for_row_by_attribute(db, document: str, attribute: str, search_term: str) -> list:
    """ 
    Usage:
        print(search_for_row_by_attribute(connect_db(), "Movies", "originalTitle", "Miss Jerry"))
    """
    collection = db[document]
    query = {attribute : search_term}  
    return [x for x in collection.find(query)]


def count_movies_in_year(db, document: str, year: int) -> int:
    """
    Returns the number of movies made in a year
    Usage:
        print(count_movies_in_year(connect_db(), "Movies", 2017))
    """
    collection = db[document]
    pipeline = [
        {"$match": {"startYear": year}},
        {"$group": {"_id": year, "count": {"$sum": 1}}
        }
    ]
    result = list(collection.aggregate(pipeline))
    return result[0]["count"] if result else 0


def average_runtime_in_year(db, document: str, year: int) -> float:
    """
    Returns the average length of a movie in a given year
    Usage:
        print(average_runtime_in_year(connect_db(), "Movies", 2017))
    """
    collection = db[document]
    pipeline = [
        {"$match": {"startYear": year}},
        {"$group": {"_id": year, "averageRuntime": {"$avg": "$runtimeMinutes"}}
        }
    ]
    result = list(collection.aggregate(pipeline))
    return result[0]["averageRuntime"] if result else 0


def fuzzy_search_by_title(db, document: str, title: str, tolerance: int) -> list:
    """
        Search for a title based while allowing for mispellings based on tolerance
        print(fuzzy_search_by_title(connect_db(), "Movies", search_term))
    """
    collection = db[document]
    pattern = re.compile('.*'.join(list(title[:2])) + '.*' + '.*'.join(list(title[tolerance:])), re.IGNORECASE)
    query = {"originalTitle": {"$regex": pattern}}
    return list(collection.find(query))


def find_related_movies(db, movie_id: str) -> list:
    collection = db["Movies_people_link"]
    movie_collection = db["Movies"]
    movie_persons = list(collection.find({"tconst": movie_id}))
    related_movies = []
    for person in movie_persons:
        person_id = person["nconst"]
        person_movies = list(collection.find({"nconst": person_id}))
        for person_movie in person_movies:
            related_movie_id = person_movie["tconst"]
            related_movie = movie_collection.find_one({"tconst": related_movie_id})
            if related_movie:
                related_movies.append(related_movie)
            if len(related_movies) >= 10: break
        if len(related_movies) >= 10: break
    return related_movies

def main():
    # print(search_for_row_by_attribute(connect_db(), "Movies", "originalTitle", "Miss Jerry"))
    print(count_movies_in_year(connect_db(), "Movies", 2017))
    print(average_runtime_in_year(connect_db(), "Movies", 2017))
    # print(fuzzy_search_by_title(connect_db(), "Movies", "Miss Jeray", 1))

    movie_id = "tt0000001" 
    related_movies = find_related_movies(connect_db(), movie_id)
    for movie in related_movies:
        print("Title:", movie["originalTitle"])
        print("Year:", movie["startYear"])
        print("-----")


if __name__ == "__main__":
    main()
