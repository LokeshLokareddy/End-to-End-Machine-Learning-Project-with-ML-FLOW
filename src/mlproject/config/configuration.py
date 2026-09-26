from mlproject.constants import *
from mlproject.utils.common import read_yaml, create_directories
from mlproject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig)

class ConfigurationManager:
    def __init__(
            self,
            config_filepath: Path = CONFIG_FILE_PATH,
            params_filepath: Path = PARAMS_FILE_PATH,
            schema_filepath: Path = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([Path(config.root_dir)])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config


    def get_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation
    
            data_validation_config = DataValidationConfig(
                root_dir=Path(config.root_dir),
                unzip_data_dir=Path(config.unzip_data_dir),
                STATUS_FILE=Path(config.STATUS_FILE),
                all_schema=self.schema.COLUMNS
            )
    
            return data_validation_config