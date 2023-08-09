""" Preload module for DeepDanbooru or onnxtagger. """
from pathlib import Path
from argparse import ArgumentParser


def preload(parser: ArgumentParser):
    """ Preload module for DeepDanbooru or onnxtagger. """
    # default deepdanbooru use different paths:
    # models/deepbooru and models/torch_deepdanbooru
    # https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/c81d440d876dfd2ab3560410f37442ef56fc6632

    parser.add_argument(
        '--deepdanbooru-projects-path',
        type=str,
        help='Path to directory with DeepDanbooru project(s).'
    )
    parser.add_argument(
        '--onnxtagger-path',
        type=str,
        help='Path to directory with Onnyx project(s).'
    )
