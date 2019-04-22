# Bird

A simple twitter bot that allows for scraping a website, picking a URL and a snippet of text from the page that URL links to and tweets it. The bot does so every 10 Minutes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

You will need a system with these requirements:

1. A system running [python](https://www.python.org/downloads/) version 3.6+
2. A twitter account
3. API keys for twitter accessed [here](https://developer.twitter.com/)


### Installing

To get started clone this git repository

```
git clone https://github.com/Spcktr/Bird.git
````

Change directory to the now created Bird directory and run
```
python3 -m vevn bird-env
```

Once you've created the virtual environment activate it

Linux:
```
source bird-env/bin/activate
```
Windows:
```
.\bird-env\Scripts\activate.bat
```

Rename the sample_creds.py file to creds.py
```
mv sample_creds.py creds.py
```
Then edit the creds file by inserting your access tokens and consumer keys.

Install the required packages

```
pip3 install -r requirements.txt
```

Then run the bot
```
python3 main.py
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Pip](https://github.com/pypa/pip) - Dependency Management


## Authors

* **Saurabh Chaturvedi** - *Initial work* - [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-and-post-content-to-twitter-with-python-3/#step-5-%E2%80%94-tweeting-the-scraped-content)


## License

This project is licensed under the  - see the [LICENSE.md](LICENSE.md) file for details
