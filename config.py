import logging

LOG_FILENAME = "Netflix2TraktImportLog1.log"
LOG_LEVEL = logging.INFO
VIEWING_HISTORY_FILENAME = "NetflixViewingHistory1.csv"

# Set the datetime format of the csv file (default: %d.%m.%y for 05.02.21)
# Use %Y-%m-%d for 2021-02-05 (Canada, ...)
CSV_DATETIME_FORMAT = "%m/%d/%y"

TMDB_API_KEY = ""
TMDB_LANGUAGE = "en"
TMDB_DEBUG = True
TMDB_SYNC_STRICT = False

TRAKT_API_CLIENT_ID = ""
TRAKT_API_CLIENT_SECRET = ""
