#!/usr/bin/env python
# coding: utf-8

# <div style="display: flex; align-items: center;">
#     <img src="https://www.avantihnw.com/api/rp/w1200/h630/aHR0cHM6Ly93d3cuYXZhbnRpaG53LmNvbS9kYXRhL2VuLzEvMDEvZmVkYmMyMTItN2M3Zi00NTJjLWE4YmItMjQ3Nzk5OTRlMWUyLmpwZw===.jpg" alt="Image Alt Text" width="500" height="200" style="margin-right: 20px;">
#     <div style="font-size: 60px;">
#          <strong> 3<sup>rd</sup> lab <strong>
#     <div style="font-size: 40px;margin-right: 30px">
#          <strong> MRI: DICOM Images <strong>
#     </div>
# </div>

# <table>
#   <tr>
#     <td style="background-color: rgba(114, 147, 203, 0.9); font-size: 15px; color: white; padding: 20px;">
#       <div style="font-size: 20px"> 
#           <strong>XCT Module (2 x 2h)</strong><br>
#       </div>  
#       <ul>
#         <li> <strong> Week 1 : visualisation and using of ready-to-use functions</strong> (2h)</li>
#         <ul>
#            <li> discover scikit image libary for XCT 
#            <li> read files
#            <li> plot profiles and global criteria
#            <li> projections, sinograms
#            <li> reconstruction with library functions (inverse Radon, FBP, SART)
#         </ul>
#         <br> 
#         <li> <strong> Week 2 : code writing and analyses</strong> (2h)</li>
#         <ul>
#            <li> SART reconstruction code
#            <li> FBP coding
#            <li> compare with ready-to-use functions
#            <li> use of global and local metrics to compare the results
#         </ul>
#     </td>
#     <td style="background-color: rgba(225, 151, 76, 0.7); font-size: 15px; color: white; padding: 20px; vertical-align: top;">
#     <div style="font-size: 20px"> 
#         <strong> MRI Module (2 x 2h)</strong><br>
#     </div> 
#     <ul>
#         <li> <strong> Week 3 : visualisation and using of ready-to-use functions</strong> (2h)</li>
#         <ul>
#            <li> read files, analyse the data and the image content
#         </ul>
#         <br> 
#         <li> <strong> Week 4 : Explore 3D images, windows and views </strong> (2h)</li>
#     </td>
#     <td style="background-color: rgba(132, 186, 91, 0.8); font-size: 15px; color: white; padding: 20px; vertical-align: top;">
#     <div style="font-size: 20px"> 
#       <strong> Numerisation Module (2 x 2h)</strong><br>
#     </div> 
#       <ul>
#         <li> <strong> Week 5 : depth map exploration </strong> (2h)</li>
#         <br> 
#         <li> <strong> Week 6 : point cloud and mesh understanding</strong> (2h)</li>
#     </td>
#   </tr>
# </table>
# 

# <div style="display: flex; align-items: center;">
#     <img src="https://img.freepik.com/premium-vector/warning-signs-high-voltage-hazard-isolated-white-background_68708-427.jpg?w=2000" alt="Image Alt Text" width="50" height="50" style="margin-right: 20px;">
#     <div style="font-size: 15px;margin-right: 30px">
#             Each lab must be completed before the beginning of the other lab session. 
#         <br> 
#           <strong>Don't forget to entitle your .ipynb file with your name and surname. <strong>
#         <br> 
#          The final submission of the first module has to be done <strong> by Tuesday 16<sup> th</sup>October before 10 am.</strong>
#     </div>
# </div>

# <table>
#       <td style="border-left: 3px solid rgba(114, 147, 203, 0.9); background-color: rgba(114, 147, 203, 0.1); font-size: 15px; color: blakc; padding-left: 30px;">
#         Don't forget to legend your figures and graphs. Interpretations are expected and must by short but comprehensive.  
#       </td>
# </table>

