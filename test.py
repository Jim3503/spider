'''
Author: Jim3503 jiming1920@mails.jlu.edu.cn
Date: 2024-08-20 18:20:50
LastEditors: Jim3503 jiming1920@mails.jlu.edu.cn
LastEditTime: 2024-08-21 13:29:38
FilePath: \spider\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))
print(torch.cuda.get_device_capability(0))