import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


def graph_b(edgelist):
    g = nx.from_pandas_edgelist(edgelist, 'from_address', 'to_address', 'hop')
    nx.draw_spring(g, with_labels=True)
    plt.show()
    return g


def load(path):
    data = pd.read_csv(path)
    content = pd.DataFrame(data, columns=['from_address', 'to_address', 'hop'])
    # print(type(content))
    return content


if __name__ == '__main__':
    #graph_b(load())
    g1=graph_b(load('test_g.csv'))
    g2=graph_b(load('test_g2.csv'))
