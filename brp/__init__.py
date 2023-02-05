from urllib import parse
import json
import xml.etree.ElementTree as ET
import logging
import argparse
import os
import re

parser = argparse.ArgumentParser(description="brp")
parser.add_argument(
    "-i",
    "--input",
    dest="input_filename",
    type=str,
    help="input filename (burpsuite export)",
    required=True,
)
parser.add_argument(
    "-o",
    "--output",
    dest="output_filename",
    type=str,
    help="output filename (either .py or .ipynb)",
    required=True,
)
parser.add_argument(
    "--debug",
    dest="debug",
    action="store_true",
    required=False,
)


def create_python_notebook(filename: str):
    with open(filename, "a+") as f:
        json.dump(
            {
                "cells": [
                    {
                        "cell_type": "code",
                        "execution_count": 5,
                        "id": "5bd0612f",
                        "metadata": {},
                        "outputs": [],
                        "source": ["import requests"],
                    },
                ],
                "metadata": {
                    "kernelspec": {
                        "display_name": "Python 3 (ipykernel)",
                        "language": "python",
                        "name": "python3",
                    },
                    "language_info": {
                        "codemirror_mode": {"name": "ipython", "version": 3},
                        "file_extension": ".py",
                        "mimetype": "text/x-python",
                        "name": "python",
                        "nbconvert_exporter": "python",
                        "pygments_lexer": "ipython3",
                        "version": "3.9.6",
                    },
                },
                "nbformat": 4,
                "nbformat_minor": 5,
            },
            f,
        )


def insert_in_file(
    filename: str,
    request_data: dict[str, str],
    cookies: dict[str, str],
    params: dict[str, str],
    headers: dict[str, str],
    method: str,
    url: str,
):
    if "ipynb" in filename:
        if not os.path.exists(filename):
            create_python_notebook(filename)
        with open(filename, "r+") as f:
            data = json.load(f)
            data["cells"].append(
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "id": "0xb4dc0ff3",
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        f"cookies= {json.dumps(cookies, indent=4)}\n",
                        f"headers= {json.dumps(headers, indent=4)}\n",
                        f"params= {json.dumps(params, indent=4)}\n",
                        f"data= {json.dumps(request_data, indent=4)}\n",
                        f"r = requests.{method.lower()}('{url}', params=params, cookies=cookies, headers=headers, data=data)",
                    ],
                }
            )

            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    else:
        with open(filename, "a") as f:
            f.write(
                f"""
cookies= {json.dumps(cookies, indent=4)}\n
headers= {json.dumps(headers, indent=4)}\n
params= {json.dumps(params, indent=4)}\n
data= {json.dumps(request_data, indent=4)}\n

r = requests.{method.lower()}(
    '{url}',
    params=params,
    data=data,
    cookies=cookies,
    headers=headers
)
"""
            )


def save_to_file(input_filename: str, output_filename: str):
    with open(input_filename) as file:
        tree = ET.parse(file)
        root = tree.getroot()
        for item in root[:]:
            url = item[1].text
            request_string = item[8].text
            logging.debug(request_string)
            method = item[5].text
            headers = {}
            cookies = {}
            request_data = ""
            parsed = parse.urlsplit(url)
            url = parsed.scheme + "://" + parsed.netloc + parsed.path
            params = dict(parse.parse_qsl(parsed.query))
            logging.info(url)

            for line in request_string.splitlines():
                if "Cookie" in line:
                    cookie_and_value = line.split(";")
                    for c in cookie_and_value:
                        k, v = c.split("=")[:2]
                        cookies[k.strip("Cookie: ")] = v
                elif "HTTP" not in line and "Host" not in line and "Cookie" not in line:
                    if (len(line.split(": "))) > 1:
                        k, v = line.split(": ")
                        headers[k] = v

            logging.debug(f"cookies: {cookies}")
            logging.debug(f"headers: {headers}")
            logging.debug("\n")
            data_raw = request_string.splitlines()[-1]
            if data_raw != "":
                data_raw = parse.unquote(data_raw)
                request_data = data_raw

            insert_in_file(
                output_filename,
                url=url,
                cookies=cookies,
                headers=headers,
                params=params,
                method=method,
                request_data=request_data,
            )


def run():
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    save_to_file(
        input_filename=args.input_filename, output_filename=args.output_filename
    )


if __name__ == "__main__":
    run()
