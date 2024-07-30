from webargs.flaskparser import use_kwargs
from webargs import validate, fields

password_length_config = {
    "length": fields.Int(
        missing=10,
        validate=[validate.Range(min=8, max=100, min_inclusive=True, max_inclusive=True)],
    )
}
