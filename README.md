# IMAGE-RESTORATION-INVERSE-VS.-WIENER-FILTERING
# Image Restoration Project: Inverse vs. Wiener Filtering

This project implements and compares two primary methods for restoring an image that has been degraded by motion blur and digital noise.

## Project Overview

The script `sc.py` follows a specific image processing workflow to address the following tasks:

* **Motion Blur Simulation**: Creates a horizontal blur effect using a $1 \times N$ kernel applied in the frequency domain.
* **Noise Addition**: Adds Gaussian noise to the blurred image to simulate real-world sensor interference.
* **Inverse Filtering**: Implements the standard restoration method by dividing the image spectrum by the blur kernel.
* **Wiener Filtering**: Implements a robust restoration method that balances blur removal and noise suppression using a constant $K$.
* **Quality Metrics**: Calculates **PSNR** (Peak Signal-to-Noise Ratio) and **SSIM** (Structural Similarity Index) to evaluate the restoration quality.

## Comparison of Methods

| Feature | Inverse Filter | Wiener Filter |
| :--- | :--- | :--- |
| **Noise Handling** | Poor; amplifies noise significantly. | Good; suppresses noise while restoring. |
| **Stability** | Unstable; dividing by small kernel values causes artifacts. | Stable; uses a $K$ factor to prevent division by zero. |
| **Visual Result** | Often results in heavy distortion or "snow". | Much clearer and closer to the original image. |

## Technical Implementation

### Degradation Model
The image is modeled as $G(u, v) = H(u, v)F(u, v) + N(u, v)$, where $H$ is the blur and $N$ is the noise.

### Wiener Filter Formula
The Wiener filter is calculated as:
$$F_{est} = \left[ \frac{H^*}{|H|^2 + K} \right] G$$
The parameter $K$ (set to 0.02 in the code) is used to stabilize the restoration against noise.

## Installation and Usage

1.  **Requirements**: Install the necessary Python libraries:
    ```bash
    pip install opencv-python numpy matplotlib scikit-image
    ```
2.  **Input Image**: Place an image named `corruptedimg.jpg` in the same directory as the script.
3.  **Run**: Execute the script to see the visual comparison and quality scores:
    ```bash
    python sc.py
    ```
