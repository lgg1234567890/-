import cv2


def convert_to_black_and_white(input_video_path, output_video_path):
    # 打开输入视频
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error: Could not open input video.")
        return

    # 获取视频的属性
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 定义输出视频的编码器和文件
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 使用 XVID 编码器
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_height, frame_width), isColor=False)

    if not out.isOpened():
        print("Error: Could not create output video file.")
        cap.release()
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 将 BGR 转换为灰度图像
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 旋转帧90度
        rotated_frame = cv2.rotate(gray_frame, cv2.ROTATE_90_CLOCKWISE)

        # 写入输出视频
        out.write(rotated_frame)

        frame_count += 1
        if frame_count % 100 == 0:
            print(f"Processed {frame_count} frames.")

    # 释放资源
    cap.release()
    out.release()
    print("Conversion complete.")

# 示例调用
input_video_path = 'D:/dateset/1.mp4'  # 输入视频路径
output_video_path = 'D:/dateset/output_video_gray.avi'  # 输出视频路径
convert_to_black_and_white(input_video_path, output_video_path)
