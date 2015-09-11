__author__ = 'mini'
import requests

def convert(fromcurrency,tocurrency,amount):

    uri = "http://api.fixer.io/latest?base=%s" % fromcurrency

    data=requests.get(uri)

    response=requests.get(uri)

    #todo check for 200

    data=response.json()

    return data['rates'][tocurrency]*amount