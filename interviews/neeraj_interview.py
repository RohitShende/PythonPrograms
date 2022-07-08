"""
a + b = c
display
"""


def table_header(func):
    def inner(*args, **kwargs):
        html = '<table>'
        html += func(*args, **kwargs)
        html += '</table>'
        return html

    return inner


@table_header
def table_body(l):
    s = ''
    for i in l:
        s += f'<td>{i}</td>'
    return s


lst = [1, 2, 3, 4, 5]
html_ = table_body(lst)
print(html_)


def tests():
    assert table_body([]) is not None
    assert table_body([]) != ''
    assert table_body([]).startswith('<table>')
    assert table_body([])[-8:] == '</table>'



"""
Feeds in various formats - str, json, xml, csv  => json
millions of feeds
lot of duplicated data

Read and Write to DB
Process
Visualize

Questions - 
handling duplicates
tech stack - Django, Rabbit MQ, multiprocessing package, asyncio, LB 
db to handle the load
store the feeds ? - No need
inputs are multiple partitions per file
16 core / 32 GB machine
ttl
/data partition
onprem

i/p
str, json, xml, csv  => json

o/p
db dump = read / write heavy

ip is malicious, src_ip 1
ip is malicious, src_ip 2
ip is malicious, src_ip 3

My SQL
-------
processed_record
    id 1
source
    id 1
    id 2
    id 3
source_mapping_processed_record
    pr    sr

Mongo
-----
Processed Doc
    - id
    - fields ...
    - source = [src1, src2, src3]

In Memory DB
------------
key value 

DB
--
1. Relational SQL
2. No SQL - Mongo DB
3. In Memory DB - memcache / diskcache

"""


"""
Login - Role based auth -    Feeds  -  Middle ware for converting to json - Processing - Multiple consumers to process
                            Queuing    Consumer                             Queuing      process -> extract info from feed and store to DB
                                       multiple consumers together
                            
POST /feed  -> backend -> Add the message to the Queue and return
"""








