
import requests
import time

# 目标网址
url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

print(f"开始下载: {url}")
start_time = time.time()

try:
    # 发送网络请求
    response = requests.get(url)
    
    # 把网页内容保存到本地
    filename = "baidu_v1.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    end_time = time.time()
    print(f"✅ 下载完成！保存为: {filename}")
    print(f"📏 文件大小: {len(response.text)} 字符")
    print(f"⏱️ 单线程耗时: {end_time - start_time:.4f} 秒")
    
except Exception as e:
    print(f"❌ 下载出错: {e}")