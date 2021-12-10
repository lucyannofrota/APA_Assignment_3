import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
def plot_performance(episodes, scores, events, avg_scores, avg_scores20, exploration):
    figure(figsize=(12, 6), dpi=80)
    plt.plot(episodes, scores)
    plt.plot(episodes, events)
    plt.plot(episodes, avg_scores)
    plt.plot(episodes, avg_scores100)
    plt.plot(episodes, exploration)
    plt.xlabel('episodes')
    plt.ylabel('y axis label')
    plt.title('Report')
    plt.legend(['scores',  'events', 'avg_scores', 'avg_scores100','exploration'])
    plt.show()