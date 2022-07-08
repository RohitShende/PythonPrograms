"""
URL Shortner

long_url   - 1000 char
short_url  - 25 char       - index
ttl - 7 days (user selected 3 - 30 days)
combo - long_url : ip - index

100 million new url / month
3-4 million / day
/ hour
/ sec

rate limiter

cloud
=====
elastic containers to scale as per load
https and certs
rate limiter
sql injections = ORM
UI - 443
reverse proxy - 8000 backend or REST server with LB


read requests - 100 times read requests

how to convert long to short -
UUID
SHA256 + randomness -> currentimeinmillis / epoch


issues -
1. too many read requests  - indexing / caching
2. same long url coming more than once sequentially - combo column
3. multiple people trying to create short url for same long url - concurrent request
    - check and then update
        - GET call check
          POST call
        - create if not exist - DB
4. redirection
    - short url not present


100 million * 1000 = 10^11 bits  = x bytes = x MB = x GB
                                           = y MB = y GB
                                           = z MB = z GB
                                           ===============
                                           ZXX GB per month

bit.ly/?short_url=sygrio383902
bit.ly/sygrio383902

%2D

decode the url -> trim
create the short url

return 301

"""

"""
innovacer - US healthcare product - Product / Platform / Customer 
team - 
work culture - agile 2 weeks sprint
tech stack - micro service architecture / Python * / Scala / Django, Flask and Pyramid / AWS / RDS / Mongo / 
Elasticsearch / Redis / Celery
"""