import requests
from bs4 import BeautifulSoup

# Gửi yêu cầu HTTP GET để lấy trang web
response = requests.get('https://vnexpress.net/hon-23-trieu-hoc-sinh-buoc-vao-nam-hoc-moi-4788964.html')

# Kiểm tra nếu yêu cầu thành công (status code 200)
if response.status_code == 200:
    # Phân tích nội dung HTML của trang bằng BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tìm thẻ chứa thông tin thời gian (dựa trên cấu trúc cụ thể của trang web)
    time_tag = soup.find('span', class_='date')
    
    # Kiểm tra nếu tìm thấy thẻ thời gian
    if time_tag:
        # Lấy nội dung của thẻ (thời gian) và ghi vào file
        article_time = time_tag.get_text(strip=True)
        with open('article_time.txt', 'w', encoding='utf-8') as file:
            file.write(article_time)
    else:
        print("No time tag found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")