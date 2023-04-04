# ML Server

This is a microservice built on the FastAPI framework that allows you to process images and generate embeddings. It's designed to be fast, efficient, and easy to use.

Using this microservice, you can upload an image to the API, which will then process the image and generate an embedding vector. The embedding vector can be used for various tasks such as face recognition, object detection, or similarity matching.

## Run the project with Docker

Run the following command to build an image from the Dockerfile:

`docker build -t myapp .`

Here, myapp is the name you want to give to the image, and the . at the end indicates that the build context is the current directory.

Once the image is built, you can run a container from it using the following command:

`docker run -p 8000:8000 -e PORT=8000 myapp`

Here, -p 8000:8000 maps the port 8000 of the container to the port 8000 of the host machine, and -e PORT=8000 sets an environment variable named PORT to the value 8000. Finally, myapp is the name of the image you built in step 3.

This will start a container running the application, which you can access by going to http://localhost:8000 in your web browser.

## Development

If you need to run/test the project you need:

1. Install `python` (we recommend `3.11`)
2. Create a virtual environment within the project folder:

```bash
python -m venv venv
```

3. Activate the virtual environment and install packages

```bash
# activate
source ./venv/bin/activate

# install packages
pip install -r requirements.in
```

4. If you need to add a new packages, add it to `requirements.in` and then run `pip-tools` to compile:

```bash
# you need to install pip-tools
pip install pip-tools

# compile requirements
pip-compile requirements.in

# instsal packages
pip install -r requirements.txt
```

5. Run the local server:

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8080 --reload
```