'''
Author: Jim3503 jiming1920@mails.jlu.edu.cn
Date: 2024-08-20 18:20:50
LastEditors: Jim3503 jiming1920@mails.jlu.edu.cn
LastEditTime: 2024-08-21 14:15:13
FilePath: \spider\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import torch
import requests as rq
from bs4 import BeautifulSoup
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))
print(torch.cuda.get_device_capability(0))

url = input("请输入url:")
if("https" or "http") in url:
    data = rq.get(url,verify=False)
else:
    data = rq.get("https://"+url,verify=False)
soup = BeautifulSoup(data.text,"html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))
    
with open("myLinks.txt",'a') as saved:
    print(links[:10],file=saved)