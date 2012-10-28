drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  message string not null,
  created datetime default current_timestamp
);
