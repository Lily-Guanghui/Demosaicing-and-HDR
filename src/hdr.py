def get_hdr_raw(files, ):
    h = files[0]

    for idx in range(1, len(files)):
        i = files[idx]

        t = 0.8 * h.max()
        mask = h > t
        h[mask] = (i * 2 ** idx)[mask]

    return h