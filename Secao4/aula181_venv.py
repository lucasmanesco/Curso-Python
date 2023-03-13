"""
Ambientes Virtuais em Python (venv)
- Um ambiente virutal carrega toda a sua instalação
do python para uma pasta no caminho escolhido.
- Ao ativar um ambiente virtual, a instalação do
ambiente virtual será usada.
- venv é o módulo que vamos usar para criar
ambientes virtuais.
- Você pode dar o nome que preferir para um
ambiente virtual, mas o mais comuns são:
venv env .venv .env
"""

# no powershell
#1 criar ambiente virtual: python -m venv venv
#2 visualizar caminho do python.exe: gcm python -Syntax
#3 ativando o venv: venv\Scripts\activate
#4 desativar: deactivate
#5 visualizar caminho do python venv: gcm python -Syntax
#6 instalar pacotes: pip install pymysql
#7 atualizar pacote: pip install pymysql --upgrade
#8 desinstalar pacote: pip uninstall mysql
#9 verificar pacotes instalados: pip freeze
#10 verificar versões instaladas: pip index version pymysql
#11 gerar requirements: pip freeze > requirements.txt
#12 apagar pasta venv: rm venv
#13 instalar requirements: pip install -r .\requirements.txt
