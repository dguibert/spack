# $spack/lib/spack/docsest/data/config/modules.yaml
is_feature = $(if $(filter $1,$(.FEATURES)),T)
ifneq ($(call is_feature,oneshell),T)
	$(error This Makefile only works with a Make program that supports "oneshell" feature (version>=3.82))
endif

.ONESHELL:
.POSIX:

SPACK ?= spack

.PHONY: all clean env

all: env

spack.lock: spack.yaml packages-spartan-x86_64.yaml
	$(SPACK) -e . concretize -f

packages-spartan-x86_64.yaml: ../generate-packages.yaml.sh
	../generate-packages.yaml.sh

env.mk: spack.lock
	$(SPACK) -e . env depfile -o $@ --make-target-prefix spack

env: spack/env
	$(info Environment installed!)

clean:
	rm -rf spack.lock env.mk spack/

ifeq (,$(filter clean,$(MAKECMDGOALS)))
include env.mk
endif
