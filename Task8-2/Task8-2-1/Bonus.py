import numpy as np
import cv2

def block_matching(left_image, right_image, block_size, disparity_range):
    height, width = left_image.shape[:2]
    disparity_map = np.zeros_like(left_image, dtype=np.float32)

    half_block_size = block_size // 2

    for y in range(half_block_size, height - half_block_size):
        for x in range(half_block_size, width - half_block_size):
            min_ssd = float('inf')
            best_disparity = 0

            for disparity in range(disparity_range):
                ssd = np.sum((left_image[y - half_block_size:y + half_block_size + 1,
                                        x - half_block_size:x + half_block_size + 1] -
                              right_image[y - half_block_size:y + half_block_size + 1,
                                         x - half_block_size - disparity:x + half_block_size + 1 - disparity]) ** 2)

                if ssd < min_ssd:
                    min_ssd = ssd
                    best_disparity = disparity

            disparity_map[y, x] = best_disparity

    return disparity_map

left_image = cv2.imread('left_image.png', cv2.IMREAD_GRAYSCALE)
right_image = cv2.imread('right_image.png', cv2.IMREAD_GRAYSCALE)

left_image = cv2.GaussianBlur(left_image, (5, 5), 0)
right_image = cv2.GaussianBlur(right_image, (5, 5), 0)

block_size = 9
disparity_range = 64

disparity_map = block_matching(left_image, right_image, block_size, disparity_range)

disparity_map_normalized = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('Disparity Map', disparity_map_normalized)
cv2.waitKey(0)
cv2.imwrite('depth_map.png', disparity_map_normalized)