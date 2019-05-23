# Extract Audio From Video
***FFmpeg is a prerequisite. Please download and install. https://www.ffmpeg.org/download.html***

***The program (extract-audio.py) and the video file must be in the same directory, as well as the Nero AAC encoder if you wish to use it.

***Nero AAC is only compatible with Windows or Linux***

This program allows you to extract the audio from a video and save it as an audio file. You are also able to choose the output audio codec. Options:
- AAC (.m4a extension, .aac results in no seekbar when playing the audio in foobar2000).
- Nero AAC (.m4a)
- MP3 (.mp3)
- FLAC (.flac) lossless compression, no quality loss.
- ALAC (.m4a) lossless compression, no quality loss.
- Vorbis (.ogg)
- Opus (.opus)

# Notes:
- Selecting MP3 means that if the original audio contains more than 2 channels (e.g DTS HD, Dolby Digital), the audio will be downmixed to stereo.
- FLAC or ALAC results in zero quality loss. The downside is larger file size.
- If unsure as to which codec to choose, select MP3 or AAC as they are most widely supported by players.
