import os
import yaml

from pathlib import Path

def get_languages():
    """Get languages that are currently active on website."""
    current_dir = Path(__file__)
    toplevel_dir = current_dir.parent.parent.parent
    config_path = toplevel_dir / "config.yaml"
    with open(config_path) as f:
        data = yaml.safe_load(f)
    return list(data["languages"])


def translate_file(
        input_filepath: str, output_filepath: str, translation_func: callable
) -> None:
    """Apply translation function to text in a file and save to new location.

    Parameters
    ----------
    input_filepath : str
        Path to file to be translated
    output_filepath : str
        Path where translated file will be saved.
    translation_func : callable
        Function from str to str which translates input.

    Returns
    -------
    None
    """
    with open(input_filepath, 'r') as input_file:
        data = input_file.read()

    transformed_data = translation_func(data)

    with open(output_filepath, 'w') as output_file:
        output_file.write(transformed_data)
