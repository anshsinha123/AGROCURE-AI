from backend.app_server import app

print(f"Total routes: {len(app.routes)}")
for r in app.routes:
    path = getattr(r, 'path', '')
    methods = getattr(r, 'methods', '')
    name = getattr(r, 'name', '')
    print(f"{list(methods) if methods else ''} {path} -> {name}")
