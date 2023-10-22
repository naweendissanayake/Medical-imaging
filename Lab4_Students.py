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
#            <li> using DICOM
#         </ul>
#         <br> 
#         <li> <strong> Week 4 : Explore 3D images, windows and views </strong> (2h)</li>
#         <li> using NIfTI images
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
#          The final submission of the first module has to be done <strong> by Thursday 19<sup> th</sup> October before 10 am.</strong>
#     </div>
# </div>

# <table>
#       <td style="border-left: 3px solid rgba(114, 147, 203, 0.9); background-color: rgba(114, 147, 203, 0.1); font-size: 15px; color: blakc; padding-left: 30px;">
#         Don't forget to legend your figures and graphs. Interpretations are expected and must by short but comprehensive.  
#       </td>
# </table>

# #### Contact : meghna.parameswaran-ayyar@u-bordeaux.fr

# We saw two types of normalizations last week. There is another method which uses two metadata fields of the DICOM
# 
# ### **METHOD 3:** Windowing
# 
# 1. Load the `sample_mri.dcm` and get the WindowWidth and WindowCenter values. These two vaues give you the intensities of interest in the scan.
# 2. Use the center and the width to find the range of intensities that are of interest in the MRI. 
# 3. Use `np.clip` to discard the intensities that lie beyond the range that you calculated above
# 4. Use the min-max method to normalize the values to [0, 255]
# 5. Plot the final image and the corresponding colorbar

# In[1]:


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
get the WindowWidth and WindowCenter values. These two vaues give you the intensities of interest in the scan.


# In[2]:


plt.imshow(ds.pixel_array,cmap='gray')
plt.colorbar()
plt.show()


# In[11]:


import numpy as np
image_data = ds.pixel_array

window_width = ds.WindowWidth
window_center = ds.WindowCenter
lower_intensity = ds.WindowCenter - ds.WindowWidth / 2
upper_intensity = ds.WindowCenter + ds.WindowWidth / 2

print("WindowWidth......:", window_width)
print("WindowCenter......:", window_center)
print("Intensity Range...: ({}, {})".format(lower_intensity, upper_intensity))


# In[14]:


image_data.shape


# In[13]:


clipped_image_data = np.clip(image_data, lower_bound, upper_bound)


plt.imshow(clipped_image_data, cmap='gray')
plt.title("MRI Image with Clipped Intensity Range")
plt.colorbar()
plt.show()



# In[15]:


clipped_image_data.shape


# In[149]:


min_value = np.min(clipped_image_data)
max_value = np.max(clipped_image_data)


normalized_image_data = ((clipped_image_data - min_value) / (max_value - min_value)) * 255
normalized_image_data = normalized_image_data.astype(np.uint8)
print(min_value)
print(max_value)

plt.imshow(normalized_image_data, cmap='gray')
plt.title("Normalized MRI Image")
plt.colorbar()
plt.show()


# Comment on the range of intensities in the colorbar with this method and the other 2 from the previous lab
# 
# 1. 
# 

# A small caveat for this exercise is, as previously discussed, the images we use in this lab are already pre-processed. So you may not notice a visible change in the image while viewing it. Plot the colorbar to see the effect of this normalization. In the further sections we will work with 3D images where you will be able to vizualize the difference.

# <div style="display: flex; align-items: center;">
#     <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/T1-weighted-MRI.png" alt="Image Alt Text" width="100" height="100" style="margin-right: 20px;">
#     <div style="font-size: 20px;margin-right: 30px">
#          <strong> Reading and Understanding NIfTI <strong>
#     </div>
# </div>

# ## NIfTI: Neuroimaging Informatics Technology Initiative
# 
# It is a data format for the storage of MRI and other medical images
# 
# Ref: https://neuraldatascience.io/8-mri/nifti.html

# The goal of this assignment is to be able to open, display and reader the header information from a `.nii` file.

