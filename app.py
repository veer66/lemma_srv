from starlette.applications import Starlette
from starlette.responses import JSONResponse
import spacy

nlp = spacy.load("en_core_web_sm", disable=["tagger", "parser"])

app = Starlette()

@app.route('/lemma', methods=["POST"])
async def lemma(req):
    params = await req.json()
    text = params["text"]
    doc = nlp(text)
    lemma = [tok.lemma_ for tok in doc]
    return JSONResponse({"lemma": lemma})
