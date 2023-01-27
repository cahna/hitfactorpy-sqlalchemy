## Features
- [ ] Custom scoring equations
- [x] ~~Calculate hitfactors in SQL~~
- [ ] Add model methods for domain logic:
  - [ ] calculate overall winner
  - [ ] calculate division winners

## Technical
- [x] ~~Refactor all `float` to `Decimal` and use `sqlalchemy.Numeric`~~
- [ ] Make DB drivers optional/extras dependencies (probably requires splitting the package into more subpackages)
- [ ] Test with multiple databases
  - [ ] mariadb
  - [ ] mysql
  - [ ] sqlite
