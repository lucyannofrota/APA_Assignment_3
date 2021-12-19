import torch
import torch.nn as nn
import random

class DQN(nn.Module):

    def __init__(self, inputs, outputs,dfactor,device,n_layers):
        super(DQN, self).__init__()
        
        self.input_size=inputs;
        self.output_size=outputs;
        self.discount_factor=dfactor;
        self.device=device
        
        if(n_layers == 0):
            self.layers = nn.Sequential(
                nn.Linear(in_features=self.input_size, out_features=512),
                nn.ReLU(),
                nn.Linear(in_features=512, out_features=self.output_size)
            )
        elif(n_layers == 1):
            self.layers = nn.Sequential(
                nn.Linear(in_features=self.input_size, out_features=512),
                nn.ReLU(),
                nn.Linear(in_features=512, out_features=256),
                nn.ReLU(),
                nn.Linear(in_features=256, out_features=self.output_size)
            )
        elif(n_layers == 3):
            self.layers = nn.Sequential(
                nn.Linear(in_features=self.input_size, out_features=512),
                nn.ReLU(),
                nn.Linear(in_features=512, out_features=256),
                nn.ReLU(),
                nn.Linear(in_features=256, out_features=128),
                nn.ReLU(),
                nn.Linear(in_features=128, out_features=64),
                nn.ReLU(),
                nn.Linear(in_features=64, out_features=self.output_size)
            )
        elif(n_layers == 5):
            self.layers = nn.Sequential(
                nn.Linear(in_features=self.input_size, out_features=512),
                nn.ReLU(),
                nn.Linear(in_features=512, out_features=256),
                nn.ReLU(),
                nn.Linear(in_features=256, out_features=128),
                nn.ReLU(),
                nn.Linear(in_features=128, out_features=64),
                nn.ReLU(),
                nn.Linear(in_features=64, out_features=32),
                nn.ReLU(),
                nn.Linear(in_features=32, out_features=16),
                nn.ReLU(),
                nn.Linear(in_features=16, out_features=self.output_size)
            )
        else:
            raise Exception("Invalid number of layers [1,3,5]")

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

class DDQN(nn.Module):

    def __init__(self, inputs, outputs,dfactor,device,n_layers):
        super(DDQN, self).__init__()
        
        self.input_size=inputs;
        self.output_size=outputs;
        self.discount_factor=dfactor;
        self.device=device
        
        if(n_layers == 1):
            self.layers = nn.Sequential(
                nn.Linear(in_features=self.input_size, out_features=512),
                nn.ReLU(),
                nn.Linear(in_features=512, out_features=256),
                nn.ReLU(),
                nn.Linear(in_features=256, out_features=self.output_size)
            )
        elif(n_layers == 3):
            self.layers = nn.Sequential(
                nn.Linear(in_features=self.input_size, out_features=512),
                nn.ReLU(),
                nn.Linear(in_features=512, out_features=256),
                nn.ReLU(),
                nn.Linear(in_features=256, out_features=128),
                nn.ReLU(),
                nn.Linear(in_features=128, out_features=64),
                nn.ReLU(),
                nn.Linear(in_features=64, out_features=self.output_size)
            )
        elif(n_layers == 5):
            self.layers = nn.Sequential(
                nn.Linear(in_features=self.input_size, out_features=512),
                nn.ReLU(),
                nn.Linear(in_features=512, out_features=256),
                nn.ReLU(),
                nn.Linear(in_features=256, out_features=128),
                nn.ReLU(),
                nn.Linear(in_features=128, out_features=64),
                nn.ReLU(),
                nn.Linear(in_features=64, out_features=32),
                nn.ReLU(),
                nn.Linear(in_features=32, out_features=16),
                nn.ReLU(),
                nn.Linear(in_features=16, out_features=self.output_size)
            )
        else:
            raise Exception("Invalid number of layers [1,3,5]")

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


 


def archs(arch_name,inputs,n_actions,discount_factor,device,n_layers):
    policy_net = DQN(inputs, n_actions,discount_factor,device,n_layers).to(device)
    target_net = DQN(inputs, n_actions,discount_factor,device,n_layers).to(device)
    return policy_net, target_net