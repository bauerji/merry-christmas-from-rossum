"""
This custom function example can be used for showing custom messages to the
user on the validation screen or for updating values of specific fields.
(annotation_content event and user_update action which provides annotation
content tree as an input). The function below shows how to:
1. Display a warning message to the user if "item_amount_base" field of
a line item exceeds a predefined threshold
2. Removes all dashes from the "document_id" field

item_amount_base and document_id should be fields defined in a schema.

You can use some external libraries in your custom functions. List of supported
libraries can be found at https://api.elis.rossum.ai/docs/#third-party-libraries

More about custom functions - https://developers.rossum.ai/docs/how-to-use-serverless-functions
"""

# it is possible to import modules from standard Python library

from urllib import request
import json


def rossum_hook_request_handler(payload):
    address = ""
    local_address = ""
    text = ""

    for datapoint in payload.get("annotation", {}).get("content", []):
        if children := datapoint.get("children"):
            for child in children:
                print(child["schema_id"], child.get("content", {}).get("value"))
                if child["schema_id"] == "address":
                    address = child["content"]["value"]
                if child["schema_id"] == "local_address":
                    local_address = child["content"]["value"]
                if child["schema_id"] == "text":
                    text = child["content"]["value"]

    if address and local_address and text:
        data = {"local_address": local_address, "text": text}
        req = request.Request(address, data=json.dumps(data).encode(), headers={"content-type": "application/json"})
        response = request.urlopen(req)

    return {"messages": [{"content": f"I've been here! {address}, {local_address}, {text}", "type": "info"}]}
