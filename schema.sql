drop table if exists entries;
create table urls (
  id integer primary key autoincrement,
  title text not null,
  url text not null
);

create table tos (
  id INTEGER PRIMARY KEY autoincrement,
  title text not null,
  contents text not null,
  date_scraped DATE not null,
  url_id integer,
  FOREIGN KEY (url_id) REFERENCES  urls(id)
);


