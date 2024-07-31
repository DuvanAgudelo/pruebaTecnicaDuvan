"""
Regular expression pattern for validating names.

This pattern accepts alphanumeric characters with diacritics, including:
- Lowercase and uppercase letters (a-z, A-Z)
- Vowels with diacritics (á, é, í, ó, ú, ü, ñ and their uppercase counterparts)
- Numbers (1-9)
- Special characters (apostrophe ('), hyphen (-), period (.), and space ( ))
"""

NAME_PATTERN = r"^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ1-9\'\-.\s]+$"
