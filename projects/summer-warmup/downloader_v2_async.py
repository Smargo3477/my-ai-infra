import asyncio
import aiohttp
import time

url = "https://www.baidu.com"

# 定义一个异步任务：单独下载一个文件
async def download_one(session, i):
    try:
        # async with：异步地建立连接
        async with session.get(url, timeout=10) as response:
            # await：这里遇到网络等待时，会自动“挂起”，把执行权让给别的任务
            text = await response.text()
            
            filename = f"baidu_v2_{i+1}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)
            
            size = len(text)
            print(f"✅ 第 {i+1} 个文件异步下载完成 ({size} 字符)")
            return size
    except Exception as e:
        print(f"❌ 第 {i+1} 个文件下载出错: {e}")
        return 0

# 主控制台
async def main():
    print("🚀 启动异步并发下载任务！")
    start_time = time.time()

    # 创建一个网络会话池
    async with aiohttp.ClientSession() as session:
        # 核心魔法：一次性生成 10 个任务
        tasks = [download_one(session, i) for i in range(10)]
        
        # asyncio.gather 让这 10 个任务“同时开火”
        results = await asyncio.gather(*tasks)

    total_size = sum(results)
    end_time = time.time()

    print("\n🎉 异步下载任务结束！")
    print(f"📊 一共下载了 {total_size} 个字符 (约 {total_size/1024:.2f} KB 文本数据)")
    print(f"⏱️ 异步总耗时: {end_time - start_time:.4f} 秒")

if __name__ == "__main__":
    asyncio.run(main())