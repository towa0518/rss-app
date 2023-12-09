# RSS取得
## 環境
Python 3.9.7
Node 20.10.0
npm 10.2.5
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
pip install -r .\rss-backend\requirements.txt
```
4. FastAPI用.envを作成
```powershell
Copy-Item .\rss-backend\.env.example .\rss-backend\.env
```
5. .envの`URL`に取得したいRSSのURLを設定
6. nodeパッケージをインストール
```powershell
cd .\rss-frontend
npm install
```
## バックエンドサーバー(FastAPI)の立ち上げ
```powershell
cd .\rss-backend
uvicorn main:app --reload

```
- ルート: http://127.0.0.1:8000/
- RSS取得: http://127.0.0.1:8000/rss

## フロントエンド(Nextjs)の立ち上げ
```powershell
cd .\rss-frontend
npm run dev
```
- トップ: http://localhost:3000/
