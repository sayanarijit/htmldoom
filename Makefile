.PHONY: docs
docs:
	@if [ -d docs/static ]; then rm -rf docs/static; fi
	@$(MAKE) docs/static
	@cp -f docs/src/pages/index/content.md README.md

docs/static: docs/src
	@if [ ! -d docs/static ]; then mkdir docs/static; fi
	@PYTHONPATH=$(PWD)/docs/src python docs/src/main.py
	# Docs generated: file://$(PWD)/docs/static/index.html
