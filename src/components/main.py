from data_ingestion import DataIngestion
from data_transformation import DataTransformation
from model_trainer import ModelTrainer


data_ingestion = DataIngestion()
data_ingestion.initiate_data_ingestion()

data_transformation = DataTransformation()
data_transformation.initiate_data_transformation()

model_trainer = ModelTrainer()
model_trainer.initiate_model_trainer()