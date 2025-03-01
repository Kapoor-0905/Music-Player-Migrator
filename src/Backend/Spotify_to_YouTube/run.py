from auth.credentials import *

from extract import *
from connect import *
from search_in_yt import *
from add_to_playlist import *

# playlist_link = "https://open.spotify.com/playlist/1agMj2TVZcnB8jxVhQL8KW?si=9ff63f14847b487a"
# playlist_URI = playlist_link.split("/")[-1].split("?")[0]

def main(url):
    plId = url.split("/")[-1].split("?")[0]
    api = connect(SP_CLIENT_ID, SP_CLIENT_SECRET)
    items_name = fetch_playlist_using_id(api, plId)
    name = items_name[1]
    queries = query_builder(extract_data(api, items_name[0]))
    videoId = get_video_id(queries,YT_API_KEY)

    service = make_service()
    new_play_id = make_playlist(service,name)
    add_to_playlist(service,new_play_id,videoId)
    print("finished migrating")

    return new_play_id
