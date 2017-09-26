#!/usr/bin/env python
# coding=UTF-8
import os

from django.template import loader
from django.http import HttpResponse
import pandas as pd
from clarifai.rest import ClarifaiApp
from config.configuration import data_path, clarifai_api_key, test_set_id, clarifai_model_name, test_concept
from khclarifai.khclarifai_predict import get_prediction_confidence, floored_percentage


def index(request):
    """Index view"""
    template = loader.get_template('khclarifai/index.html')
    context = {
    }
    return HttpResponse(template.render(context=context, request=request))


def demo(request):
    """Demo view (runs prediction)"""
    app = ClarifaiApp(api_key=clarifai_api_key)
    model = app.models.get(clarifai_model_name)
    template = loader.get_template('khclarifai/demo.html')
    lines = pd.read_csv(os.path.join(data_path, "images/test%s/predict.csv" % test_set_id), header=0, delimiter=",")
    print(lines.columns)
    results = []
    for filename, concept in zip(lines['filename'], lines['tag1']):
        image_path = "images/test%s/%s" % (test_set_id, filename)
        pred_conf = floored_percentage(get_prediction_confidence(model, image_path), 2)
        results.append({'image_path': image_path, 'prediction_confidence': pred_conf, 'concept': concept})
    context = {
        'results': results,
        'concept': test_concept,
    }
    return HttpResponse(template.render(context=context, request=request))
