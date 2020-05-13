import os
import sys

video_file = sys.argv[1]
output_file = "compressed_" + os.path.splitext(video_file)[0] + ".mp4"

codec_config = "-r 25 -s 1920x1080 -codec:v libx264 -crf 18 -bf 2 -flags +cgop -pix_fmt yuv420p -codec:a aac -strict -2 -b:a 384k -movflags faststart"
ffmpeg_command = "ffmpeg -i \"" + video_file + \
    "\" " + codec_config + " " + output_file

print("compressing: " + video_file)
os.system(ffmpeg_command)
