
import sys
from string import ascii_lowercase as lowercase
import networkx as nx


def generate_graph(words):
    G = nx.Graph(name="words")
    lookup = dict((c, lowercase.index(c)) for c in lowercase)

    def edit_distance_one(word):
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i + 1:]
            j = lookup[c]  # lowercase.index(c)
            for cc in lowercase[j + 1:]:
                yield left + cc + right
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G


def words_graph(n):
    """Return the words example graph from the Stanford GraphBase"""
    fh = open(str(n)+'_dat.txt', 'r')
    words = set()
    for line in fh.readlines():
        if line.startswith('*'):
            continue
        w = str(line[0:n])
        words.add(w)
    return generate_graph(words)


if __name__ == '__main__':
    wl = int(sys.argv[1])
    G = words_graph(wl)
    print("Loaded {}_dat.txt containing {} {}-letter English words."\
        .format(wl, len(G), wl))
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          % (nx.number_of_nodes(G), nx.number_of_edges(G)))
    print("%d connected components" % nx.number_connected_components(G))

    if wl == 5:
        pair_list = [('chaos', 'order'),\
                    ('nodes', 'graph'),\
                    ('moron', 'smart'),\
                    ('pound', 'marks')]
    else:
        pair_list = [('cold', 'warm'),\
                    ('love', 'hate')]

    for (source, target) in pair_list:
        print("Shortest path between %s and %s is" % (source, target))
        try:
            sp = nx.shortest_path(G,source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")
