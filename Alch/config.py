class Config:
    SQL_RESPONSE_LIMIT = 1844674407370955161
    PRAGMA_SCRIPT = {
        'foreign_key': 'PRAGMA foreign_keys = "1";\n',
        'auto_vacuum': 'PRAGMA auto_vacuum = 0;',
    }
    JOIN_TYPES = ['LEFT', 'INNER', 'RIGHT', 'FULL', ]
    DEFAULT_JOIN = 'LEFT'
