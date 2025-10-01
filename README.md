# Description

Certified 'artisanal' Python Fast API project scaffolding with UV. No AI, just me (Laurence) writing up some boilerplate code as it's often a foundation for my web services at the moment. 

# Pre requisites

Python, UV

# Installation
uv sync --all-extras

# Update dependencies (if you want newer versions)
uv lock --upgrade

# Add a new dependency
uv add <package-name>

# Run application

`uv run uvicorn app.main:app --reload`
