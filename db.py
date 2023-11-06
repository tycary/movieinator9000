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


def find_people_that_work_on_movie(db, movie_id: str) -> list:
    collection = db["Movies_people_link"]
    return  list(collection.find({"tconst": movie_id}))

def find_other_movies_for_persion(db, person_id: str) -> list:
    collection = db["Movies_people_link"]
    return  list(collection.find({"nconst": person_id}).limit(5))


def main():
    print("\nFirst ouput +++")
    print(search_for_row_by_attribute(connect_db(), "Movies", "originalTitle", "Miss Jerry"))
    
    print("\nSecond ouput +++")
    print(count_movies_in_year(connect_db(), "Movies", 2017))

    print("\nThird ouput +++")
    print(average_runtime_in_year(connect_db(), "Movies", 2017))

    print("\nFourth output +++")
    director = find_people_that_work_on_movie(connect_db(), "tt0000001")[1]
    print(find_other_movies_for_persion(connect_db(), director["nconst"]))


if __name__ == "__main__":
    main()