# #### Contact : meghna.parameswaran-ayyar@u-bordeaux.fr

# <div style="display: flex; align-items: center;">
#     <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/T1-weighted-MRI.png" alt="Image Alt Text" width="100" height="100" style="margin-right: 20px;">
#     <div style="font-size: 20px;margin-right: 30px">
#          <strong> Reading and Understanding DICOM <strong>
#     </div>
# </div>

# ## DICOM:  Digital Imaging and Communications in Medicine standard
# 
# It is just an image format that is used for viewing different medical images acquired by different modalities. DICOM differs from other image formats in that it groups information into data sets. A DICOM file consists of a header and image data sets, all packed into a single file.
# 
# 
# 
# 
# 
# 
# Ref: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3354356/

# The goal of this assignment is to be able to open, display and reader the header information from a DICOM file.

# <div style="display: flex; align-items: center;">
#     <img src="https://pydicom.github.io/images/logo/logo.png" alt="Image Alt Text" width="50" height="50" style="margin-right: 20px;">
#     <div style="font-size: 20px;margin-right: 15px">
#            We will use <strong>pydicom</strong>. 
#     </div>
# </div>

# Install the pydicom library locally. (https://github.com/pydicom/pydicom)

# In[1]:


# Install
get_ipython().system('pip install pydicom')


# There is a `.dcm` file provided along with the notebook. 
# 1. Read this DICOM file. (Ensure it is saved in the same folder as this notebook)
# 2. Get the DICOM data. A quick example of the fields has been shown below

# In[2]:


# specify your image path
from pydicom import dcmread
import pydicom
import matplotlib.pylab as plt

image_path = 'sample_mri.dcm'
ds = pydicom.dcmread(image_path)

patien_name = ds.PatientName

display_name = patien_name.family_name + ", " + patien_name.given_name
print("Patient's name...:", display_name)
print("Patient id.......:", ds.PatientID)
print("Modality.........:", ds.Modality)


# 1. What do you see from the results and what might some other useful header fields?
# 2. Which field contains the actual image?
# 3. What information are needed to visualize a DICOM image ? For example, what is the meaning of the *pixel spacing* parameter ?

# ANSWERS
# 1:Study description: Describes the type and purpose of the study.
# Series description: Provides additional information about the specific image series within the study.
# Image orientation: Describes the orientation and position of the image in relation to the patient.
# Acquisition parameters: Details about how the image was acquired, including slice thickness, exposure settings, etc.
# Image dimensions: Information about the number of rows and columns in the image.
# Pixel data type: Specifies the data type and format of the pixel data (e.g., 16-bit signed integer).\
# 
# 2:The actual image data in a DICOM file is typically stored in the "Pixel Data" field. 
# 
# 3:Pixel Data: This is the most critical field as it contains the actual image pixel values.
# Rows and Columns: These parameters specify the dimensions of the image, i.e., the number of rows and columns.
# Pixel Spacing: Pixel spacing is a crucial parameter that defines the physical size of each pixel in millimeters (mm). It consists of two values: the row spacing (spacing between rows) and the column spacing (spacing between columns). It's essential for accurately scaling the image for visualization.
# 
# 

# 

# ### Visualizing the image
# 
# After you found the field with the image data:
# 
# 1. Try to display it as image using `matplotlib.pyplot` and use the `cmap` as `pyplot.cm.gray`
# 2. What does the *pydicom.data.get_testdata_files()* function do ?
# The pydicom.data.get_testdata_files() function is a utility provided by the PyDICOM library in Python. It is used to retrieve a list of paths to test data files that come bundled with the PyDICOM library. These test data files are typically DICOM files that are included to facilitate testing and development with the PyDICOM library.
# 
# The function returns a list of file paths to these test data files, allowing you to access them programmatically for various purposes, such as testing your DICOM parsing and processing code, learning how to work with DICOM files, or using them as sample data for experimentation
# 

