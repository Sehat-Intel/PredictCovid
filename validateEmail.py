import requests

api_key = "03dc6598-2b78-4316-b924-9bf38970bf26"

def validateEmail(email_address):
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address},
        headers = {'Authorization': "Bearer " + api_key })

    status = response.json()['status']
    if status == "valid":
        #print("email is valid")
        return True
    else:
        #print("email is invalid")
        return False

