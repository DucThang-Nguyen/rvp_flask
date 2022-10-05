import os

from typing import Type, List


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-dev.db".format(basedir)


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-test.db".format(basedir)


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
