import rauth
import time
import json
 
def main():
    locations = ['Brooklyn,NY', 'Hoboken,NJ']
    """locations to process"""
    api_calls = []
    for cities in locations:
        params = get_search_parameters(cities)
        api_calls.append(get_results(params))
        #Be a good internet citizen and rate-limit yourself
        time.sleep(1.0)
    with open('C:\Python34\edwincode\yelpdata.txt', 'w') as outfile:
        json.dump(api_calls, outfile, indent=4)
    ##Do other processing
 
def get_results(params):

    jsonraw = {}
    #Obtain these from Yelp's manage access page
    consumer_key = "KmNIYTAHxDH1LHn23Bxplg"
    consumer_secret = "4X-NRJlHpJjd9TUByhNFMNUYRbY"
    token = "V101rI2cz8dEd-hZuJcROvM_7A6dhU72"
    token_secret = "rXsMIwQIspm36-HW-jmML2eGJiw"
    session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
    request = session.get("http://api.yelp.com/v2/search",params=params)
    #Transforms the JSON API response into a Python dictionary
    data = request.json()
    for business in data['businesses']:
        jsonraw.update({business['id']: str(business['location']['city']) + ',' + str(business['name']) + ',' + str(business['rating'])})
    session.close()
    return jsonraw
    """throws jsonraw back to main, each restaurant gets its own record"""

def get_search_parameters(cities):
    #See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["location"] = cities
    params["radius_filter"] = "2000"
    params["limit"] = "10"
 
    return params
 
if __name__=="__main__":
    main()
