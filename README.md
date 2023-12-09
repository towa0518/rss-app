# RSS取得
## 環境
Python 3.9.7
## 環境構築(Windows PowerShell)
1. 仮想環境を作成する
```powershell
python -m venv .venv
```
2. 仮想環境を有効化
```powershell
.venv\Scripts\activate.ps1
```
3. パッケージをインストール
```poweshell
pip install -r .\requirements.txt
```
4. .envを作成
```powershell
Copy-Item .\.env.example .\.env
```
5. .envの`URL`に取得したいRSSのURLを設定

## バックエンドサーバー(FastAPI)の立ち上げ
```powershell
uvicorn main:app --reload

```
- ルート: http://127.0.0.1:8000/
- RSS取得: http://127.0.0.1:8000/rss
