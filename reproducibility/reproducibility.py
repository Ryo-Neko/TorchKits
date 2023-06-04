import random
import numpy as np
import torch


def init_seed(seed=1234):
    """
    乱数シードを再現性のために初期化する。

    Args:
        seed (int, optional): 全てのライブラリに対する初期シード。デフォルトは1234。
    """
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def worker_init_fn(worker_id):
    """
    DataLoaderのワーカー初期化関数。
    DataLoaderの`num_workers`を指定する際に、この関数を`worker_init_fn`として使用する。

    Args:
        worker_id (int): ワーカーのID。
    """
    new_seed = np.random.get_state()[1][0] + worker_id
    np.random.seed(new_seed)
    random.seed(new_seed)
    return
