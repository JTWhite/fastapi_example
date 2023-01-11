
# FastAPI Example
This repo is a basic template into how FastAPI can be used. It accesses an weather API to determine what type of coat you should wear.

# Getting Started

Create a vitural environemnt 
```
python -m venv venv
```
Then acticate said environment for mac 
```
source venv/bin/activate
```
or in windows 
```
.\venv\Scripts\activate
```
install the `requirements.txt`
```
pip install -U -r requirements.txt
```

Run the following command where main is the python name and app is the method you're trying to run. 
`uvicorn main:app --reload`

using the extension `/doc` on the spun up server, FastAPI will automatically create documentation for you. 