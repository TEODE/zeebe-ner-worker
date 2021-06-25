Zeebe Text Classification Worker
================================

A [Zeebe](https://zeebe.io) text classifier worker based on [Hugging Face](https://huggingface.co/) NLP pipeline

Configure
---------

Set a virtual python environment for version 3.7.10 and install requirements:

```bash
pip install -r requirements.txt 
```

Specify a local (after downloading under models folder) or an [Hugging Face token classification model](https://huggingface.co/models?pipeline_tag=token-classification) in the .env file

Due to high resource consumption of some models, we decided to make this worker configurable in term of task name and associated model.
For example, so it is possible to separate tasks and models with multiple workers for language handling :

* task `ner-en` and model (default will be downloaded at worker startup from Hugging Face's website)
* task `ner-fr` and local model `models/camembert-ner-with-dates`

Run locally
-----------

If you have a local/docker-compose Zeebe running locally you can run/debug with:

```bash
python index.py
```

Run tests
---------

```bash
python -m unittest
```

Build with Docker
-----------------

```bash
docker build -t docker.pkg.github.com/teode/zeebe-ner-worker/zeebe-ner-french-worker:v1.0.0 -f Dockerfile.fr .
```

Make a Github package
---------------------

```bash
docker push docker.pkg.github.com/teode/zeebe-ner-worker/zeebe-ner-french-worker:v1.0.0
```

Else get it from Docker hub:

Or download from: https://hub.docker.com/r/teode/zeebe-ner-french-worker

Run with Docker
-----------------

You must have a local or a port-forwarded Zeebe gateway for the worker to connect then:

```bash
docker run --name zb-ner-fr-wkr zeebe-ner-french-worker
```

Usage
-----

Example BPMN with service task:

 ```xml
 <bpmn:serviceTask id="my-ner" name="My NER">
   <bpmn:extensionElements>
     <zeebe:taskDefinition type="my-env-var-task-name" />
   </bpmn:extensionElements>
 </bpmn:serviceTask>
 ```

* the worker is registered for the type of your choice (set as an env var)
* required variables:
  * `sequence` - the phrase to classify
* jobs are completed with an `entities` object containing serialized properties:
  * `entity_group` - ORG (organization), DATE, PER (firstname and/or name), LOC (location)
  * `score` - the confidence score
  * `word` - the word extracted from the sequence
  * `start` - the position in the first letter
  * `end` - the position in the last letter
