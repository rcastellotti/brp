from urllib import parse
import json
import xml.etree.ElementTree as ET
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
parser = argparse.ArgumentParser(description="brp")
parser.add_argument(
    "-f",
    "--filename",
    dest="filename",
    type=str,
    help="an integer for the accumulator",
    required=True,
)


def add_cell_to_notebook(
    filename: str,
    request_data: dict[str, str],
    cookies: dict[str, str],
    params: dict[str, str],
    headers: dict[str, str],
    method: str,
    url: str,
):
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


def add_to_file(
    filename: str,
    cookies: dict[str, str],
    params: dict[str, str],
    headers: dict[str, str],
    method: str,
    request_data: dict[str, str],
    url: str,
):
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


def save_to_file(filename: str):
    with open("burp.xml") as file:
        tree = ET.parse(file)
        root = tree.getroot()
        for item in root[:]:
            url = item[1].text
            request_string = item[8].text
            method = item[5].text
            cookie_list = []
            headers_list = []
            headers = {}
            cookies = {}
            spl = request_string.split()

            parsed = parse.urlsplit(url)
            url = parsed.scheme + "://" + parsed.netloc + parsed.path
            params = dict(parse.parse_qsl(parsed.query))
            logging.debug(url)

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

            data_raw = request_string.splitlines()[-1]
            data_parsed = parse.unquote(data_raw).split("&")
            request_data = {k: v for k, v in [d.split("=") for d in data_parsed]}

            add_cell_to_notebook(
                "template.ipynb",
                url=url,
                cookies=cookies,
                headers=headers,
                params=params,
                method=method,
                request_data=request_data,
            )

            add_to_file(
                "template.py",
                url=url,
                cookies=cookies,
                headers=headers,
                params=params,
                method=method,
                request_data=request_data,
            )


if __name__ == "__main__":
    args = parser.parse_args()
    save_to_file(args.filename)
