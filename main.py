import uvicorn
from fastapi import FastAPI, File, UploadFile
import os
import sqlite3
import shutil
from sqlite3 import Error
from fastapi.responses import FileResponse

app = FastAPI()


@app.get('/download/{id}')
def download_file(id: int):
  try:
    file_path = "temp/"+read_blob_data(id)
  except:
    return {"detail":"File Not Found"}
  return FileResponse(path=file_path, filename=file_path)
    



@app.post("/create_file/")
async def create_file(file: UploadFile = File(...)):
    file_path_name  =f"temp/{file.filename}"
    with open(file_path_name, "wb+") as file_object:
      file_object.write(file.file.read())
    file_blob = convert_into_binary(file_path_name) 
    last_updated_entry = insert_into_database(file_path_name, file_blob)
    return {"id": last_updated_entry,"link":"download/"+last_updated_entry,"detail":"Success","filename":file.filename}



def convert_into_binary(file_path):
  with open(file_path, 'rb') as file:
    binary = file.read()
  return binary

def insert_into_database(file_path_name, file_blob): 
  try:
    conn = sqlite3.connect('app.db')
    print("[INFO] : Successful connection!")
    cur = conn.cursor()
    sql_insert_file_query = '''INSERT INTO uploads(file_name, file_blob)
      VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(sql_insert_file_query, (file_path_name, file_blob, ))
    conn.commit()
    print("INFO: The blob for ", file_path_name, " is in the database.")
    last_updated_entry = cur.lastrowid
    return last_updated_entry
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()
    else:
      error = "Oh No, something is wrong here."
      print(error)

def read_blob_data(entry_id):
  filename = ""
  try:
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    print("[INFO] : Connected to SQLite to read_blob_data")
    sql_fetch_blob_query = """SELECT * from uploads where id = ?"""
    cur.execute(sql_fetch_blob_query, (entry_id,))
    record = cur.fetchall()
    for row in record:
      converted_file_name = row[1]
      photo_binarycode  = row[2]
      # parse out the file name from converted_file_name
      last_slash_index = converted_file_name.rfind("/") + 1 
      final_file_name = converted_file_name[last_slash_index:] 
      write_to_file(photo_binarycode, final_file_name)
      filename = final_file_name
      print("[DATA] : Image successfully stored on disk. Check the project directory. \n")
    cur.close()
  except sqlite3.Error as error:
    print("[INFO] : Failed to read blob data from sqlite table", error)
  finally:
    if conn:
        conn.close()
  return filename


def write_to_file(binary_data, file_name):
  try:
    os.mkdir("temp")
  except:
    print("Directory Already Created")
  with open("temp/"+file_name, 'wb') as file:
    file.write(binary_data)
  print("[DATA] : The following file has been written to the project directory: ","temp/", file_name)


uvicorn.run(app, host="0.0.0.0", port=8080)
