import cv2
import numpy as np
import matplotlib.pyplot as plt


def detect_stop_sign(image_path):
    # 1. 读取图像并转换到HSV颜色空间
    image = cv2.imread(image_path)
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Original Stop Sign')
    plt.axis('off')

    if image is None:
        print("错误：图像未找到！")
        return
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 2. 定义红色背景的HSV范围
    lower_red1 = np.array([0, 100, 100])  # 低H值红色范围
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])  # 高H值红色范围
    upper_red2 = np.array([180, 255, 255])

    # 创建红色掩膜
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # 3. 形态学操作优化掩膜
    kernel = np.ones((5, 5), np.uint8)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)  # 填充空洞
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)  # 去除噪声

    # 4. 查找轮廓并过滤
    contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_area = 1000  # 最小区域阈值
    stop_sign_detected = False

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < min_area:
            continue

        # 5. 形状检测：近似为八边形
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)

        if len(approx) == 8:  # 八边形顶点数为8
            # 6. 检测内部白色区域（模拟STOP文字）
            # 提取红色区域内的图像
            x, y, w, h = cv2.boundingRect(cnt)
            roi = image[y:y + h, x:x + w]

            # 检测白色（高亮度区域）
            hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            lower_white = np.array([0, 0, 200])  # 低饱和度、高亮度
            upper_white = np.array([180, 50, 255])
            mask_white = cv2.inRange(hsv_roi, lower_white, upper_white)

            # 判断白色区域占比（粗略模拟文字存在）
            white_ratio = cv2.countNonZero(mask_white) / (w * h)
            if white_ratio > 0.1:  # 假设白色区域占比超过10%
                # 绘制八边形轮廓和文本
                cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)
                cv2.putText(image, "The STOP Sign Detected", (x-10, y + h +10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 8)
                # cv2.putText(image, "Alert: You can park here!", (x, y + h + 30),
                #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                stop_sign_detected = True

    # 7. 显示结果
    if stop_sign_detected:
        plt.subplot(1, 2, 2)
        plt.imshow(image)
        plt.title('Note: you can stop here for free')
        plt.axis('off')

        plt.tight_layout()
        plt.show()

        # cv2.imshow("Stop Sign Detection", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        print("提醒：检测到停车标志，此处可以停车！")
    else:
        print("未检测到有效的停车标志。")


# 使用示例
detect_stop_sign("D:/dateset/3.jpg")  # 替换为实际图像路径
