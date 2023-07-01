import argparse
import subprocess
import moviepy.editor as mp

def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('url', help='youtube URL', nargs='?')
    p.add_argument('-ss', '--seek', help='position in time to start at', default='00:00:00')
    p.add_argument('-t', '--time', help='time of clip/duration', default='00:00:01')
    p.add_argument('-o', '--output', help='full or relative path for output file', default='output.mp4')
    return p

# Function to crop MP3 file given start and end time
def crop_audio_file(input_file, output_file):
    # Load the audio file using MoviePy
    audio = mp.AudioFileClip(input_file)

    # Export the cropped audio as an MP3 file
    audio.write_audiofile(output_file)

    # Delete the original file
    audio.reader.close_proc()

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    # Setup command for youtube-dl
    yt_dl_cmd = ['yt-dlp', '--youtube-skip-dash-manifest', '-g', args.url]
    # Run youtube-dl command
    result = subprocess.run(yt_dl_cmd, stdout=subprocess.PIPE, universal_newlines=True)
    # Split resultant URLs on new lines
    results = result.stdout.splitlines()

  # FFmpeg options for mapping audio and video
    ff_options = '-map 0:v -map 1:a -c:v libx264 -c:a aac'
    # Assemble full command
    ff_cmd = 'ffmpeg -y -ss {} -i "{}" -ss {} -i "{}" -t {} {} {}'.format(args.seek, results[0], args.seek, results[1], args.time, ff_options, args.output)
    # Run FFmpeg command
    subprocess.call(ff_cmd, shell=True)


    # Example usage
#    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
#    start_time = 10 * 1000 # Start time in milliseconds
#    end_time = 20 * 1000 # End time in milliseconds
    input_file = "output.mp4"
    output_file = "output.mp3"

    # Convert the MP4 file to an MP3 file
    video = mp.VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)

    # Crop the MP3 file
    crop_audio_file(output_file, output_file)
