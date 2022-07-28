import os
import sys

import torch
import torch.utils.data as data

import numpy as np
from PIL import Image
import glob
import random

from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean

random.seed(835)



class ImageDataset(data.Dataset):
    
    def __init__(self, root, mode='train', size=224, unaligned=False): 
        self.unaligned=unaligned
        self.size = size #256*256
        self.files_A = sorted(glob.glob(os.path.join(root, '%s/org' %mode) + '/*.*'))
        self.files_B = sorted(glob.glob(os.path.join(root, '%s/ENF' %mode) + '/*.*'))

    def __getitem__(self, index):
        k=random.randint(0,100)       
        item_A = Image.open(self.files_A[index % len(self.files_A)])
        item_A = item_A.resize((self.size,self.size), Image.ANTIALIAS)
        item_A = ((np.asarray(item_A/225.)       
        if self.mode = train:         
        if k>50:
            item_A = np.fliplr(item_A)
        item_A = torch.from_numpy(item_A.copy()).float()    
        item_A = item_A.permute(2,0,1) #.unsqueeze(0)
        
       
          
        return {'A': item_A, 'B': item_B }

    def __len__(self):
        return min(len(self.files_A), len(self.files_B))



