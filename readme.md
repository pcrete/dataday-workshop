# Python Webapp Demo


```bash
pip install jupyterlab

```

```bash
pip install -r requirements.txt
flask --help

export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run

# or
python app.py


# wsgi

pip install gunicorn

gunicorn --bind 0.0.0.0:8000 wsgi:app


# ============
gcloud init
gcloud auth login
gcloud config set project sandbox-403315
gcloud auth configure-docker

export NAME=tagger-api
export IMAGE=asia.gcr.io/sandbox-403315/$NAME

docker build -t $IMAGE .
docker run --rm -it -p 8080:8080 $IMAGE

docker buildx build --platform linux/amd64  -t $IMAGE . && docker push $IMAGE
gcloud run services update $NAME --image=$IMAGE --platform=managed --region=us-central1

# or
gcloud run deploy ticket-tagger --source ./ticket-classification --region=us-central1
```

I tried to make a transaction at a supermarket retail store, using my chase debit/atm card, but the transaction was declined. I am still able to withdraw money out of an ATM machine using the same debit card. Please resolve this issue.