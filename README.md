# Scraping LinkedIn Profiles

Run **LinkedIn Public Profile Scraper** from Apify's web interface without
writing code, or call it with Python, JavaScript or cURL to turn public LinkedIn
profile URLs into structured profile data.

This repository contains a no-code walkthrough, working API examples, a
sanitized input, a sample JSON response and a CSV representation of the result.

[Open LinkedIn Public Profile Scraper on Apify](https://apify.com/datascraperes/linkedin-public-profile-scraper?fpr=edudata)

## What this repository helps you do

- Scrape LinkedIn profiles from a list of public profile URLs.
- Extract publicly visible name, headline, location, About, experience,
  education and other profile sections when LinkedIn exposes them.
- Keep one auditable result for each submitted URL, including invalid or
  temporarily unavailable inputs.
- Export LinkedIn profile data as JSON, CSV or a spreadsheet from the Apify
  Dataset.

The Actor uses LinkedIn's public guest view. You do not need a LinkedIn login,
LinkedIn credentials or LinkedIn cookies to run it.

## Example result

The repository includes a sanitized example in
[`data/sample-output.json`](data/sample-output.json) and a flat tabular version
in [`data/sample-output.csv`](data/sample-output.csv).

```json
{
  "success": true,
  "status": "success",
  "inputUrl": "https://www.linkedin.com/in/example-profile/",
  "profileUrl": "https://www.linkedin.com/in/example-profile/",
  "publicIdentifier": "example-profile",
  "scrapedAt": "2026-01-15T12:00:00Z",
  "error": null,
  "dataQuality": {
    "level": "extended",
    "publicFields": ["fullName", "headline", "location", "about", "experience"],
    "publicFieldCount": 5
  },
  "profile": {
    "fullName": "Example Name",
    "headline": "Example professional headline",
    "location": "City, Country",
    "followers": "1200",
    "connections": "500+",
    "about": "Sanitized public profile summary.",
    "experience": [],
    "education": [],
    "skills": [],
    "certifications": [],
    "languages": []
  }
}
```

The sample is deliberately sanitized. It explains the response shape and is
not a claim that an `example-profile` page exists.

## Run without code

You can run the hosted Actor directly from the Apify web interface. This is the
simplest way to scrape LinkedIn profiles if you do not need a program.

1. Open [LinkedIn Public Profile Scraper on Apify](https://apify.com/datascraperes/linkedin-public-profile-scraper?fpr=edudata).
2. Open the **Input** tab and paste one or more public URLs into **LinkedIn profile URLs**.
3. Click **Start**. No LinkedIn login or cookie is required.
4. Open the **Dataset** tab when the run finishes.
5. Review `status`, `profile.fullName`, `profile.headline` and `dataQuality`.
6. Export the Dataset as JSON, CSV or Excel when you need a file for a spreadsheet or another tool.

Use [`docs/no-code-guide.md`](docs/no-code-guide.md) for the field-by-field
walkthrough and [`data/sample-input.json`](data/sample-input.json) for the
input shape.

## Try it with Apify's free plan

Apify's Free plan includes **$5 in monthly prepaid usage** that can be spent in
the Apify Store or on your own Actors. No credit card is required to start. A
small test of LinkedIn Public Profile Scraper can use that credit while it is
available; it is not unlimited free usage.

Unused credits expire at the end of the billing cycle and do not roll over.
See the [current Apify pricing](https://apify.com/pricing?fpr=edudata) before
running a larger batch.

## Quick start for developers

### Python

#### 1. Install the client

```bash
pip install apify-client
```

#### 2. Set your Apify token

```bash
export APIFY_API_TOKEN="your-token"
```

On Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

#### 3. Run the example

```bash
python examples/python/scrape_linkedin_profiles.py
```

The example reads [`data/sample-input.json`](data/sample-input.json), starts
the hosted Actor and prints the returned Dataset items.

## Input example

```json
{
  "profileUrls": [
    "https://www.linkedin.com/in/example-profile/",
    "https://www.linkedin.com/company/example/"
  ]
}
```

Use only public profile URLs in the form
`https://www.linkedin.com/in/<public-identifier>/`. The second URL above is
intentionally invalid so the sample also shows the auditable error shape.
See the complete contract in [`docs/input-reference.md`](docs/input-reference.md).

## Request examples

### cURL

See [`examples/curl-request.md`](examples/curl-request.md) for a synchronous
API request that returns Dataset items.

### Python

See [`examples/python/scrape_linkedin_profiles.py`](examples/python/scrape_linkedin_profiles.py)
for a minimal request and
[`examples/python/batch_linkedin_profiles.py`](examples/python/batch_linkedin_profiles.py)
for repeated `--profile-url` arguments.

### JavaScript

See [`examples/javascript/request.mjs`](examples/javascript/request.mjs).

All examples use the hosted Apify Actor. They do not expose a proxy, bypass
access controls or require the Actor source code locally.

## Output fields

The default Dataset returns one item for each submitted URL that can be written
within the run spending limit.

| Field | Meaning |
| --- | --- |
| `success` | `true` only when a public profile was extracted. |
| `status` | `success`, `invalid_url`, `not_found`, `login_required`, `blocked`, `rate_limited`, `network_error` or `parse_error`. |
| `inputUrl` | The URL submitted to the Actor. |
| `profileUrl` | The normalized public profile URL, or `null`. |
| `publicIdentifier` | The LinkedIn public identifier, or `null`. |
| `profile` | Public profile fields, or `null` for an unsuccessful item. |
| `dataQuality` | Which public fields were available on that page. |
| `error` | A diagnostic message for an unsuccessful item, otherwise `null`. |
| `scrapedAt` | ISO timestamp for the result. |

Profile fields can include full name, headline, location, followers,
connections, profile image, About, experience, education, skills,
certifications and languages. Missing public fields remain `null` or an empty
list; they are never guessed.

See [`docs/output-reference.md`](docs/output-reference.md) for the full public
output contract.

## Common use cases

Read [`docs/use-cases.md`](docs/use-cases.md) for complete examples covering:

- recruiting and candidate research from public profile URLs;
- sales or CRM enrichment using public professional fields;
- workforce, market and competitive research with auditable JSON output.

## Scrape LinkedIn profiles from a list of URLs

Put one or more public profile URLs in the `profileUrls` array. The hosted web
workflow accepts the same input as the API examples, so a batch does not require
Python or a custom integration. The Actor processes each URL independently and
keeps unsuccessful inputs visible in the Dataset.

For a scripted batch, use
[`examples/python/batch_linkedin_profiles.py`](examples/python/batch_linkedin_profiles.py).

## Export LinkedIn profile data to CSV

The Apify Dataset can be exported as CSV after a run. For a local conversion of
saved JSON output, use
[`examples/python/export_linkedin_profiles_csv.py`](examples/python/export_linkedin_profiles_csv.py).
It flattens the most useful identity and quality fields while retaining the
complete JSON response for workflows that need nested experience or education.

## LinkedIn profile data JSON example

The nested response in [`data/sample-output.json`](data/sample-output.json)
keeps the original profile structure. Use `profile.experience`,
`profile.education` and `profile.skills` for structured sections, and use
`dataQuality.publicFields` before assuming a section exists.

## FAQ

See [`docs/faq.md`](docs/faq.md) for questions derived from the actual Actor
input, output and pricing behavior.

## Limits and pricing

The Actor charges **$0.001 per successfully extracted public profile**, which
is **$1 per 1,000 successful profile extractions**. Invalid URLs, inaccessible
public profiles, blocks, rate limits and parser failures do not create the
successful-profile charge. Apify plan-based Dataset storage, data transfer or
other platform costs may still apply.

Each successful submitted URL is an independent `profile` event. Submitting
the same URL twice can therefore produce two successful outputs and two
chargeable profile events.

The public guest view varies by profile. If LinkedIn asks for sign-in for a
particular page, the Actor does not log in or request credentials; it records
the result as unavailable public data, such as `login_required`.

## Hosted version

Use the hosted version when you need repeatable execution, batching, scheduling,
API access or Dataset storage without managing scraping infrastructure yourself.
It can be run from the web interface or called programmatically:

[Open LinkedIn Public Profile Scraper on Apify](https://apify.com/datascraperes/linkedin-public-profile-scraper?fpr=edudata)

## Responsible use

Use only public profile URLs for a lawful, documented purpose. Respect
[LinkedIn's User Agreement](https://www.linkedin.com/legal/user-agreement),
applicable data-protection laws and any other requirements that apply to your
use case. Do not use this Actor to access private content, send spam, harass
people, discriminate or make high-impact automated decisions about individuals.

Never commit API tokens, cookies, proxy URLs or other credentials to this
repository.

## Support

For a problem with the examples, [open a GitHub issue](https://github.com/datacrawler-edu/linkedin-public-profile-scraper/issues)
with the command, sanitized input and error message. For an execution problem,
include the Apify run ID but never include your token.

## License

This repository is released under the MIT License.
