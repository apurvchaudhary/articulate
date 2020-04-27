def create_embed_link(link):
    YOUTUBE_URL = "https://www.youtube.com/embed/"
    try:
        youtube_normal_link = link.split("&")[0]
        hash = youtube_normal_link.split("=")[1]
        return YOUTUBE_URL + hash
    except IndexError:
        try:
            hash = link.split("/")[-1]
            return YOUTUBE_URL + hash
        except IndexError:
            return link
