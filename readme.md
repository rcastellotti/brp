# brp


`brp` is a simple tool to convert request from [burpsuite](https://portswigger.net/burp)'s HTTP History export to [python-requests](https://requests.readthedocs.io/en/latest/user/quickstart/).

To obtain the HTTP History export file just intercept some requests, go to HTTP History, select them, right click and click `Save Items`.

## install

`pip3 install brp`

## usage 

I mainly use it to embed requests in a python notebooks, by using:   
```python
brp -i burp.xml -o template.ipynb
```

There is not much more to say, if in doubt run `python3 brp.py --help`

### release new version
+ bump version
+ `python3 -m build`
+ `python3 -m twine upload dist/*`