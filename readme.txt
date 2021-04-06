sqlite3 app.db
CREATE TABLE IF NOT EXISTS uploads (
  id integer PRIMARY KEY,
  file_name text NOT NULL,
  file_blob text NOT NULL
);