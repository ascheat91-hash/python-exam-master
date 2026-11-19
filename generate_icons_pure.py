import struct
import zlib

def write_png(filename, width, height, color_rgb):
    # Generates a standard uncompressed PNG file without external libraries
    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)

    magic = b'\x89PNG\r\n\x1a\n'
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0) # 8-bit truecolor RGB
    
    raw_data = bytearray()
    r, g, b = color_rgb
    for y in range(height):
        raw_data.append(0) # filter byte: none
        for x in range(width):
            raw_data.extend([r, g, b])
            
    idat = zlib.compress(bytes(raw_data), 9)
    
    with open(filename, 'wb') as f:
        f.write(magic)
        f.write(chunk(b'IHDR', ihdr))
        f.write(chunk(b'IDAT', idat))
        f.write(chunk(b'IEND', b''))

write_png('assets/icon-192.png', 192, 192, (30, 58, 138)) # #1e3a8a
write_png('assets/icon-512.png', 512, 512, (30, 58, 138))
print("Pure Python PNG icons created successfully.")

