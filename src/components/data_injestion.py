import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass #helps to create simple classes meant to hold data w/o having to manually write an __init__()
class DataIngestionConfig: #It defines where data files will be stored 
    train_data_path = str = os.path.join('artifacts',"train.csv")
    test_data_path = str = os.path.join('artifacts',"test.csv")
    raw_data_path = str = os.path.join('artifacts',"data.csv")


#It is used to autonmate the first step of ml project-> collecting,saving and preparing raw data for training
class DataIngestion: #Imagine this as a delivery worker who gets the address info(DataIngestionConifg) of where to pick up and drop off data
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    #here the actual work happens
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('notebook\data\stud.csv') #Reads the file
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #extracts a folder called artifacts and if doesnt exists creates one

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) #saves the raw data into artifacts/data.csv
            
            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            #The delivery man(DataIngestion) delivers
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Injestion of the data is completed")

            return(
                #returns the file paths so the next stage can use them
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)








