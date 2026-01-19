import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

# 0. Load Original Image (Grayscale)
img = cv2.imread('corruptedimg.jpg', 0) / 255.0

# 1. Simulate Motion Blur (Kernel 1xN) - Question 1
def get_motion_kernel(shape, size=20):
    kernel = np.zeros(shape)
    center_row = shape[0] // 2
    center_col = shape[1] // 2
    # Create horizontal line (1xN)
    kernel[center_row, center_col : center_col + size] = 1.0
    kernel /= kernel.sum()
    return np.fft.ifftshift(kernel)

h_kernel = get_motion_kernel(img.shape, size=25)
H = np.fft.fft2(h_kernel)
# Apply blur in frequency domain
img_blurred = np.real(np.fft.ifft2(np.fft.fft2(img) * H))

# 4. Add Noise - Question 4
noise_level = 0.01
noise = np.random.normal(0, noise_level, img.shape)
img_noisy_blurred = np.clip(img_blurred + noise, 0, 1)

# 2 & 3. Restoration Functions - Question 2 & 3
def inverse_filter(noisy_img, H):
    G = np.fft.fft2(noisy_img)
    # Question 7: Dividing by small H values causes instability
    res = G / (H + 1e-3) 
    return np.clip(np.real(np.fft.ifft2(res)), 0, 1)

def wiener_filter(noisy_img, H, K=0.01):
    G = np.fft.fft2(noisy_img)
    H_conj = np.conj(H)
    # Wiener Formula: G * [H* / (|H|^2 + K)]
    res = G * (H_conj / (np.abs(H)**2 + K))
    return np.clip(np.real(np.fft.ifft2(res)), 0, 1)

# Apply filters
res_inverse = inverse_filter(img_noisy_blurred, H)
res_wiener = wiener_filter(img_noisy_blurred, H, K=0.02)

# 6. Calculate PSNR & SSIM (With DATA_RANGE Fixed) - Question 6
psnr_inv = psnr(img, res_inverse, data_range=1.0)
ssim_inv = ssim(img, res_inverse, data_range=1.0)

psnr_wie = psnr(img, res_wiener, data_range=1.0)
ssim_wie = ssim(img, res_wiener, data_range=1.0)

print(f"--- Results for Noisy Blurred Image ---")
print(f"Inverse Filter: PSNR = {psnr_inv:.2f} dB, SSIM = {ssim_inv:.4f}")
print(f"Wiener Filter:  PSNR = {psnr_wie:.2f} dB, SSIM = {ssim_wie:.4f}")

# 5. Comparison Visualization - Question 5
titles = ['Original', 'Blurred+Noise', 'Inverse (Unstable)', 'Wiener (Restored)']
images = [img, img_noisy_blurred, res_inverse, res_wiener]

plt.figure(figsize=(20, 5))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(f"{titles[i]}\nPSNR: {psnr(img, images[i], data_range=1.0):.1f}")
    plt.axis('off')
plt.show()