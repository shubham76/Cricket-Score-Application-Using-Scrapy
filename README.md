# Cricket Score Application Using Scrapy

Simple Cricket Scoring Application Using Python Scrapy
This is a simple application which scraps http://www.espncricinfo.com/ website.
It gives the list of all the cricket matches that are going on and shows the scoring details if asked. 
It also gives the notification on ubuntu side bar if any wicket falls or somebody scores a century.

## Getting Started

Follow the instructions to get the project running on your local machine.
(Running the project in Virtual Environment is preferable.)

### Prerequisites

Scapy

```
pip install scrapy
```

### Installing


```
git clone https://github.com/shubham76/Cricket-Score-Application-Using-Scrapy.git
```

Go to the `spiders/` folder inside the cloned repository and run the following command. 

```
scrapy runspider scores.py
```

### How to use?

Select the index of the match for which you want to see the scores.
You can see scores and notifications will start coming! 

## Contributing

Just fork the repository and create the branch with added feature and create a PR!