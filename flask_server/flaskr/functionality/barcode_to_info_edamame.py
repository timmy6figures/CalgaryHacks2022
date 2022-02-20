import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import json

def get_product_information(barcode=None, keyword=None, other_params=None):
    """
    :param barcode: The barcode of the product trying to be found
    :param keyword: The name of the product (e.g. apple)
    :param other_params: Any other paramaters you may want to add to the query. List of queries can be found here:
    https://developer.edamam.com/food-database-api-docs#/
    :return: The json string of the response from the api
    """
    url = 'https://api.edamam.com/api/food-database/v2/parser'
    headers={'Content-Type':'appplication/json'}
    params={'app_id':'1a92f936', 'app_key':'b215ad19c437e29706a5c36b4e197016', 'upc':barcode}
    if barcode:
        params['barcode'] = barcode
    # This is ELSE if to make sure only one is send in the paramaters.
    # The default for the ali is to ignore the keyword if both are present
    elif keyword:
        params['ingr'] = keyword
    if other_params:
        params.update(other_params)
    r = requests.get(url, headers=headers, params=params)
    return r.json()

def main():

    # This is not tested:
    information_wanted = {'health':'keto'}
    information_wanted = {}

    requested_food = input("Enter the food you want to search for:")
    response = get_product_information(keyword=requested_food,other_params=information_wanted)
    # response = get_product_information(barcode='038000576089',other_params=information_wanted)

    # These json files can be confusing. Use this website to visualize the data:
    # http://jsonviewer.stack.hu/
    # print(response)

    # There are two parts to the response. 'parsed' and 'hints'.
    # parsed looks like the information we want, and hints is like other products that are similar
    # E.G. there is not a parsed section for frosted flakes, but under hints it shows "Corn flakes"
    # Try to get the parsed. If that fails, default to the first hint
    basic_facts = None
    try:
        basic_facts = response['parsed'][0]['food']
    except:
        print("Lookup failed! Defaulting to similar products")
        num_of_similar_products = len(response['hints'])
        for i in range(0,num_of_similar_products,1):
            print("Num of products: ", i)
            try:
                basic_facts = response['hints'][i]['food']
                break
            except:
                # Dummy code
                error_num = i

    try:
        print("---Your food is:---")
        print(basic_facts['label'])
        print(basic_facts['image'])
        print("Calories: ", basic_facts['nutrients']['ENERC_KCAL'])
        print("Fat content: ", basic_facts['nutrients']['FAT'])
        print("Fiber content: ", basic_facts['nutrients']['FIBTG'])
        print("Protein content: ", basic_facts['nutrients']['PROCNT'])
    except:
        print("Error printing results")

if __name__ == '__main__':
    main()