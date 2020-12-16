class Column:
    def __init__(self, field_type, **kwargs):
        self.constraints = tuple(['type', 'not_null', 'default', 'primary_key', 'autoincrement', 'unique', 'foreign_key', ])
        self.constraints_values = (
            field_type().get_type(),
            kwargs.get('not_null', False),
            kwargs.get('default'),
            kwargs.get('primary_key', False),
            kwargs.get('autoincrement', False),
            kwargs.get('unique', False),
            kwargs.get('foreign_key'),
        )

    def keywords(self):
        return tuple(
            (key_word, self.keyword_format(key_word, value)) 
            for key_word, value in zip(self.constraints, self.constraints_values) 
            if value)

    @staticmethod
    def keyword_format(key_word: str, value: any) -> str:
        if key_word == 'default':
            return 'DEFAULT {}'.format(value)
        elif key_word in ['type', 'on_delete', 'on_update']:
            return value.upper()
        elif key_word == 'foreign_key':
            fk = value if isinstance(value, str) else str(value)
            return '{}({})'.format(*fk.split('.'))
        return key_word.upper().replace('_', ' ')
