import cv2
from ultralytics import YOLO

# Path to the input video file
VIDEO_PATH = '148317-793718152_small.mp4'

# Path to the output video file
OUTPUT_VIDEO_PATH = 'output_video.mp4'

# Load the YOLO model
model = YOLO('yolov8x.pt')

# Open the input video
video_capture = cv2.VideoCapture(VIDEO_PATH)

# Get video specifications
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for saving the video

# Define the output video
output_video = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (frame_width, frame_height))

# Target classes for detection
target_classes = {'car', 'truck', 'motorbike'}

# Process the frames
while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:  # Check for the end of the video
        break

    # Apply the model to each frame
    # results = model(frame, conf=0.3, iou=0.5, device='cuda')  # Use GPU
    results = model(frame, conf=0.08, iou=0.5, device='cpu')  # Switch to CPU

    # Copy the frame to draw the results
    frame_copy = frame.copy()

    # Process the results
    for obj in results[0].boxes:
        box = obj.xyxy.cpu().numpy()[0]  # Extract bounding box coordinates
        if len(box) == 4:
            x1, y1, x2, y2 = map(int, box)

            # Get class name and confidence
            confidence = float(obj.conf)
            class_name = model.names[int(obj.cls)]

            # Check if the class is in the target classes
            if class_name in target_classes:
                # Draw the bounding box and write the class name
                cv2.rectangle(frame_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
                text = f"{class_name} ({confidence:.2f})"
                cv2.putText(frame_copy, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the processed frame to the output file
    output_video.write(frame_copy)

# Release resources
video_capture.release()
output_video.release()

print(f"Output video saved at {OUTPUT_VIDEO_PATH}")