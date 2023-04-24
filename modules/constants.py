# Set the user files and options
VERSION_MAJOR: str = '2.00'
VERSION_MINOR: str = '1'
CLONE_LIST_METADATA_DOWNLOAD_LOCATION: str = 'https://raw.githubusercontent.com/unexpectedpanda/retool-clonelists-metadata/main'
CLONE_LIST_METADATA_DOWNLOAD_LOCATION_KEY: str = 'cloneListMetadataUrl'
PROGRAM_DOWNLOAD_LOCATION: str = 'https://raw.githubusercontent.com/unexpectedpanda/retool/main'
PROGRAM_DOWNLOAD_LOCATION_KEY: str = 'programUrl'
CONFIG_FILE: str = 'config/internal-config.json'
IGNORE_TAGS_KEY: str = "ignoreTags"
DISC_RENAME_KEY: str = "discRename"
PROMOTE_EDITIONS_KEY: str = 'promoteEditions'
DEMOTE_EDITIONS_KEY: str = 'demoteEditions'
MODERN_EDITIONS_KEY: str = 'modernEditions'
LANGUAGES_KEY: str = 'languages'
REGION_ORDER_KEY: str = 'defaultRegionOrder'
VIDEO_ORDER_KEY: str = 'defaultVideoOrder'
CLONE_LISTS_KEY: str = 'cloneLists'
METADATA_KEY: str = 'metadata'
SYSTEM_LANGUAGE_ORDER_KEY: str = 'language order'
SYSTEM_REGION_ORDER_KEY: str = 'region order'
SYSTEM_VIDEO_ORDER_KEY: str = 'video order'
SYSTEM_LIST_PREFIX_KEY: str = 'list prefix'
SYSTEM_LIST_SUFFIX_KEY: str = 'list suffix'
SYSTEM_EXCLUSIONS_OPTIONS_KEY: str = 'exclusions and options'
USER_CONFIG_KEY: str = 'userConfig'
USER_LANGUAGE_ORDER_KEY: str = 'language order'
USER_REGION_ORDER_KEY: str = 'region order'
USER_VIDEO_ORDER_KEY: str = 'video order'
USER_LIST_PREFIX_KEY: str = 'list prefix'
USER_LIST_SUFFIX_KEY: str = 'list suffix'
USER_GUI_SETTINGS_KEY: str = 'gui settings'
USER_FILTERS_PATH: str = 'config/systems'
SANITIZED_CHARACTERS: tuple[str, ...] = (':', '\\', '/', '<', '>', '"', '|', '?', '*')
RESERVED_FILENAMES: tuple[str, ...] = ('con', 'prn', 'aux', 'nul', 'com[1-9]', 'lpt[1-9]')