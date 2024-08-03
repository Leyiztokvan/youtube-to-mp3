# YouTube to MP3 Converter

## Aim
Convert a list of YouTube video links to MP3 files.

## Project Overview
This project allows users to download audio from YouTube videos and convert them to MP3 files using Python. The project utilizes `yt_dlp` for downloading videos and `pydub` for audio conversion.

**Note**: You can use any virtual environment tools you prefer. The instructions below showcase the example of using Conda and Miniforge.
## Prerequisites
- A virtual environment for example [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- Required Packages : [ffmpeg](https://ffmpeg.org/download.html), yt_dlp, pydub

## Setup Instructions

### Create a Conda Environment

First, ensure you have Conda installed. If not, you can install it by following the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

Create a new Conda environment using Miniforge:

```bash
conda create -n youtube-to-mp3 python=3.10
conda activate youtube-to-mp3
```

**Note**: Specifing the python version is recomended but not required.

### Install Required Packages

Install the necessary packages from the conda-forge channel:

```bash
conda install -c conda-forge yt-dlp pydub ffmpeg
```

### Ensure ffmpeg is Installed

Make sure ffmpeg is installed and available in your PATH. You can download and install ffmpeg from [here](https://ffmpeg.org/download.html).

## Usage

Add the YouTube video URLs to the video_urls list in the script.py file.
Run the script to download and convert the videos to MP3 format.
The MP3 files will be saved in the mp3_files directory.

### Add YouTube Links

Add the YouTube video URLs to the video_urls list in the script.py file.
 ```python
video_urls = [
    #"https://www.youtube.com/watch?v=example1",
    #"https://www.youtube.com/watch?v=example2",
    # Add more URLs as needed
    #
]
```

### Run the Script

Save the file and run the script:
```bash
python script.py
```

## Notes and Best Practices

- Use a virtual environment to manage dependencies and avoid conflicts.
- Ensure that ffmpeg is correctly installed and accessible from the command line.
- The script is set to download the best audio format available and convert it to MP3 with a bitrate of 192 kbps.
- Adjust the ydl_opts dictionary in the script as needed to customize the download and conversion settings.
- Keep the video_urls list updated with the YouTube links you want to convert.

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENCE.md) file for details.



