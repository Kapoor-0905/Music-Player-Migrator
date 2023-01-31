 api = connect(SP_CLIENT_ID, SP_CLIENT_SECRET)
    items_name = fetch_playlist_using_id(api, plId)
    name = items_name[1]
    queries = query_builder(extract_data(api, items_name[0]))
    videoId = get_video_id(queries,YT_API_KEY)

    service = make_service()