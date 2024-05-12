# Gnp

Script that generates the following passwords patterns which are commonly used in organizations:

```sh
<COMPANY><YEAR>
<SEASON><YEAR>
<YEAR><COMPANY>
<YEAR><SEASON>
<COMPANY>@<YEAR>
<SEASON>@<YEAR>
<YEAR>@<COMPANY>
<YEAR>@<SEASON>
<COMPANY>.<YEAR>
<SEASON>.<YEAR>
<YEAR>.<COMPANY>
<YEAR>.<SEASON>
```

> Purpose: Generate passwords to use for cracking hashes or password spraying.

# Usage

Generate strings based on company name and year:

```sh
gnp.py -c company_name -y year 
```

Generate strings based on season name and year:

```sh
gnp.py -s season_name -y year 
```

Generate strings based on company name and years:

```sh
gnp.py -c company_name -m year-start-range year-end-range
```

Generate strings based on season name and years:

```sh
gnp.py -s season_name -m year-start-range year-end-range
```