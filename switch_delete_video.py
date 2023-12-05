import argparse
import requests

TOKEN='REPLACE_WITH_PERSONAL_TOKEN_STRING'
ORIGIN = 'https://tube.switch.ch'

headers = {'Authorization': 'Token ' + TOKEN}

def return_video_id_by_title(channel_id,video_title):
    response = requests.get(
        ORIGIN + '/api/v1/channels/'+str(channel_id)+'/videos',
        headers=headers,
        )
    response.raise_for_status()
    videos=response.json()
    for dictionary in videos:
        if video_title in str(dictionary):
            return(int(dictionary['id']))

def delete_video(video_id):
    response = requests.delete(
        ORIGIN + '/api/v1/videos/'+str(video_id),
        headers=headers,
        )
    response.raise_for_status()


if __name__ == '__main__':
# Define and parse command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('--channel', '-c', help='id of the channel')
    parser.add_argument('--title', '-t', help='Title of the video')
    args = parser.parse_args()

    
    video_id=return_video_id_by_title(str(args.channel),str(args.title))
    delete_video(video_id)

