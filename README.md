# Lab material for *Unsupervised Learning* course
Learn some samples of unsupervised learning in python using jupyter notebook.

This repository provides lab materials for the [Unsupervised Learning online course](http://edu.synnovateinc.com/courses/ai-ml-2/), 
supported by [Synnovate Inc](http://synnovateinc.com/). 

## Prerequisites
#### Python

Install [python](http://www.python.org) according to your OS.
Make sure that you have successfully installed python (version 3.6 or above) in your system.
To do so, in the command prompt, type the `python --version` command. Go ahead if the version is 3.6 or above.
 
#### Jupyter Notebook

To install the `jupyter noteook`, run the following command:

```bash
pip install jupyter
```
If the installation goes well, the plain `jupyter notebook` command runs the web application that allows you to create 
and share documents that contain live code. So to make sure if you have installed the jupyter package correctly, 
run the follwoing command:
```bash
jupyter notebook
```
The above command will open a browser in your system, ready to launch an implementaion under the jupyter machine.

#### Other Packages

In this repository, we use the `scikit-learn`, the well-known machine learning package in Python. 
Besides, the following packages should be installed for matrix manipulations and plots:

* matplotlib
* numpy

To install the required packages in one shot, go ahead and download the `requirments.txt` 
file from the repository, and run the following command in the path containing the txt file:

```bash
pip install -r requirements.txt
```

# Lab1: K-Means Clustering 

As the first unsupervised algorithm, you are going to see how to cluster 8x8 images, containing handwritten digits 
using the well-known K-Means algorithm.  

### Running under the Jupyter Notebook

To run the *handwritten digit clustering* provided in this repository, do the followings:
1. Download the *Lab1* folder.
2. Run the following command in a command prompt in the the folder path.

```
jupyter notebook handwritten_digit_clustering.ipynb
```
# Lab2: Dimensionality Reduction

To learn the `scikit-learn` package for dimensionality reduction, we compare two well-known methods:

* Principal Component Analysis (PCA)
* t-Distributed Stochastic Neighbor Embedding (t-SNE)

We are going to see the Handwritten digits in 2D plot generated by PCA and t-SNE.
Download the `Lab2` folder in this repository and run the following command:

```
jupyter notebook dimensionality_reduction.ipynb
```

# Lab3: Autoencoder

We would like to start our first real deep learning project, an autoencoder, for feature learning on the same 
handwritten digits dataset. To make it even more "deep learning project", let's utilize [pytorch](https://pytorch.org/) 
as one of the famous deep learning frameworks. So go ahead and install the pytorch using pip command, as guided in 
[this page](https://pytorch.org/get-started/locally/).

For example, to install the stable latest version of pytorch on windows using pip, the follwoing command works:
```buildoutcfg
pip install torch===1.5.1 torchvision===0.6.1 -f https://download.pytorch.org/whl/torch_stable.html
```
As mentioned above, [this page](https://pytorch.org/get-started/locally/) is helpful for other variations of installation. 