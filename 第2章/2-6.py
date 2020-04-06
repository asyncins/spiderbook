def request(flow):
    if ".png" in flow.request.url:
        # 判断 .png 是否在请求 URL 中
        with open("image.txt", "a+") as file:
            # 保存 URL
            file.write(flow.request.url)
            file.write("\n")