# In[3]:


plt.imshow(ds.pixel_array,cmap='gray')
plt.colorbar()
plt.show()


# ANSWER

# ### Display multiple images
# 
# There is another folder provided with other .dcm files. Write a code to display thumbnails of all the DICOM files from the folder

# In[4]:


#image path
import os
image_path = 'mri'

for ds in os.listdir(image_path):
    image_filename = os.path.join(image_path, ds)
    ds = pydicom.dcmread(image_filename)
    patien_name = ds.PatientName

    display_name = patien_name.family_name + ", " + patien_name.given_name
    print("Patient's name...:", display_name)
    print("Patient id.......:", ds.PatientID)
    print("Modality.........:", ds.Modality)


# ### Investigate the image
# 
# To begin, check what range of the graylevels are present in the DICOM file for the image. Comment on what would be needed for visualization of such a range on our screens

# In[36]:


import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# Define the path to the DICOM images
image_path = 'mri'
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
y_coordinate = 100

for i, ds_filename in enumerate(os.listdir(image_path)):
    if i >= 6:  # Display up to 6 images
        break

    ds = pydicom.dcmread(os.path.join(image_path, ds_filename))
    patient_name = ds.PatientName
    display_name = patient_name.family_name + ", " + patient_name.given_name

    ax = axes[i // 3, i % 3]
    im = ax.imshow(ds.pixel_array, cmap='gray')
    ax.set_title(f"Patient: {display_name}\nID: {ds.PatientID}\nModality: {ds.Modality}")
    ax.axis('on')

    max_gray_level = ds.pixel_array.max()
    
    intensity_profile_original = ds.pixel_array[y_coordinate, :]
    
    ax.text(0.5, 0.05, f"Max Gray Level: {max_gray_level}", color='red', transform=ax.transAxes,
            horizontalalignment='center', backgroundcolor='black')

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Pixel Value", rotation=270, labelpad=15)
    
    # Create a subplot for the intensity profile
    plt.figure(figsize=(12, 5))
    plt.plot(intensity_profile_original, label='Image before method')
    plt.xlabel('Pixel Position')
    plt.ylabel('Intensity')
    plt.title('Intensity Profile (Image before method)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
for ax in axes.ravel():
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())

plt.tight_layout()
plt.show()


# As a maximum gray value I m taking the number to represent the diffrence from others: Most importatly I have noticed some images have different gray levels. and many images have lie 0 to 1200 but the maximum gray level is different. 

# ANSWER
# 
# 
# 
# 
# 
# 

# There are multiple ways of handling this. In the previous question we found what is the maximum value of graylevel that we can display on our screen. For the rest of the assignment we denote this as **MAXVAL**. Thus we want the graylevels to be in the range [0, **MAXVAL**]
# 
# I m taking maximum value from each gray DICOM images:   max_gray_level = ds.pixel_array.max()
# 
# #### With every plot ensure to plot the colorbar to visualize the intensities of the final image
# 
# Also,
# 
# 1. Plot the profile of the image before applying the methods and after.
# 2. For each of the method visualize: The image with the chosen profile, the intensities of that profile BEFORE the method and the intensities of the profile after the method.
# 3. Comment on if there is a difference in the two methods what you might say is the more informative one. 
# 4. Try to do the same for a couple of other images from the folder: (You can choose)
# 
# 

# **METHOD 1**: Naive Method
# Divide the pixels values by **MAXVAL** and display this image
# 
# - Hint check the use of `np.clip` to keep pixels that are within a range to set the rest to 0

# In[37]:


import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# Define the range for pixel value normalization
MINVAL = 0 
MAXVAL = 255
y_coordinate = 100

image_path = 'mri'
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for i, ds_filename in enumerate(os.listdir(image_path)):
    if i >= 6:  # thumbnails
        break

    ds = pydicom.dcmread(os.path.join(image_path, ds_filename))
    patient_name = ds.PatientName
    display_name = patient_name.family_name + ", " + patient_name.given_name

    ax = axes[i // 3, i % 3]

    # Normalize pixel values by dividing by MAXVAL
    img = ds.pixel_array / MAXVAL
    pixel_array_normalized = np.clip(img,MINVAL, MAXVAL) 
    intensity_profile_m= pixel_array_normalized[y_coordinate, :]

    im = ax.imshow(pixel_array_normalized, cmap='gray')
    ax.set_title(f"Patient: {display_name}\nID: {ds.PatientID}\nModality: {ds.Modality}")
    ax.axis('on')

    max_gray_level = pixel_array_normalized.max()
    ax.text(0.5, 0.05, f"Max Gray Level: {max_gray_level:.2f}", color='red', transform=ax.transAxes,
            horizontalalignment='center', backgroundcolor='black')

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Normalized Pixel Value")
      # Create a subplot for the intensity profile
    plt.figure(figsize=(12, 5))
    plt.plot(intensity_profile_m, label='Image after method')
    plt.xlabel('Pixel Position')
    plt.ylabel('Intensity')
    plt.title('Intensity Profile (Image after method)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

for ax in axes.ravel():
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())

plt.tight_layout()
plt.show()


# **METHOD 2**: Min-Max Method. 
# 
# Find the min and max value of the pixels. Use these values to set the range of the pixels to be in [0, **MAXVAL**]
# 
# Use this and display the new image that you get

# In[39]:


import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# # Define the desired range for pixel value normalization
# MINVAL = 0
# MAXVAL = 4095  
y_coordinate = 100
image_path = 'mri'
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for i, ds_filename in enumerate(os.listdir(image_path)):
    if i >= 6:  # thumbnails
        break

    ds = pydicom.dcmread(os.path.join(image_path, ds_filename))
    patient_name = ds.PatientName
    display_name = patient_name.family_name + ", " + patient_name.given_name

    ax = axes[i // 3, i % 3]

    # Find the min and max pixel values in the DICOM image
    pixel_array = ds.pixel_array
    min_val = np.min(pixel_array)
    max_val = np.max(pixel_array)
    print(f'min value and max value:',min_val, max_val)

    # Normalize the pixel values to the specified range [0, MAXVAL]
    pixel_array_normalized = (pixel_array - min_val) / (max_val - min_val) *255
    intensity_profile_m2 = pixel_array_normalized[y_coordinate, :]

    im = ax.imshow(pixel_array_normalized, cmap='gray')
    ax.set_title(f"Patient: {display_name}\nID: {ds.PatientID}\nModality: {ds.Modality}")
    ax.axis('on')

    max_gray_level = pixel_array_normalized.max()
    ax.text(0.5, 0.05, f"Max Gray Level: {max_gray_level:.2f}", color='red', transform=ax.transAxes,
            horizontalalignment='center', backgroundcolor='black')
    
    plt.figure(figsize=(12, 5))
    plt.plot(intensity_profile_m2, label='Image after method')
    plt.xlabel('Pixel Position')
    plt.ylabel('Intensity')
    plt.title('Intensity Profile (Image after method)')
    plt.legend()

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Normalized Pixel Value")

for ax in axes.ravel():
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())

plt.tight_layout()
plt.show()


# ANSWER
# 3. First we use the usual method to visualize the image from the MRI folder and I noticed it has a few dicom images in different gray levels. then after visualization the maximum gray level goes to more than 1000 in every image then after 1 method we divide each image from the maximum gray value and clip it to see some interesting stuff but we realize it is already preprocessed so it doesn’t look different even the intensity values are similar. 
# after 1 method the range goes to 1nto 5 and some 1 to 8. 
# so then we normalize the image using min and max value in each image to get back to 0 and 255 as a good practice most importantly, everything is same nothing look different.
# 

# 4. Try to do the same visualization for 1/2 images from the folder

# 
