import requests
import json 

##### Below  is the api we are using #####
api_url = "https://jsonplaceholder.typicode.com/todos/1"

#### Test 2: To update data ####
def test_update_data():
    
     ## Below is the get http request ##
    get_Req = requests.get(api_url)
    
    ## It returns the json-encoded content of a response ##
    get_Req.json()
    
    ## Below command json.loads will helps us to receive the data from json to python ##
    get_Data = json.loads(get_Req.text)
    
    ## Prints the requested json ##
    print(get_Data)
    
    ## fetch the status code and store in the variable ##
    status_Code_Get = get_Req.status_code
    
    ## Assertion applied on the received http status ##
    assert status_Code_Get ==200,"did not match"
    print(status_Code_Get, "\n")

    print("Updated data below:")
    
    ## Below is a payload given ##
    update_Data = {"userId": 1,"id":2, "title": "pytest update request", "completed": True}
    
    ## Below is the put http request with payload ##
    response_Req = requests.put(api_url, json=update_Data)
    response_Req.json()
    
    ## fetch the status code and store in the variable ##
    get_ResData = json.loads(response_Req.text)
    print(get_ResData)

    ## Assertion applied on the received http status ##
    status_Code = response_Req.status_code
    assert status_Code ==200,"did not match"
    print(status_Code)