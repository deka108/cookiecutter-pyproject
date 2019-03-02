test-cookiecutter:
	@rm -rf tmp/my-project
	@yes "" | cookiecutter . -o tmp