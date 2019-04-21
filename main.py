from config import test_path, test_out_path
from n_gram import NGram

if __name__ == '__main__':
    n = NGram()
    n.segment(test_path, test_out_path)