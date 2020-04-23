def create_embed_link(link):
    try:
        youtube_normal_link = link.split("&")[0]
        hash = youtube_normal_link.split("=")[1]
        youtube_embed_url = "https://www.youtube.com/embed/" + hash
        embed_link = youtube_embed_url
        return embed_link
    except IndexError:
        return link
