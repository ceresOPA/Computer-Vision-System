
import argparse
import matplotlib.pyplot as plt

from colorization.colorizers import *

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input', type=str, default='imgs/ansel_adams3.jpg')
parser.add_argument('--use_gpu', action='store_true', help='whether to use GPU')
parser.add_argument('--output',type=str,default='C:/Users/YL/Desktop/OldPhotoRectify/server/output')
opt = parser.parse_args()

# load colorizers
colorizer_eccv16 = eccv16(pretrained=True).eval()
colorizer_siggraph17 = siggraph17(pretrained=True).eval()
if(opt.use_gpu):
	colorizer_eccv16.cuda()
	colorizer_siggraph17.cuda()

# default size to process images is 256x256
# grab L channel in both original ("orig") and resized ("rs") resolutions
img = load_img(opt.input)
(tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
if(opt.use_gpu):
	tens_l_rs = tens_l_rs.cuda()

# colorizer outputs 256x256 ab map
# resize and concatenate to original L channel
img_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig),dim=1))
out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

img_name = opt.input.split('/')[-1]

plt.imsave(f'{opt.output}/eccv16_{img_name}', out_img_eccv16)
plt.imsave(f'{opt.output}/sig_{img_name}', out_img_siggraph17)

