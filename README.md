# Extract Audio From Video
***FFmpeg is a prerequisite. Please download and install. https://www.ffmpeg.org/download.html***

**The program (extract-audio.py) and the video file must be in the same directory, as well as the Nero AAC encoder if you wish to use it.**

**Nero AAC is only compatible with Windows or Linux**

This program allows you to extract the audio from a video and save it as an audio file. You are also able to choose the output audio codec. Options:
- MP3 (.mp3) - LAME VBR V0.
- FFmpeg's native AAC encoder (file extension will be .m4a)
- Nero AAC (.m4a)
- WAV (.wav) - lossless file, but pointless if the orignal audio file is not lossless, unless you need/want a .wav file. Largest file size.
- FLAC (.flac) - lossless file, no quality loss.
- ALAC (.m4a) - lossless file, no quality loss.
- Vorbis (.ogg)
- Opus (.opus)

# Notes:
- Selecting MP3 means that if the original audio contains more than 2 channels (e.g DTS HD, Dolby Digital), the audio will be downmixed to stereo.
- If unsure as to which codec to choose, select Nero AAC (if on Windows or Linux), FFmpeg's native AAC encoder or MP3 as they are most widely supported by players. With regards to the quality of these three, it is probably as follows: Nero AAC > MP3 > FFmpeg's native AAC encoder.
