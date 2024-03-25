.PHONY: all clean default install lock update checks pc test docs run

default: build

build:
	poetry run maturin develop

install:
	pre-commit install
	poetry install --sync

lock:
	poetry lock --no-update

update:
	poetry up --latest

checks: pc install build lint test

pc:
	pre-commit run -a

lint:
	poetry run poe lint

test:
	poetry run poe test

rs-test:
	cargo test --all-features --workspace

rs-fmt:
	cargo fmt --all --check

rs-clippy:
	cargo clippy --all-targets --all-features --workspace -- -D warnings
