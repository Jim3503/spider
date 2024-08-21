'''
Author: Jim3503 jiming1920@mails.jlu.edu.cn
Date: 2024-08-20 18:20:50
LastEditors: Jim3503 jiming1920@mails.jlu.edu.cn
<<<<<<< HEAD
LastEditTime: 2024-08-21 11:25:31
=======
LastEditTime: 2024-08-21 11:05:51
>>>>>>> ec34da09d1c2aee30540c8e5e62754061a9f5c6b
FilePath: \spider\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import torch
import torch.nn as nn
import torch.optim as optim

# Define the model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        return self.fc(x)
    
# Create the model
model = Net()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Create some data
x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0], [10.0]])

# Train the model
for epoch in range(1000):
    optimizer.zero_grad()
    y_pred = model(x)
    loss = criterion(y_pred, y)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch + 1}/1000, Loss: {loss.item()}')

# Save the model
<<<<<<< HEAD
torch.save(model.state_dict(), 'model.pth')
# Load the model
=======
torch.save(model.state_dict(), 'model.pth')
>>>>>>> ec34da09d1c2aee30540c8e5e62754061a9f5c6b
