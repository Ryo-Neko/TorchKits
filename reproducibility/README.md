# シードの初期化ユーティリティ

このリポジトリは、再現性のために乱数シードを初期化するためのユーティリティ関数を提供します。

## 概要

このユーティリティでは、以下の関数が提供されています。

- `init_seed(seed=1234)`: 乱数シードを初期化するための関数です。再現性を確保するために、numpy、random、torchの乱数シードを設定します。
- `worker_init_fn(worker_id)`: DataLoaderのワーカー初期化関数です。`num_workers`を指定してDataLoaderを作成する際に、この関数を`worker_init_fn`引数として渡すことで、各ワーカーの乱数シードを設定します。

## 使い方

1. このリポジトリをクローンします。

```bash
git clone https://github.com/example/reproducible-seed.git
```

2. 必要なスクリプトにこのユーティリティをインポートします。
```python
Copy code
from reproducible_seed import init_seed, worker_init_fn

# シードの初期化
init_seed(seed=1234)

# DataLoaderの作成
data_loader = torch.utils.data.DataLoader(
    dataset,
    batch_size=32,
    num_workers=4,
    worker_init_fn=worker_init_fn
)
```

- `init_seed`関数を使用して、再現性のために乱数シードを初期化します。デフォルトではシード値として`1234`が使用されますが、必要に応じて変更することができます。それぞれのユーティリティはメインスクリプトの最初に読み込むのが一般的です。
- `worker_init_fn`関数を使用して、DataLoaderのワーカーごとに乱数シードを設定します。`worker_init_fn`引数としてこの関数を渡すことで、並列処理中に再現性を確保することができます。DataLoaderを定義する箇所で使用します。


## 使用例
```python
# 必要なライブラリのインポート
import numpy as np
import torch
import random
from reproducible_seed import init_seed, worker_init_fn

# 乱数シードの初期化
init_seed(seed=1234)

# データセットの準備
dataset = create_dataset()

# データローダーの作成
data_loader = torch.utils.data.DataLoader(
    dataset,
    batch_size=32,
    num_workers=4,
    worker_init_fn=worker_init_fn
)
```


## 使用した方へ
使ってくださったことをご一報いただけると金子が喜びます。