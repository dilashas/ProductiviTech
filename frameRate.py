import cv2

video = cv2.VideoCapture("SampleZoom.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
per_frame_duration = 1 / fps

frames = input("Enter the frames, separated by space if more than one : ")
frames_list = [int(i) for i in frames.split(" ")]

start = frames_list[0] * per_frame_duration
end = frames_list[len(frames_list) - 1] * per_frame_duration

print(f"The fps of the video = {fps}")
print(f"Total frames in the video = {total_frames}")
print(f"Time taken by each frame = {per_frame_duration}s")
print(f"Person Distracted form {start:.2f}s to {end:.2f}s")
video.release()
