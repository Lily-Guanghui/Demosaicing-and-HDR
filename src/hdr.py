def get_hdr_raw(files, ):
    # 用第一张作为初始图像
    h = files[0]

    for idx in range(1, len(files)):
        i = files[idx] # 当前处理的较亮图像

        t = 0.8 * h.max() # h.max() 获取当前HDR图像的最大值，乘以0.8作为阈值
        mask = h > t
        h[mask] = (i * 2 ** idx)[mask]

    return h