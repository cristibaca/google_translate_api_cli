FROM python:3

RUN pip install python-daemon

RUN pip install ratelimit

RUN pip install requests

RUN pip install argparse

ADD gtd /

ADD translator /

ADD gtranslate /

CMD [ "./gtd" ]