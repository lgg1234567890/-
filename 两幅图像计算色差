import cv2
import numpy as np
import matplotlib.pyplot as plt


def calculate_delta_e(image1, image2):
    """
    计算两幅图像之间的色差（ΔE）。
    :param image1: 第一幅图像的路径或图像数组
    :param image2: 第二幅图像的路径或图像数组
    :return: 两幅图像之间的平均色差（ΔE）
    """
    # 如果输入是路径，则读取图像
    if isinstance(image1, str):
        image1 = cv2.imread(image1)
        if image1 is None:
            raise ValueError(f"无法读取图像: {image1}")
        # 将BGR转换为RGB
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    if isinstance(image2, str):
        image2 = cv2.imread(image2)
        if image2 is None:
            raise ValueError(f"无法读取图像: {image2}")
        # 将BGR转换为RGB
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

    # 确保两幅图像大小相同
    if image1.shape != image2.shape:
        raise ValueError("两幅图像的大小必须相同")

    # 将图像从RGB转换为LAB颜色空间
    lab_image1 = cv2.cvtColor(image1, cv2.COLOR_RGB2LAB)
    lab_image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2LAB)

    # 计算每对像素之间的色差
    delta_e = np.sqrt((lab_image1[:, :, 0] - lab_image2[:, :, 0]) ** 2 +
                      (lab_image1[:, :, 1] - lab_image2[:, :, 1]) ** 2 +
                      (lab_image1[:, :, 2] - lab_image2[:, :, 2]) ** 2)

    # 计算平均色差
    average_delta_e = np.mean(delta_e)

    return average_delta_e, image1, image2


def display_images_with_delta_e(image1_path, image2_path):
    """
    显示两幅图像，并在下方显示色差（ΔE）。
    :param image1_path: 第一幅图像的路径
    :param image2_path: 第二幅图像的路径
    """
    # 计算色差
    average_delta_e, image1, image2 = calculate_delta_e(image1_path, image2_path)

    # 创建一个图形和两个子图
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # 显示第一幅图像
    axes[0].imshow(image1)
    axes[0].set_title('Image 1')
    axes[0].axis('off')

    # 显示第二幅图像
    axes[1].imshow(image2)
    axes[1].set_title('Image 2')
    axes[1].axis('off')

    # 在图像下方显示色差
    fig.text(0.5, 0.01, f'Average Color Difference (ΔE): {average_delta_e:.2f}', ha='center', fontsize=30, color='red')

    # 显示图形
    plt.show()


# 示例调用
image1_path = 'D:/dateset/1.jpg'  # 第一幅图像路径
image2_path = 'D:/dateset/1_processed.jpg'  # 第二幅图像路径

# 显示图像并显示色差
display_images_with_delta_e(image1_path, image2_path)
