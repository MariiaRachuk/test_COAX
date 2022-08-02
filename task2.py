import requests
from moviepy.editor import VideoFileClip

num_tt_video = 0


def gif_converting(url: str, ):
    global num_tt_video
    num_tt_video += 1

    name_tt_video = 'Tiktok_video.mp4'
    name_tt_gif = 'TikTok-example-' + str(num_tt_video) + '.gif'

    r = requests.get(url, stream=True)

    with open(name_tt_video, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    video_clip = VideoFileClip(name_tt_video)
    video_clip.write_gif(name_tt_gif)

    return name_tt_gif


gif_converting("https://v16-webapp.tiktok.com/297843f67801aa73bbbcd89cfd0d1824/62e93344/video/tos/useast2a/tos-useast2a-ve-0068c004/776739df67d34feab16dd84d7f8ad9b1/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4448&bt=2224&btag=80000&cs=0&ds=3&ft=ar5S8qT2mo0PDSeW_uaQ9gi1~ObpkV1PC6&mime_type=video_mp4&qs=0&rc=Nzc6OWdoOTlkaDQzZjtpaEBpM3c6eDs6Zmd2ZTMzNzczM0A0X18xM181XmExYmE2YWFgYSNrXi5ycjQwYS1gLS1kMTZzcw%3D%3D&l=202208020822220102170290421303D851")

