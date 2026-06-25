---
tags:
  - Free
catalog:
  name: FFmpeg
  description: Tools and libraries for recording, converting and streaming audio and video
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Roihu
---

# FFmpeg

[FFmpeg](https://ffmpeg.org/) is a cross-platform collection of libraries and
command-line tools for recording, converting, filtering and streaming audio and
video. It supports a wide range of codecs and container formats and is commonly
used for tasks such as transcoding media, extracting frames, and assembling
images into videos.

## Available

* Puhti: 4.4.1
* Roihu: 7.1

## License

FFmpeg is free software, licensed under the
[LGPL 2.1 or later](https://ffmpeg.org/legal.html); some optional components are
covered by the GPL.

## Usage

Initialize FFmpeg with:

```bash
module load ffmpeg
```

The main command-line tool is `ffmpeg`. For example, to convert a video file to
another format:

```bash
ffmpeg -i input.mov output.mp4
```

You can check the version and the available encoders, decoders and filters with:

```bash
ffmpeg -version
ffmpeg -encoders
ffmpeg -filters
```

## More information

* [FFmpeg home page](https://ffmpeg.org/)
* [FFmpeg documentation](https://ffmpeg.org/documentation.html)
