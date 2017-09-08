
# coding: utf-8

# In[1]:

li=[1,2,3,4,5]


# In[2]:

#for 문으로 target 찾기
# 선형 탐색
# linear search
def linear_search(data, target):
    '''
    data에서 target의 인덱스
    '''
    for e in data:
        if target == e:
            return data.index(e)
    return None


# In[10]:

idx = linear_search(li,7)
if idx:
    print(idx)
else:
    print('no such data')


# In[6]:

#같은 인터페이스를 가지는데 성능이 훨씬 좋은 알고리즘
#이진 탐색
#binary search
def binary_search(data, target):
    '''
    data에서 target의 인덱스
    target이 없다면 None
    '''
    start=0
    end=len(data)-1
    while start <= end:
        mid=(start + end) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            end=mid -1 
        else:
            start = mid + 1
    return None


# In[9]:

idx = binary_search(li,4)
if idx:
    print(idx)
else:
    print('no such data')

