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

# Lab1: K-Means & PCA 

As the first unsupervised algorithm, you are going to see how to cluster 8x8 images, containing handwritten digits 
using the well-known K-Means algorithm. Moreover, to practice dimensionality reduction, the PCA algorithm is employed 
as the pre-processing. The code is forked from 
[here](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans). 

### Running under the Jupyter Notebook


To run the *handwritten digit clustering* provided in this repository, do the followings:
1. download the *handwritten_digit_clustering.ipynb* file
2. run the following command in the the path containing the *ipynb* file.

```
jupyter notebook handwritten_digit_clustering.ipynb
```
# Lab2: TBA 
