import numpy as np
import matplotlib.pyplot as plt

def plot_images(X, num_of_imgs=20, max_intensity=16):
    # X: Nx64 matrix, containing N images of 8x8 pixels
    num_of_imgs = min(num_of_imgs, np.shape(X)[0])
    for i in range(num_of_imgs):
        plt.subplot(1, num_of_imgs, i+1)
        img = np.reshape(X[i], (8, 8))
        plt.imshow(max_intensity - img)
        plt.gray()
        plt.axis('off')
    plt.show()

def plot_loss(loss):
    plt.plot(loss)
    plt.title('Train Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.show()
