import pandas as pd

filename = "data.tsv"
filepath = "moviedata/"
foldernames = ["name_basics/", "title_akas/", "title_basics/",
                "title_crew/", "title_principals/", "title_ratings/"]

# Trim name_basics by removing birthYear and deathYear
nBasicsDF = pd.read_csv(filepath+foldernames[0]+filename, sep="\t")

# Dropping Columns
nBasicsDF = nBasicsDF.drop('birthYear', axis=1)
nBasicsDF = nBasicsDF.drop('deathYear', axis=1)


# Trim akas by region US and remove ordering, attributes, region, isOriginalTitle, and types
akasDF = pd.read_csv(filepath+foldernames[1]+filename, sep="\t")

akasDF = akasDF[akasDF['region'] == 'US'] # Check for region US

# Dropping Columns
akasDF = akasDF.drop('ordering', axis=1)
akasDF = akasDF.drop('attributes', axis=1)
akasDF = akasDF.drop('region', axis=1)
akasDF = akasDF.drop('isOriginalTitle', axis=1)
akasDF = akasDF.drop('types', axis=1)

# Trim title_basics by movie and remove endYear
tBasicsDF = pd.read_csv(filepath+foldernames[2]+filename, sep="\t")

tBasicsDF = tBasicsDF[tBasicsDF['titleType'] == 'movie'] # Check for movies

tBasicsDF = tBasicsDF.drop('endYear', axis=1) # Dropping endYear column

# Trim crew by movie and remove endYear
crewDF = pd.read_csv(filepath+foldernames[3]+filename, sep="\t")

crewDF = crewDF[crewDF['titleType'] == 'movie'] # Check for movies

crewDF = crewDF.drop('endYear', axis=1) # Dropping endYear column

# Trim principals by removing ordering, category, job, and characters
principalsDF = pd.read_csv(filepath+foldernames[4]+filename, sep="\t")

# Dropping Columns
principalsDF = principalsDF.drop('ordering', axis=1)
principalsDF = principalsDF.drop('category', axis=1)
principalsDF = principalsDF.drop('job', axis=1)
principalsDF = principalsDF.drop('characters', axis=1)

# Trim ratings by removing numVotes
ratingsDF = pd.read_csv(filepath+foldernames[5]+filename, sep="\t")

ratingsDF = ratingsDF.drop('numVotes', axis=1)
