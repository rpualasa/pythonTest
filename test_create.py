import requests
import json 

##### Below  is the api we are using #####
api_url = "https://jsonplaceholder.typicode.com/posts"

##### Test 1: to create data #####
def test_create_data():
    ## below is payload stored in the variable "payload" ##
    payload={'id':102, 'title':'Pytest', 'body':'A quick brown fox jumps over the lazy dog'}
    
    ## Below is the post http request ##
    res = requests.post(api_url,payload)
    
    ## Below command json.loads will helps us to receive the data from json to python ##
    response = json.loads(res.text)
    
    ## Below we get our status code ##
    code = res.status_code
    
    ## Below is the assertion for the code we received in the above stored variable ##
    assert code ==201,"did not match"
    
    ## Below are the print commands that displays the Json output and status code
    print(response)
    print(code)