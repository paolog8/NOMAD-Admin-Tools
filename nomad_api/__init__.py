"""
NOMAD API Package

This package provides functionality for interacting with the NOMAD Materials Database API.
"""

# Import key classes and functions
from nomad_api.client import NomadClient
from nomad_api.auth import (
    authenticate, 
    get_token, 
    get_token_from_env, 
    verify_token,
    OASIS_OPTIONS
)
from nomad_api.data import (
    get_all_samples_with_authors,
    get_user_details,
    query_sample_entries
)

# Import utility functions
from nomad_api.utils.convenience import (
    get_client,
    get_batch_ids,
    get_ids_in_batch,
    get_uploads_by_author
)

# Version information
__version__ = '0.1.0'