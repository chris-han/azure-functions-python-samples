import logging

import azure.functions as func


def main(event: func.EventHubEvent,cosmoDocument:func.Out[func.Document]):
    logging.info('Python EventHub2Cosmo trigger processed an event: %s', event.get_body().decode('utf-8'))

    try:
        # Get Blog feeds

        outdata = event.get_body().decode('utf-8').strip('[').strip(']') # remove the extra charactors by EventHub
        logging.info('outdata: %s', outdata)  # for debug

        # Store output data using Cosmos DB output binding
        cosmoDocument.set(func.Document.from_json(outdata))

    except Exception as e:
        logging.error('Error:')
        logging.error(e)
