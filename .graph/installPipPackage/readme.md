sch: https://www.google.com/search?q=jupyter+notebook+pip+install+package

# ai:
https://chat.openai.com/share/4d442c65-0339-46bd-9e02-8268e5c9818e

>Install OpenCV: In the first cell of your new Jupyter Notebook, type the following command to install OpenCV using pip:

```
!pip install opencv-python
```
>Execute the cell: To run the installation command, click on the cell to select it, and then press "Shift + Enter" or click the "Run" button in the toolbar.
>Verify the installation: After the installation completes, you can verify if OpenCV is installed correctly by importing it in another cell and checking its version:
```
import cv2
print(cv2.__version__)
```

# guide:
**Top.Favorite:**
- [Installing Python Packages from a Jupyter Notebook](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)

>Fundamentally the problem is usually rooted in the fact that the Jupyter kernels are disconnected from Jupyter's shell; in other words, the installer points to a different Python version than is being used in the notebook. In the simplest contexts this issue does not arise, but when it does, debugging the problem requires knowledge of the intricacies of the operating system, the intricacies of Python package installation, and the intricacies of Jupyter itself. In other words, the Jupyter notebook, like all abstractions, is leaky.

else:
- [Install Python package using Jupyter Notebook - GeeksforGeeks](https://www.geeksforgeeks.org/install-python-package-using-jupyter-notebook/)
