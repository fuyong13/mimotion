from datetime import datetime

def log_variables(*variables, filename='app.log'):
    """记录变量到日志文件，每行一条记录"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] " + ' '.join(str(v) for v in variables) + '\n')

# 使用
name = "张三"
action = "登录"
status = "成功"
log_variables(name, action, status)
log_variables("用户", name, "执行了操作", "年龄:", 25)
