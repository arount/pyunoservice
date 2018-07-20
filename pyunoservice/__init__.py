#!/usr/env/bin python3

import requests

class FileWrongTypeException(Exception):
    pass


class UnoService(object):
    '''
    Simple wrapper for Uno Service
    '''

    def __init__(self, host='localhost', port='3000', protocol='http'):
        self.protocol = protocol
        self.host = host
        self.port = port


    @property
    def uri(self):
        return '{s}://{h}:{p}/convert'.format(
            s=self.protocol,
            h=self.host,
            p=self.port
        )


    def info(self, input_file_or_path):
        '''
        Call /info (GET)
        '''
        if isinstance(input_file_or_path, str):
            input_file_or_path = open(input_file_or_path, 'rb')

        response = requests.get(self.uri, files={"file": input_file_or_path})
        return response.text


    def convert(self, input_file_or_path, output_file_or_path):
        '''
        Call /convert (POST)
        Output will be saved in `output_file_or_path`
        Raise a FileWrongTypeException if file cannot be converted
        '''
        if isinstance(input_file_or_path, str):
            input_file_or_path = open(input_file_or_path, 'rb')
        if isinstance(output_file_or_path, str):
            output_file_or_path = open(output_file_or_path, 'wb')

        response = requests.post(self.uri, files={"file": input_file_or_path}, stream=True)

        if response.text == 'Cannot open this document':
            raise FileWrongTypeException('Cannot open this document')

        for chunk in response:
            output_file_or_path.write(chunk)

        return output_file_or_path

