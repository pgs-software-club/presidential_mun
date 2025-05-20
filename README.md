## Repository of Presidential MUN

This is the official repository of Presidential MUN

### Setup process for the project

- Clone the repo

```bash
git clone https://github.com/pgs-software-club/presidential_mun.git
```

- Install all the require packages

```bash
pip install -r requirements.txt
```

- Setup database and environment by renaming .env.example to .env and filling the required information

```bash
cp .env.example .env
```

- Setup database using docker or any other local instances

- Run the application

```bash
python server.py
```
