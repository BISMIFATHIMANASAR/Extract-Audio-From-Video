import os

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

    print("\n")
    # Prompt the user to select a video.
    video_file = input("To select a video, please enter its associated number (e.g. '1') then press enter: ")

# Set the index of the chosen file.
video_file_index = int(video_file)

# Find the selected file in compatible_files_list by using its index.
video_file = compatible_file_list[video_file_index - 1]

print("You have selected: {}".format(video_file))

print("\n")
print("What would you like the audio codec to be? You can choose from one of the following ffmpeg_parameters:")
print("\n")

# Define the choice of audio ffmpeg_parameters.
codec_options = ["MP3", "AAC", "FLAC", "ALAC", "Vorbis"]

for codec_number, codec in enumerate(codec_options, 1):
    print("{}. {}".format(codec_number, codec))

print("\n")
print("NOTES:")
print("- Choose FLAC or ALAC for zero quality loss. The downside is larger file size.")
print("- If unsure as to which codec to choose, select MP3 or AAC as they are the most widely supported ffmpeg_parameters by players.")
print("- Selecting MP3 means that if the original audio contains more than 2 channels (e.g DTS HD, Dolby Digital), the audio will be downmixed to stereo.")
print("\n")

# Prompt the user to select an audio codec.
chosen_codec = input("To select your desired codec, please enter its associated number (e.g. '1') then press enter: ")

chosen_codec_index = int(chosen_codec)
chosen_codec = codec_options[chosen_codec_index - 1]

output_name = input("What would you like the audio to be named? ")

# Create a dictionary for the FFmpeg parameters associated with each codec.
ffmpeg_parameters = {
    "AAC": ["aac", "-q:a 2", "m4a"], # "-q:a 2" = highest VBR quality setting for FFmpeg's native AAC encoder.
    "MP3": ["libmp3lame", "-qscale:a 0", "mp3"], # "-qscale:a 0" = VBR V0 (highest quality LAME VBR setting).
    "FLAC": ["flac", "", "flac"],
    "ALAC": ["alac", "", "m4a"], 
    "Vorbis": ["libvorbis", "-qscale:a 10", "ogg"] # "-qscale:a 10" = highest VBR quality setting for libvorbis.
}

if chosen_codec in ffmpeg_parameters.keys():
    codec_specifier, codec_options, extension = ffmpeg_parameters[chosen_codec]

    print("Extracting audio and converting to your desired codec...")
    os.system('ffmpeg -loglevel 16 -i "{}" -vn -c:a {} {} {}.{}'.format(video_file, codec_specifier, codec_options,  output_name, extension))
    print("Success! Audio saved as {}.{}".format(output_name, extension))

else:
    print("You did not enter a valid number. Please restart this program.")

prevent_window_from_closing = input("You may now close this window.")