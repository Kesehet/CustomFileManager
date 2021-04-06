# Developing Custom File Information Manager (Repl.it Instructions)

- Fork this repo to get started
- Simply hit run to start the server
- 
## First Run

1. Ensure that there is a temp folder in the main directory
2. Ensure there is an app.db in the main directory (if not refer to app.db section)

## Usage
- This app runs on the server and lets you download and upload files on the server.
- To first upload a file make a POST request using the index.html to 
```
xyz.com/create_file
```
  and save the id to be able to download it back from the server.
-To download a file, visit 
```
xyz.com/download/[ID_OF_THE_FILE]
```
- This app doesnt use authentication at the time of writing. (basic authentication will be added soon.)
- 
## Making App.db file
open CMD and simply write
```
sqlite3 app.db
```
and then create a table using
```
CREATE TABLE IF NOT EXISTS uploads (
  id integer PRIMARY KEY,
  file_name text NOT NULL,
  file_blob text NOT NULL
);
```

## Run the program @
https://replit.com/@HamoodSiddiqui/fastapi#index.html
