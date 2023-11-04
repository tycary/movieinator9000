import pandas as pd

filename = "data.tsv"
filepath = "moviedata/"
foldernames = ["name_basics/", "title_akas/", "title_basics/",
                "title_crew/", "title_principals/", "title_ratings/"]

# Trim name_basics by removing birthYear and deathYear
print("Reading in name_basics")
nBasicsDF = pd.read_csv(filepath+foldernames[0]+filename, sep="\t", low_memory=False)
nBasicsDF.set_index('nconst')

# Dropping Columns
nBasicsDF = nBasicsDF.drop('birthYear', axis=1)
nBasicsDF = nBasicsDF.drop('deathYear', axis=1)


# Trim akas by region US and remove ordering, attributes, region, isOriginalTitle, and types
print("Reading in akas")
akasDF = pd.read_csv(filepath+foldernames[1]+filename, sep="\t", low_memory=False)
akasDF.set_index('titleId')

akasDF = akasDF[akasDF['region'] == 'US'] # Check for region US

# Dropping Columns
akasDF = akasDF.drop('ordering', axis=1)
akasDF = akasDF.drop('attributes', axis=1)
akasDF = akasDF.drop('region', axis=1)
akasDF = akasDF.drop('isOriginalTitle', axis=1)
akasDF = akasDF.drop('types', axis=1)

# Trim title_basics by movie and remove endYear nad titleType
print("Reading in title_basics")
tBasicsDF = pd.read_csv(filepath+foldernames[2]+filename, sep="\t", low_memory=False)
tBasicsDF.set_index('tconst')

tBasicsDF = tBasicsDF[tBasicsDF['titleType'] == 'movie'] # Check for movies

# Dropping Columns
tBasicsDF = tBasicsDF.drop('endYear', axis=1)
tBasicsDF = tBasicsDF.drop('titleType', axis=1)

# Read in crew
print("Reading in crew")
crewDF = pd.read_csv(filepath+foldernames[3]+filename, sep="\t", low_memory=False)
crewDF.set_index('tconst')

# Trim principals by removing ordering, category, job, and characters
print("Reading in principals")
principalsDF = pd.read_csv(filepath+foldernames[4]+filename, sep="\t", low_memory=False)

# Dropping Columns
principalsDF = principalsDF.drop('ordering', axis=1)
principalsDF = principalsDF.drop('job', axis=1)
principalsDF = principalsDF.drop('characters', axis=1)

# Trim ratings by removing numVotes
print("Reading in ratings")
ratingsDF = pd.read_csv(filepath+foldernames[5]+filename, sep="\t", low_memory=False)
ratingsDF.set_index('tconst')

ratingsDF = ratingsDF.drop('numVotes', axis=1)

# Merge movie tables
movieDF = pd.merge(tBasicsDF, akasDF, left_on='tconst', right_on='titleId')
movieDF = movieDF.drop('titleId', axis=1)
movieDF = pd.merge(movieDF,crewDF)
movieDF = movieDF.drop_duplicates(subset='tconst')
print(movieDF)
movieDF.to_csv("moviedata/output/movie_data.tsv", index=False, sep="\t")

principalsDF = principalsDF.loc[principalsDF['tconst'].isin(movieDF['tconst'])]
principalsDF.to_csv("moviedata/output/principals_data.tsv", index=False, sep="\t")
print(principalsDF.shape)

nBasicsDF = nBasicsDF.loc[nBasicsDF['nconst'].isin(principalsDF['nconst'])]
nBasicsDF.to_csv("moviedata/output/name_data.tsv", index=False, sep="\t")
print(nBasicsDF.shape)