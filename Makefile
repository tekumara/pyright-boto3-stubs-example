MAKEFLAGS += --warn-undefined-variables
SHELL = /bin/bash -o pipefail
.DEFAULT_GOAL := typings

ifndef VIRTUAL_ENV
  $(error Please activate your virtual environment)
endif


# install pyright stubs
typings: $(VIRTUAL_ENV)
	rm -rf typings/

	$(VIRTUAL_ENV)/bin/python -m mypy_boto3

	# workaround for https://github.com/vemel/mypy_boto3_builder/issues/39
	mkdir -p typings/boto3
	cp $(VIRTUAL_ENV)/lib/python*/site-packages/mypy_boto3/boto3_init_gen.py typings/boto3/__init__.pyi

	# install generated stubs for implicit type inference on boto3.client/boto3.resource
	mkdir -p typings/mypy_boto3/ec2
	for f in __init__ client paginator service_resource waiter type_defs; do \
		cp $(VIRTUAL_ENV)/lib/python*/site-packages/mypy_boto3/ec2/$$f.py typings/mypy_boto3/ec2/$$f.pyi; done

	# install packaged stubs for explicit type annotation (also used by the generated stubs)
	mkdir -p typings/mypy_boto3_ec2
	for f in __init__ client paginator service_resource waiter type_defs; do \
		cp $(VIRTUAL_ENV)/lib/python*/site-packages/mypy_boto3_ec2/$$f.py typings/mypy_boto3_ec2/$$f.pyi; done

	touch typings
