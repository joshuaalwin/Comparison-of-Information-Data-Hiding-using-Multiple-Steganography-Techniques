# Comparison-of-Information-Data-Hiding-using-Multiple-Steganography-Techniques
This tool aims to compare images produced by LSB and DCT Steganography based on characteristics such as MSE, PSNR and SSIM. 


## Installing the Required tools

```py
pip3 install -r requirements.txt
```


## Usage

```py
stego.py [-h] [-d] [-a] -i FILE [-o FILE] [-s STRING] [-f FILE]
```

Stego: DCT and LSB Image Steganography

optional arguments:
  -h, --help  show this help message and exit
  -d          Set method to decode, default is encode
  -a          Set encoding/decoding algorithm to LSB, default is DCT
  -i FILE     Specify input file name
  -o FILE     Specify output file name (optional)
  -s STRING   Specify message to encrypt
  -f FILE     Specify text file containing message


