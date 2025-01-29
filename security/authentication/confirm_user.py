import boto3

user_pool_id = 'us-east-1_F8jtObheG'
username = 'test-ua'
password = '1q2w3e$R'

client = boto3.client(
    'cognito-idp',
    region_name= 'us-east-1',
)
response = client.admin_set_user_password(
    UserPoolId=user_pool_id,
    Username= username,
    Password= password,
    Permanent=True                    # 비밀번호를 영구적으로 설정
)
print(response)

# This code will occur error if the function above returns 200
response = client.admin_confirm_sign_up(
    UserPoolId = user_pool_id,
    Username = username
)
print(response)
