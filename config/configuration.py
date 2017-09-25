#!/usr/bin/env python
# coding=UTF-8
"""
Configuration
The configuration is read from the configuratio file "settings.cfg". The
parameters below get there values from this configuration file. However,
if an environment variable is defined, it overrules the setting of the
configuration file.
"""
import os
import ConfigParser
import logging

root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

# logging configuration
logging.basicConfig(filename=os.path.join(root_dir, "khclass.log"), level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ATTENTION: Environment variables overrule config file settings in config/settings.cfg
config = ConfigParser.RawConfigParser()
config.read(os.path.join(root_dir, 'config/settings.cfg'))

# paths
_data_dir = config.get('paths', 'data_dir')
data_dir = os.getenv('DATA_DIR', _data_dir if _data_dir else "static")
data_path = os.path.join(root_dir, data_dir)

# api keys
clarifai_api_key = os.getenv('CLARIFAI_API_KEY', config.get('apikeys', 'clarifai_api_key'))

# test parameters
test_set_id = os.getenv('TEST_SET_ID', config.get('testparams', 'test_set_id'))
test_concept = os.getenv('TEST_CONCEPT', config.get('testparams', 'test_concept'))
concept_column = os.getenv('TEST_COLUMN', config.get('testparams', 'concept_column'))
_clarifai_model_prefix = os.getenv('TEST_MODEL_PREFIX', config.get('testparams', 'clarifai_model_prefix'))
clarifai_model_name = "%s%s" % (_clarifai_model_prefix, test_set_id)
