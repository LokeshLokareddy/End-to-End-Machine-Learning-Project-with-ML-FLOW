import os
from box.exceptions import BoxValueError
import yaml
from mlproject.logger import logger
import json
import jsonlib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def get_config(config_path: Path) -> ConfigBox:
    try:
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {config_path} loaded successfully")
            return ConfigBox(config)
    except Exception as e:
        logger.error(f"Error occurred while loading yaml file: {config_path}")
        raise BoxValueError(f"Error occurred while loading yaml file: {config_path}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: Any):
    with open(path, "w") as f:
        json.dump(data, f, indent=4) 

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"