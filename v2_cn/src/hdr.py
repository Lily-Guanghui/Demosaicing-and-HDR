def get_hdr_raw(files, ):
    # 用第一张作为初始图像
    h = files[0]

    for idx in range(1, len(files)):
        i = files[idx] # 当前处理的较亮图像

        t = 0.8 * h.max() # h.max() 获取当前HDR图像的最大值，乘以0.8作为阈值
        mask = h > t
        h[mask] = (i * 2 ** idx)[mask]

    return h

#     def get_hdr_raw(files):
#     # 用最亮图作为初始图像
#     h = files[0].copy()  # 避免修改原始数组

#     for idx in range(1, len(files)):
#         i = files[idx]  # 当前处理的较暗图像

#         # HDR中过亮的阈值（取当前HDR最大值的80%）
#         t = 0.8 * h.max()
#         mask = h > t  # 只有HDR中过亮的区域才被替换

#         # 用当前较暗图替换过亮区域，同时可按经验缩放（可根据曝光时间调整）
#         h[mask] = i[mask] * 1.0  # 这里简单用1.0，保持原图亮度

#     return h
# def get_hdr_raw(files,):
#     h = files[0].copy()  # 最亮图作为初始 HDR
#     for idx in range(1, len(files)):
#         i = files[idx]
#         i_scaled = i * (2 ** idx)  # 假设每张比上一张曝光减半
#         mask = h > 0.8 * h.max()   # HDR中过亮的区域
#         h[mask] = i_scaled[mask]
#     return h
