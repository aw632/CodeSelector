class Clusterer:
    """Clusterer is a heuristic clustering algorithm that uses no embeddings.

    It performs the following steps:
    1. Initialize by letting each repository be its own cluster.
    2. In each cluster, split by filetype.
    3.

    """

    def __init__(self, path_to_dataset):
        self.dataset = self.load_from_path(path_to_dataset)

    def load_from_path(self, path):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
