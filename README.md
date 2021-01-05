### Main monitor
ffmpeg -f gdigrab -framerate 30 -video_size 1920x1080 -show_region 1 -i desktop output.mkv

### Left monitor from the main
ffmpeg -f gdigrab -framerate 30 -offset_x -1920 -offset_y 0 -video_size 1920x1080 -show_region 1 -i desktop output.mkv

### Right monitor from the main
ffmpeg -f gdigrab -framerate 30 -offset_x 1920 -offset_y 0 -video_size 1920x1080 -show_region 1 -i desktop output.mkv

### Capture a particular application
ffmpeg -f gdigrab -framerate 30 -i title=clipit o.mkv