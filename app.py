from PyPDF2 import PdfReader
import iocextract
import json


iocs = {
    'md5'    : [],
    'sha1'   : [],
    'sha256' : [],
    'ip'     : [],
    'url' : []
}

try:
    pdf = PdfReader('sample.pdf')
    print('Number of pages: {}'.format(len(pdf.pages)))
    for page in pdf.pages:
        text = page.extract_text()
        for url in iocextract.extract_urls(text):
            if url not in iocs['url']:
                iocs['url'].append(url)
        for hash in iocextract.extract_md5_hashes(text):
            if hash not in iocs['md5']:
                iocs['md5'].append(hash)
        for hash in iocextract.extract_sha1_hashes(text):
            if hash not in iocs['sha1']:
                iocs['sha1'].append(hash)
        for hash in iocextract.extract_sha256_hashes(text):
            if hash not in iocs['sha256']:
                iocs['sha256'].append(hash)
        for ip in iocextract.extract_ipv4s(text):
            if ip not in iocs['ip'] and 'http' not in ip:
                iocs['ip'].append(ip)
        
    print(json.dumps(iocs, indent=3))

except FileNotFoundError:
    print("Boy you're in a whole lot of trouble now!")