import csv

movies = {}
with open('movies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        index = row['movieId']
        title = row['title']
        movies[index] = row['title']

ratings = {}
with open('ratings.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        userId = row['userId']
        movieId = row['movieId']
        rating = row['rating']
        ratings.setdefault(userId, {})
        ratings[userId][movies[movieId]] = float(rating)


def getMovieID(movie_name):
    for i in range(len(movies)):
        if movie_name in str(movies[i][1]):
            return i
    return False

def simPearson(prefs, p1, p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1

    n = len(si)

    if n==0:
        return 0

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])

    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq - pow(sum1,2)/n)*(sum2Sq - pow(sum2,2)/n))

    if den==0:
        return 0

    r = num/den
    return r


def getRecommendations(prefs, person, similarity=simPearson):

    totals = {}
    simSums = {}
    for other in prefs:
        #skip Toby
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies Toby hasn't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                simSums.setdefault(item, 0)
                simSums[item] += sim
    rankings = [(total / simSums[item], item) for (item, total) in
                totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


def topMatches(prefs, person, n=5, similarity=simPearson):
    scores=[(similarity(prefs,person,other),other)
            for other in prefs if other!=person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

simPearson(ratings, 1, 2)
#print(getMovieID('Sabrina'))
#print(getMovieID('Toy Story'))
