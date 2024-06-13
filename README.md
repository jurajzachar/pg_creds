# pg_creds
A tool to generate and hash (md5) credentials of Postgresql role. The tool is useful for managing Postgresql role credentials
without exposing the password to the database server.

## Installation
```bash
python3 install.py
```

## Usage

### Hash password
```bash
> pg_creds --role miriam --hash

type postgres password to hash for role miriam
jw8s0F4
hashed password (miriam):
md5f8a4ea6f4f079632cddb7c83a10fe02c
```

### Generate password
The tool will generate a random password of fixed length of __20 characters__ for the role and hash it.

```bash
> pg_creds --role miriam --generate

generated password (miriam):
[[UJupMCH!hApX<YO`a6
hashed password (miriam):
md59da8e0ae7673ba3c58baac97dab4edff
```

## Manage Postgres role credentials
```
CREATE ROLE miriam WITH LOGIN PASSWORD 'md59da8e0ae7673ba3c58baac97dab4edff' VALID UNTIL '2005-01-01';
```

## Limitations
Future versions of this tool will support `SCRAM-SHA-256$4096` hashing algorithm.