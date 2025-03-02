import matplotlib.pyplot as plt

def display_images(original, filtered, title1, title2):
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title(title1)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(filtered)
    plt.title(title2)
    plt.axis('off')
    plt.show()