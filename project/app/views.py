import bcrypt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import json

# MongoDB connection
client = MongoClient("mongodb+srv://avasanth081:vasanth@cluster0.ed7yf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["userdetails"]  # Replace with your database name
users_collection = db["user"]  # Replace with your collection name

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")
            confirm_password = data.get("confirm_password")

            # Check if passwords match
            if password != confirm_password:
                return JsonResponse({"error": "Passwords do not match."}, status=400)

            # Check if the user already exists
            if users_collection.find_one({"email": email}):
                return JsonResponse({"error": "User already exists."}, status=400)

            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

            # Save user to MongoDB
            user = {"name": name, "email": email, "password": hashed_password.decode("utf-8")}
            users_collection.insert_one(user)

            return JsonResponse({"message": "User registered successfully."}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            # Find the user in MongoDB
            user = users_collection.find_one({"email": email})
            if not user:
                return JsonResponse({"error": "Invalid email or password."}, status=400)

            # Verify the password
            if not bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
                return JsonResponse({"error": "Invalid email or password."}, status=400)

            return JsonResponse({"message": "Login successful."}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

