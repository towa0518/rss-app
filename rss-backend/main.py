from dotenv import load_dotenv
from fastapi import FastAPI
import feedparser
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/rss")
def read_rss():
  url = os.environ.get("URL")

  d = feedparser.parse(url)
  return d
