#!/usr/bin/env python
# coding=UTF-8
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import pandas as pd
from config.configuration import data_path, clarifai_api_key, test_set_id, concept_column, test_concept, clarifai_model_name


if __name__ == '__main__':
    train_file_path = os.path.join(data_path, "images/test%s/train.csv" % test_set_id)
    app = ClarifaiApp(api_key=clarifai_api_key)
    lines = pd.read_csv(train_file_path, header=0, delimiter=",")
    results = []
    for filename, concept in zip(lines['filename'], lines[concept_column]):
        print "Processing: %s" % filename
        img = None
        image_path = os.path.join(data_path, "images/test%s/%s" % (test_set_id, filename))
        if concept == test_concept:
            img = ClImage(filename=image_path, concepts=[test_concept])
        else:
            img = ClImage(filename=image_path, not_concepts=[test_concept])
        app.inputs.create_image(img)
    model = app.models.create(model_id=clarifai_model_name, concepts=[test_concept])
    model.train()
    print "Model created: %s" % clarifai_model_name
