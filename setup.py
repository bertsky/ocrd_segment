# -*- coding: utf-8 -*-
"""
Installs:

    - maskrcnn-address
    - maskrcnn-formdata
    - maskrcnn-publaynet
    - maskrcnn-run
    - ocrd-segment-repair
    - ocrd-segment-from-masks
    - ocrd-segment-from-coco
    - ocrd-segment-extract-pages
    - ocrd-segment-extract-regions
    - ocrd-segment-extract-lines
    - ocrd-segment-replace-original
    - ocrd-segment-replace-page
    - ocrd-segment-evaluate
    - ocrd-segment-extract-address
    - ocrd-segment-extract-formdata
    - ocrd-segment-classify-address-text
    - ocrd-segment-classify-address-layout
"""
import codecs

import json
from setuptools import setup, find_packages

with open('./ocrd-tool.json', 'r') as f:
    version = json.load(f)['version']
    
setup(
    name='ocrd_segment',
    version=version,
    description='Page segmentation and segmentation evaluation',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Konstantin Baierer, Kay-Michael Würzner, Robert Sachunsky',
    author_email='unixprog@gmail.com, wuerzner@gmail.com, sachunsky@informatik.uni-leipzig.de',
    url='https://github.com/OCR-D/ocrd_segment',
    license='Apache License 2.0',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=open('requirements.txt').read().split('\n'),
    package_data={
        '': ['*.json', '*.yml', '*.yaml'],
    },
    entry_points={
        'console_scripts': [
            'maskrcnn-address=maskrcnn_cli.address:main',
            'maskrcnn-formdata=maskrcnn_cli.formdata:main',
            'maskrcnn-publaynet=maskrcnn_cli.publaynet:main',
            'maskrcnn-run=maskrcnn_cli.run:cli',
            'ocrd-segment-repair=ocrd_segment.cli:ocrd_segment_repair',
            'ocrd-segment-from-masks=ocrd_segment.cli:ocrd_segment_from_masks',
            'ocrd-segment-from-coco=ocrd_segment.cli:ocrd_segment_from_coco',
            'ocrd-segment-extract-pages=ocrd_segment.cli:ocrd_segment_extract_pages',
            'ocrd-segment-extract-regions=ocrd_segment.cli:ocrd_segment_extract_regions',
            'ocrd-segment-extract-lines=ocrd_segment.cli:ocrd_segment_extract_lines',
            'ocrd-segment-replace-original=ocrd_segment.cli:ocrd_segment_replace_original',
            'ocrd-segment-replace-page=ocrd_segment.cli:ocrd_segment_replace_page',
            'ocrd-segment-evaluate=ocrd_segment.cli:ocrd_segment_evaluate',
            'ocrd-segment-extract-address=ocrd_segment.cli:ocrd_segment_extract_address',
            'ocrd-segment-extract-formdata=ocrd_segment.cli:ocrd_segment_extract_formdata',
            'ocrd-segment-classify-address-text=ocrd_segment.cli:ocrd_segment_classify_address_text',
            'ocrd-segment-classify-address-layout=ocrd_segment.cli:ocrd_segment_classify_address_layout',
        ]
    },
)
