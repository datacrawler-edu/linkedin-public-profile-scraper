# Input reference

The Actor accepts one required field:

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| `profileUrls` | Array of strings | Yes | `https://www.linkedin.com/in/public-identifier/` | One or more public LinkedIn profile URLs. |

## Accepted URL format

Use a public profile URL under `/in/`:

```text
https://www.linkedin.com/in/<public-identifier>/
```

Do not submit company pages, job URLs, search URLs, email addresses or phone
numbers. Invalid URLs are returned as auditable Dataset items with
`status: "invalid_url"` when the item can be written.

## Validation and limits

- `profileUrls` must contain at least one non-empty string.
- Duplicate URLs are processed independently; two successful submissions can
  create two successful profile events.
- The Actor uses the public guest view and does not require LinkedIn login,
  credentials or cookies.
- A run spending limit can stop later chargeable profile extractions. Keep the
  Dataset and run URL to audit what was processed.
