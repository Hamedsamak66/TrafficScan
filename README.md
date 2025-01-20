# TrafficScan

TrafficScan is a Python-based project that uses the YOLO (You Only Look Once) object detection model to identify and track specific vehicle types (cars, trucks, and motorbikes) in video footage. The project processes an input video and generates an annotated output video highlighting the detected objects.

## Features

- Detects and tracks vehicles including cars, trucks, and motorbikes.
- Annotates the detected objects with bounding boxes and confidence scores.
- Supports input and output video processing.
- Configurable confidence and Intersection over Union (IoU) thresholds.

## Requirements

- Python 3.8 or later
- OpenCV
- Ultralytics YOLO

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hamedsamak66/TrafficScan.git
   cd TrafficScan
   ```


## Usage

1. Place the input video file in the project directory and update the `VIDEO_PATH` variable in the script with its filename.

2. Update the `OUTPUT_VIDEO_PATH` variable to specify the name of the processed output video.

3. Run the script:
   ```bash
   python main.py
   ```

4. The processed video will be saved at the specified `OUTPUT_VIDEO_PATH`.

## Script Details

The main script performs the following tasks:

1. Loads the YOLO model.
2. Opens the input video and reads its frames.
3. Applies the YOLO model to each frame to detect objects.
4. Annotates the frame with bounding boxes, class names, and confidence scores for the specified target classes (car, truck, motorbike).
5. Writes the annotated frames to the output video.

## Configuration

- **`VIDEO_PATH`**: Path to the input video file.
- **`OUTPUT_VIDEO_PATH`**: Path to save the annotated output video.
- **`target_classes`**: Set of vehicle classes to detect (default: `{'car', 'truck', 'motorbike'}`).
- **Confidence Threshold**: Adjust the `conf` parameter in the `model()` call to filter detections based on confidence level.
- **IoU Threshold**: Adjust the `iou` parameter in the `model()` call to control overlap between bounding boxes.

## Example

Input video: `148317-793718152_small.mp4`  
Output video: `output_video.mp4`

The script will detect vehicles such as cars, trucks, and motorbikes in the input video and save the annotated video as `output_video.mp4`.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

## Contact

For questions or support, feel free to reach out at samak.h@outlook.com.
