import torch
from torch import nn
class(nn.Module):
  def __init__(self, n_users):


from torch.utils.data import DataLoader
for rec_set, kg_set in tqdm(zip(DataLoader(train_set, batch_size = rec_batchSize, shuffle = True), 
                                DataLoader(kgTrainSet, batch_size = kg_batchSize, shuffle = True))):
  optimizer.zero_grad()
  loss = net(rec_set, kg_set)
                                  
