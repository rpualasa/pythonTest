import json
import requests

##### Below  is the api we are using #####
api_url = "https://jsonplaceholder.typicode.com/"

#### Below Test Validates the API is working or not ####
def test_validate_url():
    response = requests.get(api_url)
    assert response.status_code == 200
    
##### Test 3: to use post http method and validate tile and fetch the user id #####
def test_callby_title():
    
    ## Given payload ##
    payload = {'title': 'optio molestias id quia eum'}
    
    ## Below is the post http request, with endpoint as "posts" and with given payload ##
    res = requests.post(api_url + "posts", json=payload)
    
    ## Below command json.loads will helps us to receive the data from json to python ##
    response = json.loads(res.text)
    
    ## Get the status code ##
    code = res.status_code
    
    ## Assert the status code we received
    assert code == 201, "did not match"
    print(response)
    print(code)
    
    ## Storing the "id" we received from the above request ##
    stored_id = response['id']
    
    ## Storing the JSON response ##
    get_response_All_data = res.json();
    print(get_response_All_data)
    
    """ Asserting the  title, if title equals given payload, no error will be displayed.\
        Else error will be displayed """
    assert get_response_All_data['title']==payload['title'], 'title does not match'


#### TEST 4 : using "id" as  endpoint  received from the above test ####

## test does not work, because, the api responds with id as 101, which is not available on the Typicode ##
## However, on given another id, it works ##

    ##Below is the get http request with endpoint used as posts and received id ##
    test4 = requests.get(api_url + f'posts/{stored_id}')
    # test4 = requests.get(api_url + 'posts/10')
    assert test4.status_code == 200
    test_4 = test4.json()
    print(test_4)
    
#### TEST 5: using "id" as endpoint input to find the "Comments"
    
    ##Below is the get http request with endpoint used as posts, received id and comments ##
    test5 = requests.get(api_url + f'posts/{stored_id}/comments')
    
    assert test5.status_code == 200
    test_5 = test5.json()
    print(test_5)