import requests
import time

# 目标网址（还是百度）
url = "https://www.baidu.com"
total_size = 0  # 用来记录一共下载了多少字符

print("🚀 启动大批量下载任务！")
start_time = time.time()

# 用 for 循环，一口气下载 10 次！
for i in range(10):
    try:
        response = requests.get(url)
        # 【关键新知识】f"{i+1}" 让文件名动态变成 1.html, 2.html...
        filename = f"baidu_v1_{i+1}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        # 累加每次下载的大小
        total_size += len(response.text)
        print(f"✅ 第 {i+1} 个文件下载完成 ({len(response.text)} 字符)")
        
    except Exception as e:
        print(f"❌ 第 {i+1} 个文件下载出错: {e}")

end_time = time.time()

print("\n🎉 批量下载任务结束！")
print(f"📊 一共下载了 {total_size} 个字符 (约 {total_size/1024:.2f} KB 文本数据)")
print(f"⏱️ 总耗时 (10次循环): {end_time - start_time:.4f} 秒")