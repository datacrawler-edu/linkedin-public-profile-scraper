"""Run a batch of public LinkedIn profile URLs supplied on the command line."""

from __future__ import annotations

import argparse
import json
import os

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/linkedin-public-profile-scraper"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile-url",
        action="append",
        required=True,
        help="Public LinkedIn profile URL; repeat this option for a batch.",
    )
    args = parser.parse_args()

    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input={"profileUrls": args.profile_url})
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
