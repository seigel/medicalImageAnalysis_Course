import nibabel as nib
from matplotlib import pyplot as plt

%matplotlib inline

def show_slices(slices):
   """ Function to display row of image slices """
   _, axes = plt.subplots(1, len(slices))
   for i, a_slice in enumerate(slices):
       axes[i].imshow(a_slice.T, cmap="gray", origin="lower")

t1_image = nib.load("/content/IXI195-HH-1620-T1_fcm.nii.gz")
t2_image = nib.load("/content/IXI195-HH-1620-T2_reg_fcm.nii.gz")

t1_image_data = t1_image.get_fdata()
t2_image_data = t2_image.get_fdata()

# Cut about half way through
t1_interesting_slice_number = int(t1_image_data.shape[2] / 2)
t2_interesting_slice_number = int(t2_image_data.shape[2] / 2)

t1_slice = t1_image_data[:, :, t1_interesting_slice_number]
t2_slice = t2_image_data[:, :, t2_interesting_slice_number]

show_slices([t1_slice, t2_slice])

plt.show()

