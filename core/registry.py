from validators.python_validator import validate_python
from formatter.python_formatter import format_python

from validators.js_validator import validate_js
from formatter.js_formatter import format_js

from validators.cobol_validator import validate_cobol
from formatter.cobol_formatter import format_cobol

LANGUAGE_REGISTRY = {
    "python": {
        "validate": validate_python,
        "format": format_python,
    },
    "javascript": {
        "validate": validate_js,
        "format": format_js,
    },
    "cobol": {
        "validate": validate_cobol,
        "format": format_cobol,
    },
}