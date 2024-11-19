import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path) #creates video capture object
    frames = []
    while True:
        ret, frame = cap.read() #cap.read() returns two values: ret, a boolean that indicates whether reading was successful, and frame, which is the current frame image. 
        if not ret: #if read is false the loop breaks indicating there is empty frame
            break
        frames.append(frame) #then frames are appended here
    cap.release() #releases the video file
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #fourcc is a 4-byte code used to specify the video codec
    out = cv2.VideoWriter(output_video_path, fourcc, 24.0, (output_video_frames[0].shape[1], output_video_frames[0].shape[0])) #creates a video writer object
    for frame in output_video_frames:
        out.write(frame) #writes the frames to the video file
    out.release() #releases the video file