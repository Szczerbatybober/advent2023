clean:
	@echo "Cleaning..."
	@rm -rf .pytest_cache/
	@rm -rf srcgen/
	@rm -rf dist/
	@rm -rf .ruff_cache
	@rm -rf .hypothesis
	@rm -rf .coverage
	@find */tests | grep -E "(__pycache__$$)" | xargs rm -rf