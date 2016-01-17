def condition_3(src, value):

    src_head = word.split(b'\x01\x02', 1)[0]
    val_head = value.split(b'\x01\x02', 1)[0]

    d_diff = src_head.count(b'\x02') - val_head.count(b'\x02')
    c_count = val_head.count(b'\x01')
    return c_count >= d_diff
