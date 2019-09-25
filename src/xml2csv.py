import os
import glob
from pathlib import Path

import pandas as pd
import xml.etree.ElementTree as ET


class Xml2Csv(object):
    @classmethod
    def _xml_to_csv(cls, path):
        xml_list = []
        tree = ET.parse(path)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
        column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_df = pd.DataFrame(xml_list, columns=column_name)
        return xml_df

    @classmethod
    def train(cls):
        root_path = Path(os.getcwd())
        root_link = root_path.parent
        ls_file = os.listdir(os.path.join(root_link, 'xmls'))
        for file in ls_file:
            if '.xml' in file:
                image_path = os.path.join(root_link, 'xmls/{}'.format(file))
                xml_df = cls._xml_to_csv(image_path)
                # Storing the csv file into the csvs directory.
                xml_df.to_csv(os.path.join(root_link, 'csvs/{}.csv'.format(os.path.splitext(file)[0])))
                print('Successfully converted xml to csv.')
