import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import json

def performance_evaluation(arch,episodes, scores, events, avg_scores, avg_scores20, exploration):
    report(arch,episodes, scores, events, avg_scores, avg_scores20, exploration)
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

def report(arch,episodes, scores, events, avg_scores, avg_scores20, exploration):

    mod = {}
    mod['episodes'] = episodes
    mod['episodes'] = episodes

    # print(self.loss_log)

    mod['Total Training Time'] = sum([i[3] for i in self.loss_log])
    filePath = self.report_path+'/data.json'

    with open(filePath, 'w') as outfile:
        json.dump(mod, outfile)
    return