# NIfTI-1, DICOM, and ANALYZE are three distinct formats used in the field of medical imaging, and they serve different purposes and have different characteristics. Here's a comparison of these formats:
# 
# #### Purpose:
# 
# - NIfTI-1: NIfTI-1 is primarily used for neuroimaging data, particularly in the context of MRI and fMRI data. It is designed to store and share imaging data in a standardized and flexible manner.
# 
# - DICOM: DICOM (Digital Imaging and Communications in Medicine) is a widely used format in medical imaging for storing and exchanging various types of medical images, not limited to neuroimaging. It includes a broader range of medical imaging modalities, such as X-rays, CT scans, ultrasound, and more.
# 
# - ANALYZE: ANALYZE is an older format primarily used for storing 3D and 4D (spatiotemporal) medical imaging data. It was widely used in the past but has been largely replaced by NIfTI-1 and DICOM due to their improved features and standards.
# 
# #### Metadata and Flexibility:
# 
# - NIfTI-1: NIfTI-1 provides a standardized header that includes metadata about the data, making it easier to interpret and work with. It also allows for optional extensions to store additional information, increasing its flexibility.
# 
# - DICOM: DICOM is highly standardized and includes extensive metadata for various types of medical images. It is designed to accommodate a wide range of medical imaging equipment and modalities, making it highly flexible.
# 
# - ANALYZE: ANALYZE has a simpler header compared to NIfTI-1 and DICOM, which can limit its ability to capture extensive metadata. It is less flexible in comparison.
# 
# #### Coordinate System:
# 
# - NIfTI-1: NIfTI-1 defines a standard coordinate system for data, which helps ensure consistency when working with brain images.
# 
# - DICOM: DICOM does not prescribe a specific coordinate system. Instead, it includes patient position and orientation information that can vary between different modalities and vendors.
# 
# - ANALYZE: ANALYZE does not define a standard coordinate system either. It relies on basic orientation information in the header.
# 
# #### Compression:
# 
# - NIfTI-1: NIfTI-1 files can be optionally compressed using GZIP, which can help reduce file sizes.
# 
# - DICOM: DICOM files can also be compressed, often using lossless compression methods like JPEG-LS or JPEG2000.
# 
# - ANALYZE: ANALYZE files typically do not include built-in compression options.
# 
# In summary, NIfTI-1, DICOM, and ANALYZE are three distinct formats used in medical imaging, with NIfTI-1 being specifically tailored to neuroimaging, DICOM being a broader standard for medical imaging, and ANALYZE being an older format that has been largely replaced by NIfTI-1 and DICOM in modern medical imaging practice. The choice of format depends on the specific imaging modality and the needs of the research or clinical application.

# <div style="display: flex; align-items: center;">
#     <img src="https://nipy.org/nibabel/_static/nibabel-logo.svg" alt="Image Alt Text" width="100" height="100" style="margin-right: 20px;">
#     <div style="font-size: 20px;margin-right: 15px">
#            We will use <strong>Nibabel</strong>. 
#     </div>
# </div>

# Install nibabel library locally. (https://nipy.org/nibabel/)

# In[23]:


get_ipython().system('pip install nibabel')


# In[26]:


import nibabel as nib


# There is a compressed `.nii` file provided along with the notebook. 
# 1. Read this NIfTI file. (Ensure it is saved in the same folder as this notebook)

# In[68]:


images = nib.load('sample_MRI.nii.gz')
print(images.header)


# In[77]:


images = nib.load('sample_MRI.nii.gz').get_fdata()


