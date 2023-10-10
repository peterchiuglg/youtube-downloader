import sys
from pytube import YouTube

def download_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video
        video = yt.streams.get_highest_resolution()

        # Download the video
        video.download()

        print("Video downloaded successfully")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a YouTube URL as an argument.")
    else:
        url = sys.argv[1]
        download_video(url)