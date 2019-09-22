# lemma_srv

lemma_srv is a lemmatization Web API, which wraps SpaCY.

## Build

```
docker build -t lemmasrv .
```

## Run

```
docker run -d --net=host lemmasrv
```

## Try

```
curl -H 'Content-type: application/json' -XPOST localhost:8000/lemma -d '{"text":"He loves it"}'
```
