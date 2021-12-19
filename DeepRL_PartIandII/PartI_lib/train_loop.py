import gym
import torch
import copy
import numpy as np


def train_loop(policy_net, target_net, env, device, TotalEpisodes, FreezeCounter, SaveAtCounter, createMovie, MaxSteps, exploration_threshold, exploration_decay, exploration_threshold_min, buffer, trainModel,file_path):
  loss_val,scores, episodes,events, avg_scores,avg_scores20,exploration,avg_scores100 = [],[],[],[],[],[],[],[]

  bestScore=-99999;
  bestNet=copy.deepcopy(policy_net);
  fx=0
  for f in range(TotalEpisodes):
      done  = False
      score = 0.0
      state = torch.Tensor(env.reset()).to(device)
      if f % FreezeCounter == 0:
        print(str(f)+" of "+str(TotalEpisodes))
        target_net.load_state_dict(policy_net.state_dict())

      if f % SaveAtCounter == 0:
        if(f != 0):
          createMovie(policy_net,file_path,"/Checkpoints/v2CartPole_"+str(f))
          torch.save(policy_net.state_dict(), file_path+"/Checkpoints/v2CartPole_"+str(f)+'/model.ckpt')

      for F in range(MaxSteps):
          action = policy_net.getPolicy(state,exploration_threshold)
          new_state, reward, done, _ = env.step(action.item())

          new_state=torch.Tensor(new_state).to(device);
          score += reward
          if(F<(MaxSteps-1)):  # avoid adding the last "good" example as done
              buffer.store_tuples(state, action, reward, new_state, done)
          state = new_state
          trainModel()
          if(done):
              break        
      exploration_threshold= exploration_threshold-exploration_decay if exploration_threshold > exploration_threshold_min else exploration_threshold_min

      
      #log results
      exploration.append(exploration_threshold)
      scores.append(score)
      episodes.append(f)
      events.append(F)
      avg_scores.append(score/F)
      avg_scores20.append(np.mean(scores[-20:]))

      if(score>=bestScore):
          print(score,F+1,np.mean(scores[-20:]))
          bestScore=score;
          fx=f;
          bestNet=copy.deepcopy(policy_net);
      if(avg_scores20[-1] >= 400 or avg_scores100[-1] >= 200):
        break
  torch.save(bestNet.state_dict(), file_path+"/BestCartPole"+str(fx)+'_'+str(bestScore)+'_model.ckpt')
  return bestNet, episodes, scores, events, avg_scores, avg_scores20, exploration, avg_scores100