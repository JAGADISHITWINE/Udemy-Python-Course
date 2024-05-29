import zlib, base64
# base64 encode the data

def compress(inpufile,outputfile):
    data =  open(f'C:/python/Udemy-Course/File Compression & Encoding/{inpufile}.txt','r').read()
    data_bytes =data.encode('utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(f'C:/python/Udemy-Course/File Compression & Encoding/{outputfile}.txt','w')
    compressed_file.write(decoded_data)

compress('Sample','Compressed')

def decompress(inpufile,outputfile):
    file_content = open(f'C:/python/Udemy-Course/File Compression & Encoding/{inpufile}.txt','r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    decompressed_file = open(f'C:/python/Udemy-Course/File Compression & Encoding/{outputfile}.txt','w')
    decompressed_file.write(decoded_data)
    
decompress('Compressed','Decompressed')