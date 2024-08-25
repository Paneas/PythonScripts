
import json
import http.client

def run_Script():
    home = 'localhost:5103'
    headers = {'Content-type': 'application/json'}

    url = "/UpdateAccount"
    conn = http.client.HTTPConnection(home)

    for iter in range(0, 60):
        
        data = {"AccountId" : "c60d6554-1091-4560-aea7-ef4c8f91c7c9",
                "Name": "NewName",
                "Phone" : "6969696969"
                }
        
        print(json.dumps(data))
        conn.request('POST', url, json.dumps(data), headers)

        response = conn.getresponse()
        print(response.read().decode())

if __name__ == '__main__':
    run_Script()