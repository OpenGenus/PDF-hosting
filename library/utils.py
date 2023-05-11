def to_mbs(bytes_):
    # 1KB = 1024 bytes
    # 1MB = 1024KB = 1024*1024 Bytes
    bytes_per_mb = 1024*1024
    return round(bytes_/bytes_per_mb, 1)


