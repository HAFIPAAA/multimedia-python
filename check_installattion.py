import pygame
import PIL
import cv2
import moviepy.editor as mp
import pkg_resources
import numpy
import scipy  # Tambahkan scipy

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)

    try:
        moviepy_version = pkg_resources.get_distribution("moviepy").version
        print("✅ MoviePy version:", moviepy_version)
    except Exception as e:
        print("❌ Could not determine MoviePy version:", e)

    try:
        numpy_version = pkg_resources.get_distribution("numpy").version
        print("✅ NumPy version:", numpy_version)
    except Exception as e:
        print("❌ Could not determine NumPy version:", e)

    try:
        scipy_version = pkg_resources.get_distribution("scipy").version
        print("✅ SciPy version:", scipy_version)
    except Exception as e:
        print("❌ Could not determine SciPy version:", e)

if __name__ == "__main__":
    check_installation()
