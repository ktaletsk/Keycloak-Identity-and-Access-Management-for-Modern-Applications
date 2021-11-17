from keycloak import KeycloakOpenID

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8081/auth/",
                    client_id="pyclient",
                    realm_name="myrealm")

# Get Token
token = keycloak_openid.token("<username>", "<password>")

print(token)

userinfo = keycloak_openid.userinfo(token['access_token'])

print(userinfo)
