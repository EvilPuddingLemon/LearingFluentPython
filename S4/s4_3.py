for codec in ['latin_1', 'utf8', 'utf16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')
