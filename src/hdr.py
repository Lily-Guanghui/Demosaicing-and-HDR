def get_hdr_raw(files, ):
# Use the first image as the initial reference
    h = files[0]

    for idx in range(1, len(files)):
        i = files[idx] 

        t = 0.8 * h.max() 
        # h.max() gives the max value of the current HDR image; multiply by 0.8 as the threshold
        mask = h > t
        h[mask] = (i * 2 ** idx)[mask]

    return h