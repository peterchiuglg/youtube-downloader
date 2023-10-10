import argparse
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def convert_youtube_to_mp3(url, output_filename=None):
    # Download video from youtube
    yt = YouTube(url)
    if output_filename is None:
        output_filename = yt.title
    video = yt.streams.filter(progressive=True, file_extension='mp4').first()
    video.download(filename='temp.mp4')

    # Convert mp4 file to mp3
    clip = AudioFileClip('temp.mp4')
    clip.write_audiofile(f'{output_filename}.mp3') # changed line
    os.remove('temp.mp4')  # remove temp file

    print(f'Successfully converted {url} to {output_filename}.mp3')

def main():
    parser = argparse.ArgumentParser(description='Convert a YouTube video to an MP3 file.')
    parser.add_argument('url', type=str, help='The URL of the YouTube video.')
    parser.add_argument('--output', type=str, default=None, help='The output filename (optional).')

    args = parser.parse_args()
    convert_youtube_to_mp3(args.url, args.output)

if __name__ == '__main__':
    main()