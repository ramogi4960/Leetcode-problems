from platform import machine, processor, system, version, python_implementation, python_version, python_version_tuple

print(*python_version_tuple(), sep="\n")