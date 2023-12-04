
import argparse
import pathlib
import requests
import tus

TOKEN='REPLACE_WITH_PERSONAL_TOKEN_STRING'
ORIGIN = 'https://tube.switch.ch'
RETRIES = 10
CHUNK_SIZE = 52428800 # 50 megabytes

headers = {'Authorization': 'Token ' + TOKEN}

def upload_file(path):
    with open(path, 'rb') as fd:
        upload_url = tus.create(
            ORIGIN + '/files',
            path.name,
            path.stat().st_size,
            headers=headers
        )
        # Uploading a segment may fail so we retry up-to 10 times for every upload.
        for i in range(0, RETRIES):
            try:
                tus.resume(fd, upload_url, chunk_size=CHUNK_SIZE, headers=headers)
            except tus.TusError:
                continue
            break
    return(upload_url.split('/')[-1])

# Create a new video with the uploaded file.
def create_video(upload_id):
    response = requests.post(
        ORIGIN + '/api/v1/videos',
        headers=headers,
        json={
            'channel_id': arguments.channel,
            'upload_id': upload_id,
            'title': arguments.title,
            'published': True
            }
        )
    # Stop and show a message when the response has an error status code.
    response.raise_for_status()
    # Show the URL of the new video.
    video_url=ORIGIN + response.json()['path']
    video_id=response.json()['id']
    print(video_url)
    return(video_id)

def add_poster(video_id,poster_upload_id):
    response = requests.post(
        ORIGIN + '/api/v1/posters',
        headers=headers,
        json={
            'video_id': video_id,
            'upload_id': poster_upload_id
            }
        )
    response.raise_for_status()
    poster_id=response.json()['id']
    return(poster_id)

def select_poster(video_id,poster_id):
    response = requests.patch(
        ORIGIN + '/api/v1/videos/'+str(video_id),
        headers=headers,
        json={
            'poster_id': poster_id
            }
        )

if __name__ == '__main__':
# Define and parse command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('--channel', '-c', help='id of the channel')
    parser.add_argument('--video', '-v', type=pathlib.Path, help='video file to upload')
    parser.add_argument('--poster', '-p', type=pathlib.Path, help='video file to upload')
    parser.add_argument('--title', '-t', help='id of the channel')
    parser.add_argument('--info', '-i', help="output csv info line", action='store_true')

    arguments = parser.parse_args()

    video_upload_id=upload_file(arguments.video)
    video_id=create_video(video_upload_id)
    if arguments.poster:
        poster_upload_id=upload_file(arguments.poster)
        poster_id=add_poster(video_id,poster_upload_id)
        select_poster(video_id,poster_id)
    