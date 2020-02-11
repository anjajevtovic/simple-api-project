import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "
    
    for language in languages:
        query += f"language:{language} "

    return query

def repos_with_most_stars(languages, sort="stars",order="desc"):
    git_search_api = "https://api.github.com/search/repositories"

    #parameters = {"q":"stars:>50000"}
    query = create_query(languages)
    parameters = {"q":query, "sort":sort,"order":order}
    response = requests.get(git_search_api, params=parameters)
    
    status_code = response.status_code

    if status_code != 200:
        #It justs exists the code
        raise RuntimeError(f"An err has occured. Status code was {status_code}")
    else:
        response_json = response.json()["items"]
        return response_json
    


if __name__ == "__main__":
    #have a main method here
    languages = ["Python", "JavaScript", "Node"]
    results = repos_with_most_stars(languages)
    print(len(results))

   # query = create_query(languages)
    #print(f"my query: {query}")
    
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")