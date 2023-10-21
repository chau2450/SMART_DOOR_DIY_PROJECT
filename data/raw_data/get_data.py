import gdown
# import requests
# from bs4 import BeautifulSoup

# folder_id = "0B7EVK8r0v71pWEZsZE9oNnFzTm8"

# destination = "download/"


# def get_file_links(folder_id):
#     url = f"https://drive.google.com/drive/folders/{folder_id}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     file_links = []
#     for a_tag in soup.find_all("a"):
#         href = a_tag.get("href", "")
#         if "/file/d/" in href:
#             file_links.append(href)
    
#     return file_links

# file_links = get_file_links(folder_id)

# print("hello00")
# print(file_links)

# for file_link in file_links:
#     file_id = file_link.split("/file/d/")[1].split("/view")[0]
#     download_link = f"https://drive.google.com/uc?id={file_id}"
#     gdown.download(download_link, output=destination, quiet=False)


url = "https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg"
output = 'CelebA_data.tgz'
gdown.download(url, output, quiet=False)
