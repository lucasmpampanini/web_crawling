from lxml import html
import requests

class url:

    def urls_requests(self, url): #Está função recebe as urls, aplicamos o requests e html e deixamos preparada para o xpath.
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        headers = {'User-Agent': user_agent}
        page = requests.get(url, headers=headers)
        page_html = html.fromstring(page.content)

        return page_html