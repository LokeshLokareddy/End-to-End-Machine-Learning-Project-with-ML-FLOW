import pandas as pd
import os
from mlproject import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlproject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        logger.info("Reading training data")
        train_df = pd.read_csv(self.config.train_data_path)
        logger.info("Reading testing data")
        test_df = pd.read_csv(self.config.test_data_path)

        logger.info("Splitting features and target variable")
        X_train = train_df.drop(columns=[self.config.target_column], axis=1)
        y_train = train_df[self.config.target_column]

        X_test = test_df.drop(columns=[self.config.target_column], axis=1)
        y_test = test_df[self.config.target_column]

        logger.info("Training the model")
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        model.fit(X_train, y_train)

        logger.info("Saving the trained model")
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(model, model_path)

        logger.info(f"Model saved at {model_path}")