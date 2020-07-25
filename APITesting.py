import requests as req
import json
# import jsonpath as jp 

test = input("GET / POST / PUT ?")

if test.casefold() == "get":
    #GET Data to be checked
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("**API GET Started**")
    url ="https://reqres.in/api/users?page=751"

    res = req.get(url)

    with open('geres.json', 'w') as f:
        f.write(res.text)
        print("**API GET Completed**")
    print("-----------------------------------------------------------------------------------------------------------------------------")

elif test.casefold() == "post":
    #POST Data to be fetched
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("**API POST Started**")
    url ="https://reqres.in/api/users"

    with open ('poreq.json', 'r') as i:
        cont = i.read()

    res = req.post(url, cont)

    assert res.status_code == 201

    with open('pores.json', 'w') as f:
        f.write(res.text)
        print("**API POST Completed**")
    print("-----------------------------------------------------------------------------------------------------------------------------")

elif test.casefold() == "put":
    #PUT Request - Insert Data
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("**API PUT Started**")
    url ="https://reqres.in/api/users/751"

    with open ('pureq.json', 'r') as i:
        cont = i.read()

    res = req.put(url, cont)

    assert res.status_code == 200

    with open('pures.json', 'w') as f:
        f.write(res.text)
        print("**API PUT Completed**")
    print("-----------------------------------------------------------------------------------------------------------------------------")