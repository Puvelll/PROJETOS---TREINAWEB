from app import app
# Importa da pasta app, importa variavel/instancia app

@app.route("/ola")
def ola():
    return 'Olá, mundo em Flask!!'