

class SimpleCase(TestCase):
    def make_graph(self):
        G = nx.fast_gnp_random_graph(30, 0.2, seed=SEED)

        for node, data in G.nodes_iter(data=True):
            data['ntype'] = random.choice(NTYPES)

        for src, tgt, data in G.edges_iter(data=True):
            data['weight'] = random.random()

        return G

    def test_simple(self):
        G = self.make_graph()
        H = HivePlot(G, node_class_attribute='ntype')
        H.draw()
        H.save_plot('./output/main.pdf')
