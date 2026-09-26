import os
from mlproject import logger
from mlproject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

        # Create data validation directory
        os.makedirs(self.config.root_dir, exist_ok=True)

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            # Read the dataset
            data = pd.read_csv(self.config.unzip_data_dir)

            # Get columns from dataset
            all_cols = list(data.columns)

            # Get columns from schema
            all_schema = self.config.all_schema.keys()

            # Validate every column
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False

                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")

                else:
                    validation_status = True

                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e