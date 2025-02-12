from PIL import Image
import numpy as np
from utils import Vocabulary
import json
import data

class CocoDataset(data.Dataset):

    def __init__(self, root, anns, vocab, mode='train', transform=None):

        self.root = root
        with open(anns) as f:
            self.anns = json.load(f)
        self.vocab = Vocabulary.from_file(vocab)
        self.transform = transform

        self.data = [ann for ann in self.anns if ann['split'] == mode]

    def __getitem__(self, index):
        data = self.data
        vocab = self.vocab
        # load image