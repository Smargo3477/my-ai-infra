# 模拟服务器日志
raw_log = """
2026-06-30 08:12:00 [INFO] User login success: user001
2026-06-30 08:14:22 [ERROR] Database connection timeout
2026-06-30 08:15:10 [WARNING] Disk usage at 85%
2026-06-30 08:16:05 [INFO] User logout: user001
2026-06-30 08:18:30 [ERROR] Failed to fetch model weights
"""

info_count = 0
error_count = 0
warning_count = 0

lines = raw_log.split('\n')

for line in lines:
    # 【填空 2】：如果这一行里包含 "[ERROR]"
    if "[ERROR]"  in line: 
        error_count += 1  
    
    elif "[WARNING]" in line:
        warning_count += 1
    elif "[INFO]" in line:
        info_count += 1

print(f"📊 统计结果：")
print(f"INFO: {info_count} 条")
print(f"ERROR: {error_count} 条")
print(f"WARNING: {warning_count} 条")