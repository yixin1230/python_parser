import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse,urldefrag
from collections import deque

class PythonParser:
    def __init__(self, start_url, max_depth=3):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited = set()
        self.start_host = urlparse(start_url).netloc

    def same_domain(self, url):
        return urlparse(url).netloc == self.start_host
    
    def get_links(self, url):
        links = set()
        try:
            html = requests.get(url, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            for a in soup.find_all("a", href=True):
                full_url = urljoin(url, a["href"])
                # urldefrag(urljoin(url, a["href"]))not works for bfs, because it rm all 
                if '/#' in full_url:
                    full_url = full_url.rsplit("/#", 1)[0]
                if self.same_domain(full_url):
                    links.add(full_url)
        except Exception as e:
            print("Error:", e)
        return links

    def python_parser_for_for_for(self):
        for url1 in self.get_links(self.start_url):
            if url1 in self.visited:
                continue
            self.visited.add(url1)
            # print("level 1:", url1)

            for url2 in self.get_links(url1):
                if url2 in self.visited:
                    continue
                self.visited.add(url2)
                # print("level 2:", url2)
                for url3 in self.get_links(url2):
                    if url3 in self.visited:
                        continue
                    self.visited.add(url3)
                    print("level 3:", url3)

    def python_parser_recursion(self, url=None, depth=1):
        if url is None:
            url = self.start_url
        if depth > self.max_depth or url in self.visited:
            return
        self.visited.add(url)
        if depth == self.max_depth:
            print(f"level {depth}: {url}")
        else:
            for link in self.get_links(url):
                self.python_parser_recursion(link, depth+1)

    def python_parser_bfs(self):
        queue = deque([(self.start_url, 1)])
        while queue:
            url, depth = queue.popleft()
            if url in self.visited or depth > self.max_depth:
                continue
            self.visited.add(url)
            if depth == self.max_depth:
                print(f"level {depth}: {url}")
            else:
                for new_url in self.get_links(url):
                    if new_url not in self.visited:
                        queue.append((new_url, depth+1))


if __name__ == "__main__":
    parser = PythonParser("https://docs.clustervision.com", max_depth=3)
    # each output is different 
    parser.python_parser_for_for_for() 
    # parser.python_parser_recursion()
    # parser.python_parser_bfs()

