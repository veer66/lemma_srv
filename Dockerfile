FROM alpine:3.10
RUN apk update
RUN apk add python3-dev alpine-sdk
RUN pip3 install -U spacy
RUN python3 -m spacy download en_core_web_sm
RUN pip3 install starlette
RUN pip3 install uvicorn
COPY app.py /
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app:app"]]