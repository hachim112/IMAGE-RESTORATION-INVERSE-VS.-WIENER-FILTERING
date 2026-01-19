# IMAGE-RESTORATION-INVERSE-VS.-WIENER-FILTERING
This project demonstrates how to restore an image that has been damaged by motion blur and digital noise. It compares two mathematical methods to see which one performs better under realistic conditions.

Project Steps
Simulate Motion Blur: The code creates a horizontal blur effect using a 1xN kernel.

Add Noise: Random Gaussian noise is added to the blurred image to simulate a low-quality camera sensor.

Inverse Filter: A simple method that tries to reverse the blur by dividing the image frequencies.

Wiener Filter: A more advanced method that balances removing the blur while ignoring the noise.

Evaluation: The script calculates PSNR and SSIM scores to measure how close the restored image is to the original.

Why Wiener is Better than Inverse
Inverse Filtering Instability: When an image has noise, the inverse filter accidentally multiplies that noise, making the final image look like "snow" or static.

Wiener Filtering Stability: The Wiener filter uses a constant (K) to stay stable. It knows when to stop trying to fix the blur to avoid making the noise worse.

How to Use
Requirements: Install opencv-python, numpy, matplotlib, and scikit-image.

Setup: Place your image in the folder and name it corruptedimg.jpg.

Run: Execute python sc.py to see the side-by-side comparison and the quality scores.
