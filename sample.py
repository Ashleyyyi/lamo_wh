import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

from torch.utils.data import Dataset, DataLoader


# 完成数据集类
class MyDdataSet(Dataset):
    def __init__(self):
        self.namelist = []
        self.datalist = []
        self.labellist = []
        hdulist = fits.open('datasets/train_data_01.fits')
        for num in range(10000):
            flux = hdulist[0].data[num - 1]
            name = hdulist[1].data['objid'][num - 1]
            label = hdulist[1].data['label'][num - 1]

            self.namelist.append(str(hdulist[1].data['objid'][num - 1]))
            self.labellist.append(str(label))
            self.datalist.append(flux)

    def __getitem__(self, index):
        return self.namelist[index], self.labellist[index], self.datalist[index]

    def __len__(self):
        return len(self.namelist)


my_dataset = MyDdataSet()
data_loader = DataLoader(dataset=my_dataset, batch_size=4, shuffle=True)

# 遍历，获取每个batch的结果
if __name__ == '__main__':

    for i in data_loader:
        print(i)
        break
    print(len(data_loader))
    print(len(my_dataset))
