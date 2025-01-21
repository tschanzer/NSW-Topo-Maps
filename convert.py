"""Script to convert the JSON array to a name:URL mappping."""

import json

PREFIX = 'https://portal.spatial.nsw.gov.au/download/geopdf/'


def main():
    """Convert the JSON array to a name:URL mappping."""

    with open('nsw_topo_map_urls.json', 'r', encoding='utf8') as f:
        original = json.load(f)['maps']

    new = {}
    original: list[str]
    for url in original:
        if url.startswith(PREFIX):
            url = url.removeprefix(PREFIX).removesuffix('.pdf')
            # We now have something like 25k/9135-1N+ABERBALDIE
            scale, full_name = url.split('/')
            # Drop the numerical code at the start of full_name and
            # replace + with _ in multi-word place names
            name = '_'.join(full_name.split('+')[1:]).lower()
            new[name] = {'full_name': full_name, 'scale': scale}

    with open('nsw_topo_map_names_scales.json', 'w', encoding='utf8') as f:
        json.dump(new, f, indent='    ')


if __name__ == '__main__':
    main()
