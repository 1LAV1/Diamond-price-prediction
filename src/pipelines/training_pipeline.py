import pandas as pd 
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from logger import logging
from components.data_ingestion  import DataIngestion


import sys
import os
if __name__ =="__main__" :
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)