print(images.shape) #note: 160 slices with 256 256 image size
plt.imshow(images[:,:,images.shape[2]//2], cmap='bone')
plt.show()


# In[66]:


#For fun : (
num_slices, num_rows, num_columns = images.shape

# Calculate the number of rows and columns for the subplot grid
num_rows_subplots = int(num_slices**0.5)
num_columns_subplots = (num_slices + num_rows_subplots - 1) // num_rows_subplots

# Create a figure and a grid of subplots
fig, axes = plt.subplots(num_rows_subplots, num_columns_subplots, figsize=(12, 8))

# Iterate through the slices and display them in the subplots
for i, ax in enumerate(axes.flat):
    if i < num_slices:
        ax.imshow(test_load[i, :, :], cmap='gray')
        ax.set_title(f"Slice {i}")
        ax.axis('off')
    else:
        # If there are more subplots than slices, hide the extra subplots
        ax.axis('off')

plt.tight_layout()
plt.show()


# note: 160 slices with  256 256 image size 

# You will notice that the image you read is an object of a custom class. 

# 
# 2. Similar to DICOM, these files also have a header with some metadata provided. Explore a way to access all the keys and identify some interesting ones
# 
# Extra reference: Qform, Sform : https://gru.stanford.edu/doku.php/mrtools/coordinatetransforms for some info about some of the fields (if you are curious about it)

# In[74]:


# some intersetig metadata

nifti_header = nifti_image.header

# metadata keys
metadata_keys = nifti_header.keys()

#  metadata keys
for key in metadata_keys:
    print(f"Metadata Key: {key}, Value: {nifti_header[key]}")

if 'patient_name' in metadata_keys:
    patient_name = nifti_header['patient_name']
    print(f"Patient's Name: {patient_name}")


# Image Shape and Dimensions:
# 
# dim: Provides the dimensions of the image data.
# pixdim: Defines the size of a voxel in each dimension.
# datatype: Specifies the data type used for pixel values (e.g., uint8, int16).
# Coordinate Systems:
# 
# qform_code and sform_code: Indicate the coordinate system for QForm and SForm transformations.
# qoffset_x, qoffset_y, qoffset_z: The translation in mm along the three primary axes for the QForm.
# srow_x, srow_y, srow_z: The rotation and translation components of the SForm.
# Patient and Study Information:
# 
# patient_name: The name of the patient.
# study_description: A description of the study.
# patient_id: The patient's unique identifier.
# study_date: The date when the study was conducted.
# Image Acquisition Parameters:
# 
# repetition_time (TR): Time between successive excitations in an MRI.
# echo_time (TE): Time to acquire the echo signal in an MRI.
# flip_angle: The flip angle used in MRI acquisitions.
# Image Orientation and Positioning:
# 
# qform_code and sform_code: Indicate the orientation code for QForm and SForm.
# qto_xyz, sto_xyz: Transformation matrices defining the orientation and position of the image.
# Data Units:
# 
# xyzt_units: Specifies the units for spatial and temporal dimensions.
# Image Descriptors:
# 
# descrip: A free-form description of the image.

# In[71]:


# I wanted to see Qform and Sform matrixces 
import nibabel as nib

# Load a NIfTI image
nifti_image = nib.load('sample_MRI.nii.gz')

# The transformation from image coordinates to magnet coordinats is 
# done by multiplying the 4×4 affine transformation matrix specified by the Qform times the image coordinates [Ximg Yimg Zimg]:
qform_matrix = nifti_image.affine
qform_translation = nifti_image.affine[:3, 3]

# Access the SForm matrix and translation vector
sform_matrix = nifti_image.get_sform()
sform_translation = nifti_image.get_sform()[:3, 3]

print("QForm matrix:")
print(qform_matrix)
print("QForm translation:")
print(qform_translation)

print("SForm matrix:")
print(sform_matrix)
print("SForm translation:")
print(sform_translation)


# Comment

# The header also has some methods that you can use to get extra data. Try the following code and observe what they might be useful for?
# 
# 
# Note: MRI is 3D and fMRI is (3D + time). This might affect what you see as output

# fMRI:
# 
# Captures dynamic 3D images over time to observe changes in activity.
# Used to study brain function and dynamic processes, such as brain activation during a task.
# Can visualize how brain activity changes over time.
# Combines spatial and temporal information, resulting in a 4D dataset (3D space + time).

# In[75]:


header_object = images.header
print(header_object.get_zooms())
print(header_object.get_xyzt_units())


# 3. Access the data from the object and identify the type and shape of data. 
# 4. Is the acquisition shape of this MRI a cube? (look at the dimensions of the data and Comment)

# Answers:
# 
# 3:dim, Value: [  3 160 256 256   1   1   1   1]
# Index 0 is represent the time and others are not meaningfull since it has 8 dimention
# 
# 4:the MRI data is not a cube; it is a stack of 2D images arranged in the form of a 3D volume.
# This is common for structural MRI data where the first dimension may represent time (T), which is not applicable in structural MRI. The positive values in the other dimensions indicate the voxel sizes along the X, Y, and Z dimensions.

# ### Visualizing the Slices
# 
# Unlike DICOM the .nii image is for MRI is a 3D image. 
# 
# 1. Can you list the 3 types of views that we have for neuroimaging? (eg Saggital etc..
# .)
# 
# ANSWER
# 

# Sagittal View:
# 
# The sagittal view provides a side view of the brain, showing it as if it were sliced from left to right. This view is useful for observing structures from the side and is often used to examine the brain's midline and asymmetries.
# Coronal View:
# 
# The coronal view presents a front-to-back or "crown-to-sole" perspective of the brain. It is akin to looking at the brain as if it were sliced from the front of the head to the back. This view is helpful for visualizing structures and features that are perpendicular to the sagittal view.
# Axial View (Transverse View):
# 
# The axial view, also known as the transverse view, provides a "top-down" perspective of the brain, as if it were sliced horizontally. This view allows for the examination of structures from above, looking down into the brain. It is especially useful for assessing brain regions in relation to one another.

# 

# 
# As we have a 3D image, we need to choose one slice to visualize at a time. 
# 
# 2. Choose any slice from the x-axis (first index) of your data and plot it using `matplotlib`. If the view is rotated use `ndimage.rotate` to correct the orientation of the matrix
# 3. Plot the same slice for the 3 different views (choose the same index slice for the 3 dimensions of the matrix). Use caption to name the views correctly

# In[102]:


import scipy.ndimage as ndi
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=[15, 5])

# slices 
sagittal_index = images.shape[1] // 2 
coronal_index = images.shape[1] // 2 
axial_index = images.shape[1] // 2  


im_sagittal = axs[0].imshow(ndi.rotate(test_load[sagittal_index, :, :], 90), cmap='bone')
axs[0].set_title('Sagittal View')
axs[0].axis('on')


im_coronal = axs[1].imshow(ndi.rotate(test_load[:, coronal_index, :], 90), cmap='bone')
axs[1].set_title('Coronal View')
axs[1].axis('on')

im_axial = axs[2].imshow(test_load[:, :, axial_index], cmap='bone')
axs[2].set_title('Axial View')
axs[2].axis('on')


cbar_sagittal = plt.colorbar(im_sagittal, ax=axs[0], shrink=0.6)
cbar_coronal = plt.colorbar(im_coronal, ax=axs[1], shrink=0.6)
cbar_axial = plt.colorbar(im_axial, ax=axs[2], shrink=0.6)

plt.tight_layout()
plt.show()


# ### Investigate at the intensities
# 
# 1. Can you choose small 3 x 3 x 3 size voxel patch from your image and visualize the values in it?
# 
# 2. Do these numbers convey any direct information? Can you guess what the range of the intensities in the image would depend on?
# These intensity values may convey information about the properties of the underlying tissues or structures in the scanned region. In medical imaging, the range of intensities in the image typically depends on several factors, including:
# 
# Tissue Composition: Different tissues in the human body have distinct density and composition, leading to variations in intensity values. For example, bones, muscles, fat, and organs may have different intensity levels.
# 
# Imaging Modality: The range of intensities can vary depending on the imaging modality used. For instance, X-ray, CT (Computed Tomography), MRI (Magnetic Resonance Imaging), and PET (Positron Emission Tomography) scans will have different intensity scales and relationships between tissue types.
# 
# Image Processing: Pre-processing steps such as normalization, scaling, or filtering can also affect the intensity range in an image.
# 
# Scanner Settings: Scanner parameters, such as voltage and exposure in X-ray imaging or sequence parameters in MRI, can influence intensity values.
# 
# Contrast Agents: The use of contrast agents in some imaging modalities can introduce variations in intensity, highlighting specific structures or areas.
# 
# Patient Characteristics: Patient-specific factors like age, weight, and medical conditions can influence tissue properties and, consequently, intensity values.
# 
# Quantization and Bit Depth: The number of bits used to represent each voxel's intensity affects the dynamic range and precision of intensity values.
# 
# 
# 3. Plot any slice of your choice like before but this time add the colorbar to observe the range of the intensities in that slice : It chnages 800 to 1600

# In[101]:


import matplotlib.pyplot as plt

# Define the coordinates of the center of the patch
center_x = images.shape[0] // 2
center_y = images.shape[1] // 2
center_z = images.shape[2] // 2

# Define the size of the voxel patch
patch_size = 3

# Extract the voxel patch
voxel_patch = images[
    center_x - patch_size // 2 : center_x + patch_size // 2 + 1,
    center_y - patch_size // 2 : center_y + patch_size // 2 + 1,
    center_z - patch_size // 2 : center_z + patch_size // 2 + 1
]

# Visualize the values in the voxel patch
plt.figure(figsize=(6, 6))
plt.imshow(voxel_patch[:, :, patch_size // 2], cmap='bone', interpolation='nearest')
plt.title('3x3x3 Voxel Patch')
plt.colorbar()
plt.show()


# ANSWER

# As seen in the last lab there a few ways to handle the range of intensities so as to display it as an image. By default matplotlib normalizes them  when you use the `imshow` function. 
# For a particular slice try the following methods
# 
# **METHOD 1**: Naive Method
# Divide the pixels values by 255 and use `np.clip` to display this image with `matplotlib`
# 
# As seen in the last lab this method as the name suggests is a 'Naive' way and can lead to loss in information
# 

# In[117]:


import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np


#     img = ds.pixel_array / MAXVAL
#     pixel_array_normalized = np.clip(img,MINVAL, MAXVAL) 

# Load the NIfTI image
nifti_image = nib.load('sample_MRI.nii.gz')
image_data = nifti_image.get_fdata()

image_data_m1=image_data / 255

# Divide pixel values by 255 and clip to the [0, 1] range
normalized_image = np.clip(image_data_m1, 0, 255)

# Display the middle slice of the 3D volume
plt.imshow(normalized_image[:, :, normalized_image.shape[2] // 2], cmap='bone')
plt.title('Normalized MRI Image (0-1)')
plt.colorbar()
plt.show()


# **METHOD 2**: Min-Max Normalization
# 
# Do the min-max normalization for the whole image and visualize one slice. Also plot the colorbar and comment on what you observe

# In[119]:


image_data.shape


# In[124]:


min_val = np.min(image_data)
max_val = np.max(image_data)
print(f'min value and max value:',min_val, max_val)

# Divide pixel values by 255 and clip to the [0, 1] range
image_data_normalized = (image_data - min_val) / (max_val - min_val)*255


# Display the middle slice of the 3D volume
plt.imshow(image_data_normalized[:, :, image_data_normalized.shape[2] // 2], cmap='bone')
plt.title('Normalized MRI Image (min-max)')
plt.colorbar()
plt.show()


# I observed after min max scaling the max value dosent going till 255 it only gives 120 and there is no scaling facror is being used in metadata. I do not why is not reach 255?? but I assume Outliers: Outliers or extreme values in the original data can affect the scaling process. If there are very low or very high values in the original data, they can dominate the scaling, causing the majority of the data to be compressed into a narrower range.

# Comment

# **METHOD 3**: Windowing
# 
# Get the max and min intensities of the whole 3D image. Select a window center and width of your choice and apply the method to a slice of the image and visualize it (plot the colorbar too)
# 
# The main observation is that we can use windowing method to highlight some intensities of choice if it is priorly known what some structures might look like in the scans.
# 
# You can plot the profile to compare the actual slice and the same slice after windowing. Comment on the graph of their intensities

# In[145]:


image_data = nifti_image.get_fdata()
# WindowWidth......: 6083
# WindowCenter......: 3041

window_center = 3041
window_width =  6083 

# Apply windowing
lower_intensity = window_center - window_width / 2
upper_intensity = window_center + window_width / 2
windowed_image = np.clip((image_data - lower_intensity) / (upper_intensity - lower_intensity), 0, 1)


slice_index = 140

# Plot the slice with windowing
plt.imshow(windowed_image[:, :, slice_index], cmap='bone', vmin=0, vmax=1)
plt.title('Windowed MRI Slice_windowing')
plt.colorbar()
plt.show()


actual_slice = image_data[:, :, slice_index]

# Plot the intensity profiles of the actual slice and windowed slice
plt.figure(figsize=(10, 6))
plt.plot(actual_slice[slice_index, :], label='Actual Slice', color='blue')
plt.plot(windowed_image[:, :, slice_index][slice_index, :], label='Windowed Slice', color='red')
plt.xlabel('Pixel Position')
plt.ylabel('Intensity')
plt.title('Intensity Profiles of Actual and Windowed Slices')
plt.legend()
plt.grid(True)
plt.show()


# Comment

# **Further exploration**: Try the same for a different window center and width (either with the same view or you can change it - your choice). Comment on if you observe any changes

# In[146]:


image_data = nifti_image.get_fdata()
# WindowWidth......: 6083
# WindowCenter......: 3041

window_center = 4000
window_width =  6500 

# Apply windowing
lower_intensity = window_center - window_width / 2
upper_intensity = window_center + window_width / 2
windowed_image = np.clip((image_data - lower_intensity) / (upper_intensity - lower_intensity), 0, 1)


slice_index = 140

# Plot the slice with windowing
plt.imshow(windowed_image[:, :, slice_index], cmap='bone', vmin=0, vmax=1)
plt.title('Windowed MRI Slice_windowing')
plt.colorbar()
plt.show()


actual_slice = image_data[:, :, slice_index]

# Plot the intensity profiles of the actual slice and windowed slice
plt.figure(figsize=(10, 6))
plt.plot(actual_slice[slice_index, :], label='Actual Slice', color='blue')
plt.plot(windowed_image[:, :, slice_index][slice_index, :], label='Windowed Slice', color='red')
plt.xlabel('Pixel Position')
plt.ylabel('Intensity')
plt.title('Intensity Profiles of Actual and Windowed Slices')
plt.legend()
plt.grid(True)
plt.show()


# Comment

# ### Display multiple slices
# 
# This is a simple python code exercise. 
# 
# Write a code to display any 3 consecutive slices (closer to the center) from the 3 views as a grid using `matplotlib` and use `subplots` to display the slices in a grid with the colorbar. (You can use either Method 2 or 3 for the normalization)

# In[148]:


import matplotlib.pyplot as plt
import numpy as np


central_slice = nifti_image.shape[2] // 2
num_slices = 3

fig, axs = plt.subplots(3, num_slices, figsize=(15, 5))

# Labels for the views
view_labels = ['Sagittal View', 'Coronal View', 'Axial View']

# Loop through the views
for view_idx, view_name in enumerate(view_labels):
    for i in range(num_slices):
       
        slice_index = central_slice - num_slices // 2 + i
        
        if view_idx == 0: 
            slice_data = np.rot90(windowed_image[slice_index, :, :])
        elif view_idx == 1:
            slice_data = np.rot90(windowed_image[:, slice_index, :])
        else:  # Axial View
            slice_data = windowed_image[:, :, slice_index]

        
        ax = axs[view_idx, i]
        im = ax.imshow(slice_data, cmap='bone', vmin=0, vmax=1)
        ax.axis('off')
        ax.set_title(f'{view_name}\nSlice {slice_index}')

        cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

# Set a common title for the entire grid
fig.suptitle('3 Consecutive Slices in Sagittal, Coronal, and Axial Views', fontsize=16)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.show()


# ## Other References
# 
# 1. Nilearn: is another library that has more functions for plotting and ML tools (using scikit-learn) to work with biomedical images (https://nilearn.github.io/stable/index.html)
# 2. https://neuraldatascience.io/8-mri/read_viz.html (Some notes for both DICOM and NIfTI)
# 3. Some basic idea of MRI: https://www.weizmann.ac.il/chembiophys/assaf_tal/sites/chemphys.assaf_tal/files/uploads/MRI2021/Lecture%202%20-%20MRI%20As%20a%20Black%20Box.pdf
# 4. https://imagej.net/software/fiji/downloads#installation Is a tool you can use to view the image
