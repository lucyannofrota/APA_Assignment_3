import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import json

def performance_evaluation(episodes, scores, events, avg_scores, avg_scores20, exploration):
    figure(figsize=(12, 6), dpi=80)
    plt.plot(episodes, scores)
    plt.plot(episodes, events)
    plt.plot(episodes, avg_scores)
    plt.plot(episodes, avg_scores20)
    plt.plot(episodes, exploration)
    plt.xlabel('episodes')
    plt.ylabel('y axis label')
    plt.title('Report')
    plt.legend(['scores',  'events', 'avg_scores', 'avg_scores20','exploration'])
    plt.show()

def report(file_path,arch,BatchSize,exploration_threshold,exploration_threshold_min,exploration_decay,discount_factor,
            LearningRate,LearningRateDecay,episodes, scores, events, avg_scores, avg_scores20, exploration):

    mod = {}
    mod['arch'] = arch
    mod['batch_size'] = BatchSize
    mod['exploration_threshold'] = exploration_threshold
    mod['exploration_threshold_min'] = exploration_threshold_min
    mod['exploration_decay'] = exploration_decay
    mod['discount_factor'] = discount_factor
    mod['learning_rate'] = LearningRate
    mod['learning_rate_decay'] = LearningRateDecay
    mod['episodes'] = episodes
    mod['scores'] = scores
    mod['events'] = events
    mod['avg_scores'] = avg_scores
    mod['avg_scores20'] = avg_scores20
    mod['exploration'] = exploration

    filePath = file_path+'/data.json'

    with open(filePath, 'w') as outfile:
        json.dump(mod, outfile)
    return