import numpy as np
import scipy
from scipy import stats


class ProjectOne:
    def __init__(self, mang1, mang2):
        self.mang1 = mang1
        self.mang2 = mang2


    def gia_tri_tb(self):
        tong1 = 0
        tong2 = 0
        for i in self.mang1:
            tong1 += i
        for i in self.mang2:
            tong2 += i

        return tong1/len(self.mang1), tong2/len(self.mang2)

    def mode(self):
        mode1 = max(set(self.mang1), key=self.mang1.count)
        mode2 = max(set(self.mang2), key=self.mang2.count)
        return mode1, mode2

    def phuong_sai(self):
        y1 = 0
        y2 = 0
        for i in self.mang1:
            y1 += (i - self.gia_tri_tb()[0])**2
        for i in self.mang2:
            y2 += (i - self.gia_tri_tb()[1])**2
        return y1/len(self.mang1), y2/len(self.mang2)

    def doLechChuan(phuong_sai):
        return np.sqrt(phuong_sai)
PJ = ProjectOne([1,2,2,2,3,4],[2,3,4,4,4,4,2,5])
print(PJ.phuong_sai())     