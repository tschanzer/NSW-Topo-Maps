"""Script to convert the JSON array to a name:URL mappping."""

import json

PREFIX_25K = 'https://portal.spatial.nsw.gov.au/download/geopdf/25k/'


def main():
    """Convert the JSON array to a name:URL mappping."""

    with open('NSW_topo_maps.json', 'r', encoding='utf8') as f:
        original = json.load(f)['maps']

    new = {}
    original: list[str]
    for url in original:
        if url.startswith(PREFIX_25K):
            code = url.removeprefix(PREFIX_25K).removesuffix('.pdf')
            name = ' '.join(code.split('+')[1:]).lower()
            new[name] = code

    with open('nsw_topo_maps_new.json', 'w', encoding='utf8') as f:
        json.dump(new, f, indent='    ')


if __name__ == '__main__':
    main()
