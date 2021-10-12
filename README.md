Ativação de .venv:

Windows:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
```
py -3 -m venv .venv
```
```
.venv\Scripts\activate
```
```
copy env-sample .env
```
```
pip install -r requirements.txt
```

Ubuntu:
```
python3 -m venv .venv
```
```
source .venv/bin/activate
```
```
cp env-sample .env
```
```
pip install -r requirements.txt
```

Baixar atualizações:
```
git pull
```

Incluir atualizações:
```
git status
```
```
git add .
```
```
git commit -m'Info da atualização'
```
```
git push
```

Retornar para ultima versão salva no git:
```
git checkout .
```

Criar executavel:
1º - Acessar pasta onde o executavel está via CMD:
```
cd <caminho>
```
```
pyinstaller <arquivo.py> --windowed --clean --noconfirm --onefile
```
