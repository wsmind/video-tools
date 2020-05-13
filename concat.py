import os
import sys

video_files = sys.argv[1:]
output_file = "concat_" + video_files[0]

codec_config = "-codec:v libx264 -crf 18 -bf 2 -flags +cgop -pix_fmt yuv420p -codec:a aac -strict -2 -b:a 384k -movflags faststart"

ffmpeg_command = "ffmpeg -i \"concat:" + \
    "|".join(video_files) + "\" " + codec_config + " " + output_file

print("processing: " + str(video_files))
os.system(ffmpeg_command)
