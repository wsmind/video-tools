import os
import sys

video_files = sys.argv[1:]
output_file = "concat_" + video_files[0]

with open("temp_file_list.txt", "wt") as f:
    for input_file in video_files:
        f.write("file '" + input_file + "'\n")

ffmpeg_command = "ffmpeg -f concat -safe 0 -i \"temp_file_list.txt\" -c copy " + output_file

print("concatenating: " + str(video_files))
os.system(ffmpeg_command)
