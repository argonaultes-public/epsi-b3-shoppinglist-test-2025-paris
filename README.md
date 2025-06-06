# Lists

## Bien démarrer

### Environnement virtuel

```bash
python -m venv .venv
. ./.venv/bin/activate
```

### Dépendances

```bash
pip install -r requirements.txt
```

## Initialiser l'environnement de développement

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Alimenter la BDD

```bash
python manage.py shell
```

Dans le shell

```python
ShopList.objects.create(shoplist_name='Instant Gaming summer')
ShopList.objects.create(shoplist_name='AWS summer')
ShopList.objects.create(shoplist_name='GCP christmas')
```

## Démarrer le serveur


```bash
python manage.py runserver 127.0.0.1:9090
```

Aller à l'adresse permettant d'afficher les listes d'achat : [http://127.0.0.1:9090/rendertpl](http://127.0.0.1:9090/rendertpl).