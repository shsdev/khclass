#!/usr/bin/env python
# coding=UTF-8
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from math import floor
from clarifai.rest import ClarifaiApp
from config.configuration import data_path, test_set_id, clarifai_api_key, clarifai_model_name


def floored_percentage(val, digits):
    """Format float value as percentage string"""
    val *= 10 ** (digits + 2)
    return '{1:.{0}f}%'.format(digits, floor(val) / 10 ** digits)


def get_prediction_confidence(model, image_path):
    """Get the first value's float prediction value"""
    print "Processing prediction for image: %s" % image_path

    full_image_path = "%s/%s" % (data_path, image_path)

    prediction_confidence = 0.0
    result = model.predict_by_filename(full_image_path)
    for o in result['outputs']:
        concept_results = o['data']['concepts']
        for concept_result in concept_results:
            print concept_result['value']
            prediction_confidence = float(concept_result['value'])
            break
    return prediction_confidence


if __name__ == '__main__':
    app = ClarifaiApp(api_key=clarifai_api_key)
    mdl = app.models.get(clarifai_model_name)
    print floored_percentage(get_prediction_confidence(mdl, "images/test%s/%s" % (test_set_id, "EMK_1303.jpg")), 2)
