import os
import re

tree = r"""
env-control-dt/
├── configs/
│   └── default.yaml
├── env_control_dt/
│   ├── core/
│   │   ├── interfaces/
│   │   │   ├── model_interface.py
│   │   │   ├── dataset_interface.py
│   │   │   ├── controller_interface.py
│   │   └── __init__.py
│   ├── data/
│   │   ├── episode_loader.py
│   │   ├── return_calculator.py
│   │   ├── episode_dataset.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── transformer_block.py
│   │   ├── decision_transformer.py
│   │   └── __init__.py
│   ├── training/
│   │   ├── trainer.py
│   │   ├── loss.py
│   │   └── __init__.py
│   ├── control/
│   │   ├── dt_controller.py
│   │   ├── action_safety.py
│   │   └── __init__.py
│   ├── utils/
│   │   ├── seed.py
│   │   ├── config.py
│   │   └── __init__.py
│   ├── pipelines/
│   │   ├── training_pipeline.py
│   │   └── __init__.py
│   └── __init__.py
├── scripts/
│   ├── train.py
│   └── run_controller.py
└── tests/
    ├── test_dataset.py
    ├── test_model.py
    ├── test_trainer.py
    └── test_returns.py
"""

import os
import re


def create_from_tree(tree_str):
    lines = tree_str.strip().split("\n")
    path_stack = []

    for raw_line in lines:
        # 1) 장식문자를 공백으로 치환
        clean_line = re.sub(r"[│├└─]+", " ", raw_line)

        # 2) 이름 추출
        name = clean_line.strip()
        if not name:
            continue

        # 3) 들여쓰기 기반 depth 계산 (4칸 = 1 depth)
        indent = len(clean_line) - len(clean_line.lstrip(" "))
        depth = indent // 4

        # 4) 스택을 depth에 정확히 맞추기
        #    depth=0 → 스택 길이=1
        while len(path_stack) > depth:
            path_stack.pop()

        # 5) 현재 경로 계산
        if path_stack:
            current_path = os.path.join(path_stack[-1], name.rstrip("/"))
        else:
            current_path = name.rstrip("/")

        # 6) 디렉토리인지 파일인지 판단
        if name.endswith("/"):  # 디렉토리
            os.makedirs(current_path, exist_ok=True)
            path_stack.append(current_path)
        else:  # 파일
            dir_path = os.path.dirname(current_path)
            os.makedirs(dir_path, exist_ok=True)
            open(current_path, "w").close()

    print("✅ 디렉토리 및 파일 생성 완료!")


create_from_tree(tree)