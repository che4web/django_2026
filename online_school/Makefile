FRONTEND_DIST ?= dist
VUE_APP = online-school-vue
DJANGO_APP ?= .
DJANGO_TEMPLATE_DIR ?= $(DJANGO_APP)/templates
DJANGO_STATIC_DIR ?= $(DJANGO_APP)/static

.DEFAULT_GOAL := deploy

.PHONY: build copy-template copy-static deploy clean-dist

build:
	cd $(VUE_APP) && npm run build

copy-template: build
	mkdir -p $(DJANGO_TEMPLATE_DIR)
	cp $(VUE_APP)/$(FRONTEND_DIST)/index.html $(DJANGO_TEMPLATE_DIR)/index.html

copy-static: build
	mkdir -p $(DJANGO_STATIC_DIR)
	cp -R $(VUE_APP)/$(FRONTEND_DIST)/static/. $(DJANGO_STATIC_DIR)

deploy: copy-template copy-static

clean-dist:
	rm -rf $(FRONTEND_DIST)
