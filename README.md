# Python Cloud Lab API (GCP)

Ce projet est une API simple construite avec FastAPI, conçue pour être déployée et testée facilement. Elle inclut des endpoints de santé (readiness et liveness) ainsi qu'une route racine.

---

## **Installation**

1. **Clonez le dépôt** :
   ```bash
   git clone <url_du_dépôt>
   cd <nom_du_dossier>
   ```

2. **Créez un environnement virtuel** (optionnel) :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows : .\venv\Scripts\activate
   ```

3. **Installez les dépendances** :
   ```bash
   pip install fastapi uvicorn
   ```

---

## **Lancer l'application**

Pour démarrer l'application en local :

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

L'API sera disponible à l'adresse suivante : [http://127.0.0.1:8080](http://127.0.0.1:8080).

---

## **Endpoints**

### **1. Root Endpoint**

- **Description** : Retourne un message de bienvenue.
- **Méthode** : `GET`
- **URL** : `/`
- **Exemple de réponse** :
  ```json
  {
    "message": "Welcome to my Python Kubernetes Lab API!"
  }
  ```

---

### **2. Readiness Endpoint**

- **Description** : Vérifie si l'application est prête à recevoir des requêtes.
- **Méthode** : `GET`
- **URL** : `/health/ready`
- **Exemple de réponse** :
  ```json
  {
    "status": "ready"
  }
  ```

---

### **3. Liveness Endpoint**

- **Description** : Vérifie si l'application est en cours d'exécution.
- **Méthode** : `GET`
- **URL** : `/health/live`
- **Exemple de réponse** :
  ```json
  {
    "status": "alive"
  }
  ```