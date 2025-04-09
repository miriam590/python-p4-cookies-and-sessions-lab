import warnings

# Suppress deprecation warnings
warnings.filterwarnings(
    "ignore",
    message="The '__version__' attribute is deprecated",
    category=DeprecationWarning
)
