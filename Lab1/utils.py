import numpy as np
import matplotlib.pyplot as plt
def split_samples_by_indices(X, y):
    # X: Nx64 matrix, containing N images of 8x8 pixels
    # y: a vector of length N containing indices ranging from 0 to 9 regarding each row of X
    dataset = np.concatenate((X, np.reshape(y, (-1, 1))), axis=1)
    class0 = [sample[0:-1] for sample in dataset if sample[-1] == 0]
    class1 = [sample[0:-1] for sample in dataset if sample[-1] == 1]
    class2 = [sample[0:-1] for sample in dataset if sample[-1] == 2]
    class3 = [sample[0:-1] for sample in dataset if sample[-1] == 3]
    class4 = [sample[0:-1] for sample in dataset if sample[-1] == 4]
    class5 = [sample[0:-1] for sample in dataset if sample[-1] == 5]
    class6 = [sample[0:-1] for sample in dataset if sample[-1] == 6]
    class7 = [sample[0:-1] for sample in dataset if sample[-1] == 7]
    class8 = [sample[0:-1] for sample in dataset if sample[-1] == 8]
    class9 = [sample[0:-1] for sample in dataset if sample[-1] == 9]

    return [class0, class1, class2, class3, class4, class5, class6, class7, class8, class9]

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

def plot_clusters(X, indices, num_of_imgs=20, max_intensity=16):
    # X: Nx64 matrix, containing N images of 8x8 pixels
    # indices: vector of the length N, containing the cluster indices
    img_groups = split_samples_by_indices(X, indices)
    for i in range(len(img_groups)):
        print("cluster %s: %s" % (i, np.shape(img_groups[i])))
        plot_images(img_groups[i])

def plot_centroids(clusters, order=range(10)):
    images = np.zeros((len(order), 64))
    for i in range(len(order)):
        images[i, :] = np.reshape(clusters.cluster_centers_[order[i]], (1, -1))
    plot_images(images)
    
def plot_2D_samples(X, indices, title="2D samples"):
    # X: Nx2 matrix, containing N samples of 2D
    # indices: vector of the length N, containing the group indices ranging from 0 to 9
    group_list = split_samples_by_indices(X, indices)
    colors = ["r", "g", "b", "c", "m", "y", "k", "#FAC268", "#FA818A", "#A99BFA"]
    for i in range(len(np.unique(indices))):
        c = np.array(group_list[i])
        plt.scatter(c[:, 0], c[:, 1], color=colors[i])
    plt.legend(["y0", "y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8", "y9"])
    plt.title(title)
