"Le projet qu'on va construire : Une API de gestion de notes.

Ce qu'on va construire :
- Une API REST complète avec Django REST Framework
- Authentification JWT sécurisée
- Class-Based Views avancées
- Tests automatisés avec pytest
- CI/CD avec GitHub Actions ou Gitlab Runner
- Tâches asynchrones avec Celery et Redis
- Déploiement en production
- Et même de l'infrastructure as code avec Terraform


"Avant de commencer, voyons la stack technique
qu'on va utiliser.

BACKEND :
- Django 5.0 - Le framework principal
- Django REST Framework - Pour l'API
- Python 3.10+

BASE DE DONNÉES :
- PostgreSQL en production
- SQLite pour le développement local

AUTHENTIFICATION :
- JWT avec django-rest-framework-simplejwt

TÂCHES ASYNCHRONES :
- Celery pour les tâches en arrière-plan
- Redis comme message broker

TESTS :
- Pytest et pytest-django
- Coverage pour vérifier la qualité

CI/CD :
- GitHub Actions ou Gitlab runner pour automatisation
- Tests automatiques sur chaque commit

DÉPLOIEMENT :
- Docker et docker-compose
- Railway ou AWS
- Terraform pour l'infrastructure

DOCUMENTATION :
- drf-spectacular pour Swagger
- Documentation API 

Voilà pour la stack. On va intégrer tout ça
progressivement, vidéo par vidéo."


VIDÉO 1 : set up projet
- Programme
- Django et telechargement des packages 
- Création de superuser pour l'administration
- Teste url

VIDÉO 2 : Class-Based Views
- ListView, 
- CreateView, 
- UpdateView, 
- TemplateView 

VIDÉO 3 : Class-Based Views
- DeleteView, 
- DetailView

VIDéo 4 : Class-Based Views/Auth et sécurité
- Création app accounts
- Mixins de sécurité
- Authentification

VIDÉO 5 : API REST avec ViewSet
- Serializers
- ViewSet CRUD complet
- Permissions

