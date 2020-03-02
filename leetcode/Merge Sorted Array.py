# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:10:15 2019

@author: Administrator
"""
"""合并两个有序数组 Merge Sorted Array
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]"""
"""solution 1:双指针"""   """指针还是很重要的，循环遍历很难处理"""
def merge(nums1,m,nums2,n):
    nums1_copy=nums1[:m]
    nums1[:]=[]
    p1=0
    p2=0
    while p1<m and p2<n:
        if nums1_copy[p1]<nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1+=1
        else:
            nums1.append(nums2[p2])
            p2+=1
    if p1<m:
        nums1[p1+p2:]=nums1_copy[p1:]
    if p2<n:
        nums1[p1+p2:]=nums2[p2:]
    return nums1

print(merge([1,2,3,0,0,0],3,[2,4,5,6,],4))

"""solution2:先合并再排序"""
def merge2(nums1,m,nums2,n):
    nums1[:] = sorted(nums1[:m] + nums2)
        