# 🎨 Color Dominant Extraction

This Python script extracts and visualizes the dominant colors from an image using **K-Means clustering**. It's a lightweight tool for identifying key color palettes from any image—perfect for designers, developers, and artists.

---

## 🔍 Features

- ✅ Loads and converts images to RGB
- ✅ Resizes the image for optimized performance
- ✅ Extracts dominant colors using K-Means
- ✅ Visualizes color palette using Matplotlib

---

## 🛠️ Tech Stack

- [OpenCV](https://opencv.org/)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [NumPy](https://numpy.org/)

---

## 🚀 How It Works

1. 📸 Load and convert image to RGB.
2. 🔧 Resize for faster computation.
3. 🧮 Reshape and apply K-Means clustering.
4. 🎨 Visualize each color cluster as a block.

---

## 🖼️ Output Example

The output will be a visual representation of the top `k` dominant colors, displayed as side-by-side color blocks:
