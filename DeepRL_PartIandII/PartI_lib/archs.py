import torch
import torch.nn as nn
import random

class DQN(nn.Module):

    def __init__(self, inputs, outputs,dfactor,device):
        super(DQN, self).__init__()
        
        self.input_size=inputs;
        self.output_size=outputs;
        self.discount_factor=dfactor;
        self.device=device
        
        self.layers = nn.Sequential(
            nn.Linear(in_features=self.input_size, out_features=128),
            # nn.Linear(in_features=128, out_features=256),
            # nn.Linear(in_features=256, out_features=512),
            # nn.Linear(in_features=512, out_features=256),
            nn.Linear(in_features=128, out_features=self.output_size)
        )


    # Called with either one element to determine next action, or a batch
    # during optimization. Returns tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        return self.layers(x)

    def policy(self,state):
       with torch.no_grad():
            return self.__call__(state).argmax()
     
    def getPolicy(self,state,eps_threshold):
        sample = random.random()
        if sample > eps_threshold:
            with torch.no_grad():
 
                return self.__call__(state).argmax()
        else:
            return  torch.tensor([[random.randrange(self.output_size)]], device=self.device, dtype=torch.long)



 


def archs(arch_name,inputs,n_actions,discount_factor,device):
    policy_net = DQN(inputs, n_actions,discount_factor,device).to(device)
    target_net = DQN(inputs, n_actions,discount_factor,device).to(device)
    return policy_net, target_net