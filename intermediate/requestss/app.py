import requests

# response = requests.get("https://www.kgkite.ac.in/")
# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(response.text)

response = requests.get("https://api.github.com/users/aravinth")
# print("url is", r)
print(response.text)