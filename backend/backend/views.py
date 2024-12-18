from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Désactive la protection CSRF pour le développement (ou utilise un token CSRF en production)
def login_view(request):
    if request.method == 'POST':
        try:
            # Charger les données JSON depuis request.body
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Connexion de l'utilisateur
                return JsonResponse({"message": "Login réussi!"}, status=200)
            else:
                return JsonResponse({"error": "Nom d'utilisateur ou mot de passe incorrect."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Format de données incorrect."}, status=400)
    else:
        return JsonResponse({"error": "Méthode non autorisée."}, status=405)

@csrf_exempt  # Désactive la protection CSRF pour le développement (ou utilise un token CSRF en production)
def register_view(request):
    if request.method == 'POST':  # Vérifie que la méthode est bien POST
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']

            # Vérification si l'utilisateur existe déjà
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Nom d'utilisateur déjà pris"}, status=400)

            # Création de l'utilisateur
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({"message": "Utilisateur créé avec succès!"}, status=201)
        except KeyError:
            return JsonResponse({"error": "Les champs 'username' et 'password' sont requis"}, status=400)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

def check_username(request, username):
    try:
        # Vérifie si le nom d'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            return JsonResponse({"exists": True}, status=200)
        else:
            return JsonResponse({"exists": False}, status=200)
    except Exception as e:
        # Retourner une erreur en cas d'exception
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt  # Désactive la protection CSRF pour le développement, sinon utiliser un token CSRF
def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Déconnecte l'utilisateur
        return JsonResponse({"message": "Déconnexion réussie!"}, status=200)
    return JsonResponse({"error": "Méthode non autorisée."}, status=405)