## Python scripts for managing SWITCHtube channels

### Installation

* Safe the file ```tus.py``` in the same directory as ```switch_list_channels.py``` and ```switch_upload.py```

* Requests is needed for the tools to work. It can be installed with\
```pip3 install requests```

* In order for the tools to work you need to create an access token on SWITCHtube. Add the token to all files except ```tus.py```.

### Usage

* Channels to which you can contribute to can then be listed with\
```python3 switch_list_channels.py```\
The first returned number in each entry is the ```CHANNEL_ID```.

* To upload a video use\
```python3 switch_upload_video.py -c CHANNEL_ID -v path_to_video_file -t "Title of the video"```

* To upload a video and set a poster/thumbnail use\
```python3 switch_upload_video.py -c CHANNEL_ID -p path_to_poster_file -v path_to_video_file -t "Title of the video"```

* To delete a video use\
```python3 switch_delete_video.py -c CHANNEL_ID -t "Title of the video"```

### Credits

The above code is based on the python [scripts provided by SWITCH](https://github.com/Fingertips/SwitchTube-examples#web-service-api)
