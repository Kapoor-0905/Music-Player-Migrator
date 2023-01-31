from fastapi import FastAPI
from auth.credentials import *

from extract import *
from connect import *
from search_in_yt import *
from add_to_playlist import *

app = FastAPI()

@app.get("/spo_to_yu/{url:path}")
async def spo_to_yu(url: str):
    url = url.split("/")[-1].split("?")[0]
    api = connect(SP_CLIENT_ID, SP_CLIENT_SECRET)
    items_name = fetch_playlist_using_id(api, url)
    name = items_name[1]
    queries = query_builder(extract_data(api, items_name[0]))
    videoId = get_video_id(queries,YT_API_KEY)

    url = make_service()
    return url
