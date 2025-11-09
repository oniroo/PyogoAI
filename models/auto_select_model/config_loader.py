r"""YAML 읽기"""
import yaml

def load_config(path=r"C:\Users\pc\PycharmProjects\PyogoAI\configs\model.yml"):
    """YAML 설정 파일 읽어서 Python dict로 반환하는 함수"""
    with open(path) as f:
        return yaml.safe_load(f)