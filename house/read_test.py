# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:37:10 2019

@author: admin01
"""

# read readline readlines

# =============================================================================
# with open("D:/d/test.txt") as f:
#     print(f.read())
#     
# with open("D:/d/test.txt") as f:
#     
#     print("***")
#     print(f.readlines())
# 
# 
# 
# with open("D:/d/test.txt") as f:
# 
#     print("&&&&&&&")
#     while True:
#         data = f.readline()
#         if not data:
#             break
#         print(data),
# =============================================================================
def read_in_lines(filepath, line_num = 50):
    lines = []
    i = 1
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline() #逐行读取
            if not line:        #读到空时跳出？？中间空行？？
                break
            lines.append(line)  # 一定数量后再写入，而非逐行写入
            if i >= line_num:
# =============================================================================
#                 for line in lines:
#                     print(line)
# =============================================================================
                yield lines
                i = 0
                lines = []
            i += 1
    if lines:       # break跳出读取时，lines里面可能还有部分数据
# =============================================================================
#         for line in lines:
#             print(line)
# =============================================================================
        yield lines
        
# yield ,按字节读取
        
def read_in_chunks(filepath, chunk_size = 1024):
    with open(filepath, "r", encoding="utf-8") as f:
        
        while True:
            data = f.read(chunk_size) #1024byte 1kb
            if data:
                yield data
            else:
                return # return也可用来跳出循环
            
# =============================================================================
# for item in read_in_chunks("D:/d/test.csv"):
#     print(item)
# =============================================================================

for item in read_in_lines("D:/d/test.csv"):
    f = open("D:/d/testread.txt","w", encoding="utf-8")
    f.writelines(item)
    f.close()
#    print(item)      
    
