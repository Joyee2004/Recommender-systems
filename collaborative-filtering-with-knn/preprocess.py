from surprise.model_selection import train_test_split
from config import TEST_SIZE
def split_data(dataset):
    return train_test_split(dataset, test_size= TEST_SIZE)