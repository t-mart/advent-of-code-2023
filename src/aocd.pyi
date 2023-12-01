# stubs for aocd module

# "If no execution environment is configured, try to resolve using the local
# directory src. It is common for Python projects to place local source files
# within a directory of this name."
# - https://github.com/microsoft/pyright/blob/main/docs/import-resolution.md#resolution-order

def get_data(
    session: str | None = None,
    day: int | None = None,
    year: int | None = None,
    block: bool = False,
) -> str: ...
