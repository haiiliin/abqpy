lock:
	pdm lock --python=">=3.8,<3.10"
	pdm lock --python=">=3.10,<3.15" --append
