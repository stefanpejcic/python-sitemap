# Python-Sitemap

Simple script to crawl websites and create a sitemap.xml of all public link in it.

Warning : This script only works with ***Python3***

## Simple usage

	>>> python main.py --domain http://blog.lesite.us --output sitemap.xml

## Advanced usage

Read a config file to set parameters:
***You can overide (or add for list) any parameters define in the config.json***

	>>> python main.py --config config/config.json

#### Enable debug:

  ```
	$ python main.py --domain https://blog.lesite.us --output sitemap.xml --debug
  ```

#### Enable verbose output:

  ```
  $ python main.py --domain https://blog.lesite.us --output sitemap.xml --verbose
  ```

#### Enable Image Sitemap

More informations here https://support.google.com/webmasters/answer/178636?hl=en

  ```
  $ python main.py --domain https://blog.lesite.us --output sitemap.xml --images
  ```

#### Enable report for print summary of the crawl:

  ```
  $ python main.py --domain https://blog.lesite.us --output sitemap.xml --report
  ```

#### Skip url (by extension) (skip pdf AND xml url):

  ```
  $ python main.py --domain https://blog.lesite.us --output sitemap.xml --skipext pdf --skipext xml
  ```

#### Drop a part of an url via regexp :

  ```
  $ python main.py --domain https://blog.lesite.us --output sitemap.xml --drop "id=[0-9]{5}"
  ```

#### Exclude url by filter a part of it :

  ```
  $ python main.py --domain https://blog.lesite.us --output sitemap.xml --exclude "action=edit"
  ```

#### Read the robots.txt to ignore some url:

  ```
  $ python main.py --domain https://blog.lesite.us --output sitemap.xml --parserobots
  ```

#### Human readable XML

```
$ python3 main.py --domain https://blog.lesite.us --images --parserobots | xmllint --format -
```

#### Multithreaded

```
$ python3 main.py --domain https://blog.lesite.us --num-workers 4
```
