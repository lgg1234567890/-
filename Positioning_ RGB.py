# D:/dateset/1.jpg
import cv2
import numpy as np
import matplotlib.pyplot as plt


def modify_hsv_channels(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("无法读取图像，请检查图像路径。")
        return

    # 将 BGR 图像转换为 RGB 图像
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 2, 1)
    plt.imshow(rgb_image)
    plt.title('Original RGB Image')
    plt.axis('off')

    # 将 RGB 图像转换为 HSV 图像
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # 分离 HSV 通道
    h, s, v = cv2.split(hsv_image)

    # 示例修改：增加饱和度 20%，增加明度 10%
    s = np.clip(s * 1.2, 0, 255).astype(np.uint8)
    v = np.clip(v * 1.1, 0, 255).astype(np.uint8)

    # 合并修改后的 HSV 通道
    modified_hsv = cv2.merge([h, s, v])

    # 将修改后的 HSV 图像转换回 RGB 图像
    modified_rgb = cv2.cvtColor(modified_hsv, cv2.COLOR_HSV2RGB)

    return modified_rgb


if __name__ == "__main__":
    # 请将此处替换为你的图像文件路径
    image_path = 'D:/dateset/1.jpg'
    result = modify_hsv_channels(image_path)


    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.title('HSV Image(s+20%,v+10%)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# import cv2
# import matplotlib.pyplot as plt
#
#
# def display_rgb_channels(image_path):
#     image = cv2.imread(image_path)
#     if image is None:
#         print("无法读取图像，请检查路径。")
#         return
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV 读取为 BGR，转换为 RGB
#
#     # 分离通道
#     r, g, b = cv2.split(image)
#
#     # 创建彩色通道图（每个通道单独显示为对应颜色）
#     r_color = cv2.merge([r, g * 0, b*0])  # 红色通道：R=原图R，G=0，B=0
#     g_color = cv2.merge([r * 0, g, b * 0])  # 绿色通道：G=原图G，R=0，B=0
#     b_color = cv2.merge([r*0, g * 0, b])  # 蓝色通道：B=原图B，R=0，G=0
#
#     # 显示原始图像和彩色通道图
#     plt.figure(figsize=(12, 8))
#
#     plt.subplot(2, 2, 1)
#     plt.imshow(image)
#     plt.title('Original Image')
#     plt.axis('off')
#
#     plt.subplot(2, 2, 2)
#     plt.imshow(r_color)
#     plt.title('Red Channel (Colored)')
#     plt.axis('off')
#
#     plt.subplot(2, 2, 3)
#     plt.imshow(g_color)
#     plt.title('Green Channel (Colored)')
#     plt.axis('off')
#
#     plt.subplot(2, 2, 4)
#     plt.imshow(b_color)
#     plt.title('Blue Channel (Colored)')
#     plt.axis('off')
#
#     plt.tight_layout()
#     plt.show()
#
#
# if __name__ == "__main__":
#     image_path = 'D:/dateset/1.jpg'
#     display_rgb_channels(image_path)
#
#
# def display_rgb_channels(image_path):
#     try:
#         # 读取图像
#         image = cv2.imread(image_path)
#         if image is None:
#             print("无法读取图像，请检查图像路径。")
#             return
#
#         # 将 BGR 转换为 RGB
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#         # 分离 RGB 通道
#         r_channel = image[:, :, 0]
#         g_channel = image[:, :, 1]
#         b_channel = image[:, :, 2]
#
#         # 创建一个包含 4 个子图的画布
#         fig, axes = plt.subplots(2, 2, figsize=(10, 10))
#
#         # 显示原始图像
#         axes[0, 0].imshow(image)
#         axes[0, 0].set_title('Original Image')
#         axes[0, 0].axis('off')
#
#         # 显示红色通道
#         axes[0, 1].imshow(r_channel, cmap='gray')
#         axes[0, 1].set_title('Red Channel')
#         axes[0, 1].axis('off')
#
#         # 显示绿色通道
#         axes[1, 0].imshow(g_channel, cmap='gray')
#         axes[1, 0].set_title('Green Channel')
#         axes[1, 0].axis('off')
#
#         # 显示蓝色通道
#         axes[1, 1].imshow(b_channel, cmap='gray')
#         axes[1, 1].set_title('Blue Channel')
#         axes[1, 1].axis('off')
#
#         # 调整子图布局
#         plt.tight_layout()
#         plt.show()
#
#     except Exception as e:
#         print(f"发生错误: {e}")
#
#
# if __name__ == "__main__":
#     # 请将此处替换为你的图像文件路径
#     image_path = 'D:/dateset/1.jpg'
#     display_rgb_channels(image_path)

#
#
# def mouse_callback(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         img = param
#         b, g, r = img[y, x]
#         text = f"POS:({x}, {y}) RGB: ({r}, {g}, {b})"
#         cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
#         cv2.imshow('Image', img)
#
#
# if __name__ == "__main__":
#     # 请将此处替换为你的图像文件路径
#     image_path = 'D:/dateset/1.jpg'
#     img = cv2.imread(image_path)
#     if img is None:
#         print("无法读取图像，请检查图像路径是否正确。")
#     else:
#         cv2.namedWindow('Image')
#         cv2.setMouseCallback('Image', mouse_callback, img)
#
#         while True:
#             cv2.imshow('Image', img)
#             # 按 'q' 键退出
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#
#         cv2.destroyAllWindows()
