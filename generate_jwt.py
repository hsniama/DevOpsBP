import jwt


JWT_SECRET = "1720844446" 

def create_jwt():
    # Define el payload sin fecha de expiración
    payload = {"some": "data"}  # Puedes ajustar el payload según sea necesario
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

# Genera y muestra el JWT
jwt_token = create_jwt()
print("Generated JWT:", jwt_token)
