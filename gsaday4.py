import mechanicalsoup
import bs4
import requests

browser = mechanicalsoup.StatefulBrowser()

browser.open("https://www.gsa-spark.com/speedtest/ad68d729-67a7-45fd-8ca6-a8035f7da979")


browser.select_form()
res = requests.get('https://www.gsa-spark.com/speedtest/ad68d729-67a7-45fd-8ca6-a8035f7da979')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
num1 = soup.select('#number1')
num1 = num1[0].text.strip()
num2 = soup.select('#number2')
num2 = num2[0].text.strip()

total = int(num1) + int(num2)
print(total)

browser["answer"] = total

response = browser.submit_selected()

print(response.text)
