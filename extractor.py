"""
Lighthouse generates HTML reports. 
The accessibility reports are under <div id = "accessibility">
Inside this div, we want to grab:
 - <div class = "lh-gauge_percentage">  |  contains accessiblity score/100 
 - <div class = "lh-clump--failed">
 - <div class = "lh-audit-group">

Start with grabbing this stuff first, seeing what it gives us, and narrowing it down from there. 
"""

from bs4 import BeautifulSoup
import os
import pandas as pd

class Extractor:
    @staticmethod
    def read_html(file_directory):
        soup = BeautifulSoup(file_directory, 'html.parser')
        for item in soup.find(id="accessibility"):
            # more stuff here