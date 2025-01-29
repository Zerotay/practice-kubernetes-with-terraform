# text = "test"
# test1 = text.encode()
# test2 = base64.b64encode(test1)

import argparse
import base64
import json
import os
from enum import Enum

import requests

import hmac
import hashlib
# SECRET_HASH 생성 함수
def calculate_secret_hash(client_id, client_secret, username):
    message = username + client_id
    dig = hmac.new(client_secret.encode('utf-8'), 
                   message.encode('utf-8'), 
                   hashlib.sha256).digest()
    return base64.b64encode(dig).decode()

# 요청 보낼 URL
kube_url = "https://192.168.80.250:6443/api/v1/namespaces/default/pods/debug?limit=500"
curr_dir = os.getcwd()

# 요청 헤더 설정
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer zerotay"
}

# 요청 바디 설정 (JSON 형식)
data = {
    "key1": "value1",
    "key2": "value2"
}

class AuthType(Enum):
    x509 = "x509"
    static = "static"
    bootstrap = "bootstrap"
    webhook = "webhook"
    oidc = "oidc"
    satoken = "satoken"

def request_in_x509():
    headers = {
        "Content-Type": "application/json",
    }
    user_crt = curr_dir + "/x509/ua.pem"
    user_key = curr_dir + "/x509/ua-key.pem"
    response = requests.get(
            url= kube_url, 
            headers=headers, 
            verify= curr_dir+"/ca.crt",
            cert=(user_crt, user_key),
    )
    return response

def request_in_static():
    token = "zerotay"
    headers = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer " + token
    }
    response = requests.get(
            url= kube_url, 
            headers=headers, 
            verify= curr_dir+"/ca.crt",
    )
    return response

def request_in_satoken():
    # This is JWT token for test-sa
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImpOY0ZkRmtHV3phd2Qzek5nWjdxSmRzUWlMUERZMlBQRmxYYTB2cUYxRm8ifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzM3NzA3NjM2LCJpYXQiOjE3Mzc3MDQwMzYsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiZDVkY2EyZWMtNzg1Zi00MTY1LWE1YTEtOWVjNTg0ZTdjYWRjIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6InRlc3Qtc2EiLCJ1aWQiOiJmZTJkZmJiMi0zYjg3LTRmZWUtYTAyNS0wYjQ2Zjg0MDg5N2UifX0sIm5iZiI6MTczNzcwNDAzNiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6dGVzdC1zYSJ9.nG-pwMHGlmH0pW6Qj3rdhRCZGQdQUDUZhtocUUtBG2RbKSzltpPWvdtx6r-8ZKXOOfvZdBC8GuoVqHOE1Tc3siWKl1eIA2wMXyaJI8MvZPUW8-8PTy4XN9Bjb7YxJHbwT6YTwA5B4v0n37AbUfWCNIh1ZgR7xpfVM4C1Qr98lQCKBJK_pak53DcKmDyeVvNuBvgq3F_irzNLK4tZkXphuHjm5r-4ehEQZeMeRdo_6pbqBtUKgkgXHt3V3XDDfnM-SHpfOYKabv_igvHqjSn9ijAwQgupJMLaaCPl_QApKAq-T_K6kTXPkOR0CvVwbqPf24lB8VtzqUFozsEIP_XRGA"
    headers = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer " + token
    }
    response = requests.get(
            url= kube_url, 
            headers=headers, 
            verify= curr_dir+"/ca.crt",
    )
    return response

def request_in_oidc():
    # data = {
    #     "grant_type": "password",
    #     "client_id": "mlad9fi16j8t5q9drbge2j6r",
    #     "client_secret": "1e6seaub7uj72m66njncuhop0jqjgc14b465vqg0biltme1ohln5",
    #     "username": "zerogun1000",
    #     "password": "1q2w3e$R",
    #     "scope": "openid"
    # }
    # response = requests.post(
    #     'https://us-east-1f8jtobheg.auth.us-east-1.amazoncognito.com/oauth2/token',
    #     data=data,
    #     headers={'Content-Type': 'application/x-www-form-urlencoded'}
    # )
     
    # This is Amazone api url
    aws_url = "https://cognito-idp.us-east-1.amazonaws.com/"
    client_id = "mlad9fi16j8t5q9drbge2j6r"
    client_secret = "1e6seaub7uj72m66njncuhop0jqjgc14b465vqg0biltme1ohln5"
    username= "test-ua"
    password= "1q2w3e$R"
    # SECRET_HASH has to be made, if needed
    secret_hash = calculate_secret_hash(client_id, client_secret, username)

    headers = {
      'Content-Type': 'application/x-amz-json-1.1',
      'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth'
    }
    data = {
      "AuthFlow": 'USER_PASSWORD_AUTH',
      "ClientId": client_id,
      "AuthParameters": {
         "USERNAME": username,
         "PASSWORD": password,
         "SECRET_HASH": secret_hash
      }
    }
    response = requests.post(url=aws_url,json=data,headers= headers)

    # print(json.dumps(response.json(), indent=2))
    id_token:str = response.json()["AuthenticationResult"]["IdToken"]
    print("\nThis is IdToken", id_token[:20],"...")
    print(id_token)
    headers = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer " + id_token
    }
    response = requests.get(
            url= kube_url, 
            headers=headers, 
            verify= curr_dir+"/ca.crt",
    )
    return response

def main(args: argparse.Namespace):
    type: AuthType = args.type
    print("Test for ", type)
    response = requests.models.Response()
    match type:
        case AuthType.x509:
            response = request_in_x509()
        case AuthType.static:
            response = request_in_static()
        case AuthType.satoken:
            response = request_in_satoken()
        case AuthType.oidc:
            response = request_in_oidc()
        case AuthType.bootstrap:
            pass
        case AuthType.webhook:
            pass

    print(response.status_code)
    print('Response Header :::::')
    print(json.dumps(dict(response.headers), indent=2))
    print('Response Body :::::')
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="put subcommand")
    parser.add_argument("--type", type=AuthType, required=True, help="x509, static, bootstrap, webhook, oidc, satoken")
    args = parser.parse_args()
    main(args)


