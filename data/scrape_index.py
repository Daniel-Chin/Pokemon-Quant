import requests
from html.parser import HTMLParser
import typing as tp
from itertools import count
from enum import Enum

URL = 'https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89'

CACHE_INDEX = 'cache_index.html'
class EventType(Enum):
    StartTag = 'StartTag'
    EndTag = 'EndTag'
    Data = 'Data'

Attrs = tp.List[tp.Tuple[str, tp.Optional[str]]]
Event = tp.Tuple[EventType, str, tp.Optional[Attrs]]

def getPage():
    try:
        with open(CACHE_INDEX, 'rb') as f:
            content = f.read()
        print('Cache found. Use? Y/N')
        if input().lower() == 'n':
            raise FileNotFoundError
    except FileNotFoundError:
        print('Getting page...')
        response = requests.get(URL)
        print('Got page.')
        assert response.status_code == 200, f'{response.status_code} {response.reason}'
        content = response.content
        with open(CACHE_INDEX, 'wb') as f:
            f.write(content)
    return content

class StopWait(Exception):
    def __init__(self, event: Event):
        super().__init__()
        self.event = event

def waitForTagRegardlessAttr(
    event: Event, eventType: EventType, tag: str, 
):
    if event[0] != eventType or event[1] != tag:
        return
    raise StopWait(event)

def waitForData(
    event: Event, 
):
    if event[0] != EventType.Data:
        return
    raise StopWait(event[1])

def StaticParser() -> tp.Generator[None, Event, None]:
    for gen in count(1):
        try:
            while True: 
                waitForData((yield), EventType.StartTag, 'h2', )
        except StopWait:
            pass
        else: assert False

class MyParser(HTMLParser):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.staticParser = StaticParser()

    def handle_starttag(self, tag: str, attrs: Attrs):
        self.staticParser.send((EventType.StartTag, tag, attrs))

    def handle_endtag(self, tag: str):
        self.staticParser.send((EventType.EndTag, tag, None))

    def handle_data(self, data: str):
        self.staticParser.send((EventType.Data, data, None))

def parse():
    page = getPage().decode('utf-8')
    parser = MyParser()
    parser.feed(page)
    parser.close()

def main():
    parse()

if __name__ == '__main__':
    main()
