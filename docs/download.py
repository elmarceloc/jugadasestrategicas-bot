import gdown

url = 'https://drive.google.com/uc?id=1MHvTplzCarOI_GDW4xmUH_DlBxsRmhSh'
output = 'stockfish.zip'
gdown.download(url, output, quiet=False)