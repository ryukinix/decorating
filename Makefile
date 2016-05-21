PYTHON = python3
INSTALL = install
DEVELOP = develop
TARGET = setup.py
TEST_DEPLOY = sdist bdist_wheel upload --repository pypitest --sign
TEST_REGISTER = register --repository pypitest
DEPLOY = sdist bdist_wheel upload --repository pypi --sign
REGISTER = register --repository pypi
BUILD_GARBAGE = build/ dist/
CHECK = check --metadata --restructuredtext --strict
CLEAN = clean
UNINSTALL = --uninstall
BUILD = sdist bdist_wheel
ENVIROMENT = *.egg-info *.env

all: install
	 @make clean

check:
	@echo "+===============+"
	@echo "|     CHECK     |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(CHECK)
	@echo "ok!"

clean:
	@make clean-build
	@make clean-enviroment

clean-environment:
	@echo "+===============+"
	@echo "|   CLEAN ENV  |"
	@echo "+===============+"
	rm -rfv $(ENVIROMENT)

clean-build:
	@echo "+===============+"
	@echo "|  CLEAN BUILD  |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(CLEAN)
	find . -name __pycache__ -or -name *.pyc| xargs rm -rfv;
	rm -rfv $(BUILD_GARBAGE)

install:
	@echo "+===============+"
	@echo "|    INSTALL    |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(INSTALL)

build:
	@echo "+===============+"
	@echo "|    BUILD      |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(BUILD)


develop:
	@echo "+===============+"
	@echo "|    DEVELOP    |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(DEVELOP)

test-register:
	@make check
	@echo "+===============+"
	@echo "| TEST-REGISTER |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(TEST_REGISTER) 

develop-uninstall:
	@echo "+===============+"
	@echo "| DEV UNINSTALL |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(DEVELOP) $(UNINSTALL)
	@make clean

test-deploy:
	@make check
	@echo "+===============+"
	@echo "| TEST-DEPLOY   |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(TEST_DEPLOY) 

deploy:
	@make check
	@echo "+===============+"
	@echo "|   DEPLOY      |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(DEPLOY)


register:
	@make check
	@echo "+===============+"
	@echo "|   REGISTER    |"
	@echo "+===============+"
	$(PYTHON) $(TARGET) $(REGISTER)

help:
	@echo "+=============================================+"
	@echo "|                H  E  L  P                   |"
	@echo "+=============================================+"
	@echo "----------------------------------------------"
	@echo "make check:"
	@echo "	 check the build pass on PyPI"
	@echo 
	@echo "make clean:"
	@echo "	 clean the build (build/ __pyache__, sdist/)"
	@echo 
	@echo "make install:"
	@echo "	 install the package in your system"
	@echo 
	@echo "make build:"
	@echo "  build the package as egg-file"
	@echo "make develop:"
	@echo "	 install in develop mode (symlink)"
	@echo 
	@echo "make develop-uninstall:"
	@echo "	 uninstall develop files and clean build"
	@echo 
	@echo "make test-register:"
	@echo "	 test register using the testPyPI server "
	@echo 
	@echo "test-deploy:"
	@echo "	 test deploy using the testPyPI server"
	@echo 
	@echo "deploy:"
	@echo "	 deploy to PyPY"
	@echo 
	@echo "register:"
	@echo "	 register to PyPI"

