import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = 'c053c70157fbce0bf70bf81307bb0972'
redirect_uri = 'https://example.com/oauth'
authorize_code = '95aettXFa0N75H0AvXjpNbV1HaAfupGCLgP-Rl-h21XqiU9wbUIn3p6yq_EKPXLrAAABjvSlUzH7Ewsnpgvovw'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)