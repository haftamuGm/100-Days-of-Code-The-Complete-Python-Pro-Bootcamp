from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def load_image(image_path):
    return Image.open(image_path)


def resize_image(image, size=(100, 100)):
    return image.resize(size)


def get_dominant_colors(image, num_colors=5):
    image_array = np.array(image)
    pixels = image_array.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)
    return colors


def display_palette(colors):
    plt.figure(figsize=(len(colors), 1))
    for i, color in enumerate(colors):
        plt.fill_between([i, i + 1], 0, 1, color=color / 255)
    plt.xticks([])
    plt.yticks([])
    plt.show()


def main(image_path, num_colors=5):
    image = load_image(image_path)
    image = resize_image(image)
    colors = get_dominant_colors(image, num_colors)
    print("Dominant Colors (RGB):", colors)
    display_palette(colors)


if __name__ == "__main__":
    image_path = "hafi.jpg"
    num_colors = 5
    main(image_path, num_colors)