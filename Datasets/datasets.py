# coding: utf-8
import torch
from PIL import Image
from torch.utils.data import Dataset
import random
import numpy as np


class MyDataset(Dataset):
    def __init__(self, txt_path, transform = None, target_transform = None, batch_size=128, class_num=1000):
        fh = open(txt_path, 'r')
        imgs = []
        for line in fh:
            line = line.rstrip()
            words = line.split(',')
            imgs.append((words[0], int(words[1])))
            self.bs = batch_size=128
            self.cn = class_num
            self.imgs = imgs 
            self.transform = transform
            self.target_transform = target_transform
    def __getitem__(self, index):
        k=random.randint(0,100) 
        fn, label = self.imgs[index]
        img = Image.open(fn).convert('RGB') 
        img = img.resize((224,224), Image.ANTIALIAS)
        img = (np.asarray(img)/255.)                 
        if k>50:
            img = np.fliplr(img)      
        img = torch.from_numpy(img.copy()).float()    
        img = img.permute(2,0,1) #.unsqueeze(0)       
               
        if self.transform is not None:
            img = self.transform(img)
        
        # label = torch.zeros(self.bs, self.cn).scatter_(1, label, 1)
        label = np.reshape(label, (1,)).astype('float32')
        # label

        
        return img, label
               
    def __len__(self):
        return len(self.imgs)