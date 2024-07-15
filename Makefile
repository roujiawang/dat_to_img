.PHONY: image cleandat cleanimg

# Define paths
VENV = env
PYTHON = $(VENV)/bin/python
SCRIPT = dattoimg.py
DAT_FOLDER = dat
IMG_FOLDER = img

# Make image
image:
	@echo "Activating virtual environment..."
	@. $(VENV)/bin/activate && $(PYTHON) $(SCRIPT)
	@echo "Deactivating virtual environment..."

# Clean dat folder
cleandat:
	@echo "Cleaning dat folder..."
	@rm -rf $(DAT_FOLDER)/*

# Clean img folder
cleanimg:
	@echo "Cleaning img folder..."
	@rm -rf $(IMG_FOLDER)/*
