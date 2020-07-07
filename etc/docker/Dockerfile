FROM python:3.8-slim-buster

RUN mkdir /dscraper
ADD . /dscraper/
RUN pip install -r /dscraper/requirements.txt

RUN apt-get update && apt-get -y install cron
RUN (crontab -l ; echo "*/5 * * * * /usr/local/bin/python /dscraper/dscraper.py --truncate >> /var/log/cron.log 2>&1") | crontab

CMD cron && touch /var/log/cron.log && tail -f /var/log/cron.log