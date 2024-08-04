import requests

# 目标URL
url = 'http://www.baidu.com/'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 将网页内容写入到test.txt文件中
    print(response.text)
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print(f"请求失败，状态码：{response.status_code}")
