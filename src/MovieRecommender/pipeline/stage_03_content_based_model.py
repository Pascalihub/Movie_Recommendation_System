from MovieRecommender.config.configuration import ConfigurationManager
from MovieRecommender.components.content_based_model import ContentBasedModel
from MovieRecommender.logger import logging

STAGE_NAME = "Content Based Model Training"


class ContentBasedModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        content_based_model_config = config.get_content_based_model_config()
        content_based_model = ContentBasedModel(
                                    config=content_based_model_config)
        content_based_model.load_data_from_db()
        content_based_model.process_data()
        content_based_model.save_similarity_matrix() 

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ContentBasedModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e
 

