import os

def line_separator():
    print("----------------------------------------------------------------------------------------------------------------------")

# Define the files in the current directory.
current_dir_files = os.listdir()

# Define the compatible filetypes.
compatible_filetypes = ["mp4", "mkv"]

compatible_file_list = [filename for filename in current_dir_files if filename.split(".")[-1] in compatible_filetypes]
num_compatible_files = len(compatible_file_list)

# List the compatible video files in the current directory.
if num_compatible_files >= 1:
    print("You have {} compatible video file(s) in the current directory. They are: ".format(num_compatible_files))
    print("\n")
    for i in range(len(compatible_file_list)):
        print("{}. {} ".format(i+1, compatible_file_list[i]))

    line_separator()
    # Prompt the user to select a video.
    video_file = input("To select a video, please enter its associated number (e.g. '1') then press enter: ")

# Set the index of the chosen file.
video_file_index = int(video_file)

# Find the selected file in compatible_files_list by using its index.
video_file = compatible_file_list[video_file_index - 1]

print("You have selected: {}".format(video_file))
line_separator()

output_name = input("What would you like the output file to be named? ")
line_separator()

print("What would you like the audio codec to be? You can choose from one of the following:")

# Define the choice of audio ffmpeg_parameters.
codec_options = ["MP3", "AAC (FFMpeg's native encoder)", "Nero AAC", "FLAC", "ALAC", "Vorbis", "Opus"]

for codec_number, codec in enumerate(codec_options, 1):
    print("{}. {}".format(codec_number, codec))

line_separator()
# Prompt the user to select an audio codec.
chosen_codec = input("To select your desired codec, please enter its associated number (e.g. '1') then press enter: ")

chosen_codec_index = int(chosen_codec)
chosen_codec = codec_options[chosen_codec_index - 1]

# Create a dictionary for the FFmpeg parameters associated with some of the codecs, to reduce code repetition.
ffmpeg_parameters = {
    "AAC (FFmpeg's native AAC encoder)": ["aac", "-q:a 2", "m4a"],
    "MP3": ["libmp3lame", "-qscale:a 0", "mp3"], 
    "FLAC": ["flac", "", "flac"],
    "ALAC": ["alac", "", "m4a"], 
    "Vorbis": ["libvorbis", "-qscale:a 10", "ogg"] 
}

if chosen_codec == "Opus":
    line_separator()
    target_bitrate = input("Please specify a target bitrate in kilobits per second (kbps). 512 is the maximum. Please enter an integer: ")
    os.system('ffmpeg -i "{}" -vn -c:a libopus -b:a {}k {}.opus'.format(video_file, target_bitrate, output_name))
    print("Success! File saved as {}.opus".format(output_name))

elif chosen_codec == "WAV":
    os.system('ffmpeg -i "{}" -vn "{}".wav'.format(video_file, output_name))

elif chosen_codec == "Nero AAC":
    os.system('ffmpeg -i "{}" -vn -f wav - | neroAacEnc -q 1 -if - -ignorelength -of "{}".m4a'.format(video_file, output_name))
    print("Success! File saved as {}.m4a".format(output_name))

elif chosen_codec in ffmpeg_parameters.keys():
    codec_specifier, codec_options, extension = ffmpeg_parameters[chosen_codec]
    print("Converting...")
    os.system('ffmpeg -i "{}" -vn -c:a {} {} "{}".{}'.format(video_file, codec_specifier, codec_options,  output_name, extension))
    print("Success! File saved as {}.{}".format(output_name, extension))

prevent_window_from_closing = input("You may now close this window.")
